##
##canvas = Canvas(parent)
##
### Creating Items
##canvas.create_line(10, 10, 200, 50)
##
##
##from tkinter import *
##from tkinter import ttk
##
##lastx, lasty = 0, 0
##
##def xy(event):
##    global lastx, lasty
##    lastx, lasty = event.x, event.y
##
##def addLine(event):
##    global lastx, lasty
##    canvas.create_line((lastx, lasty, event.x, event.y))
##    lastx, lasty = event.x, event.y
##
##root = Tk()
##root.columnconfigure(0, weight=1)
##root.rowconfigure(0, weight=1)
##
##canvas = Canvas(root)
##canvas.grid(column=0, row=0, sticky=(N, W, E, S))
##canvas.bind("<Button-1>", xy)
##canvas.bind("<B1-Motion>", addLine)
##
##root.mainloop()
##
### Item Attributes
##canvas.create_line(10, 10, 200, 50, fill='red', width=3)
##
##id = canvas.create_line(0, 0, 10, 10, -fill red)
##...
##canvas.itemconfigure(id, fill='blue', width=2)
##
### Bindings
##canvas.tag_bind(id, '<1>', ...)
##
##
##color = "black"
##def setColor(newcolor):
##    global color
##    color = newcolor
##
##def addLine(event):
##    global lastx, lasty
##    canvas.create_line((lastx, lasty, event.x, event.y), fill=color)
##    lastx, lasty = event.x, event.y
##
##id = canvas.create_rectangle((10, 10, 30, 30), fill="red")
##canvas.tag_bind(id, "<Button-1>", lambda x: setColor("red"))
##id = canvas.create_rectangle((10, 35, 30, 55), fill="blue")
##canvas.tag_bind(id, "<Button-1>", lambda x: setColor("blue"))
##id = canvas.create_rectangle((10, 60, 30, 80), fill="black")
##canvas.tag_bind(id, "<Button-1>", lambda x: setColor("black"))	
##
##
### Tags
##>>> c = Canvas(root)
##>>> c.create_line(10, 10, 20, 20, tags=('firstline', 'drawing'))
##1
##>>> c.create_rectangle(30, 30, 40, 40, tags=('drawing'))
##2
##>>> c.addtag('rectangle', 'withtag', 2)
##>>> c.addtag('polygon', 'withtag', 'rectangle')
##>>> c.gettags(2)
##('drawing', 'rectangle', 'polygon')
##>>> c.dtag(2, 'polygon')
##>>> c.gettags(2)
##('drawing', 'rectangle')	
##>>> c.find_withtag('drawing')
##(1, 2)
##
### Let's use tags first to put a border around whichever item
### in our color palette is currently selected.
##def setColor(newcolor):
##    global color
##    color = newcolor
##    canvas.dtag('all', 'paletteSelected')
##    canvas.itemconfigure('palette', outline='white')
##    canvas.addtag('paletteSelected', 'withtag', 'palette%s' % color)
##    canvas.itemconfigure('paletteSelected', outline='#999999')
##
##id = canvas.create_rectangle((10, 10, 30, 30), fill="red", tags=('palette', 'palettered'))
##id = canvas.create_rectangle((10, 35, 30, 55), fill="blue", tags=('palette', 'paletteblue'))
##id = canvas.create_rectangle((10, 60, 30, 80), fill="black", tags=('palette', 'paletteblack', 'paletteSelected'))
##
### Let's also use tags to make the current stroke we're drawing appear
### more visible; when we release the mouse we'll put it back to normal.
##setColor('black')
##canvas.itemconfigure('palette', width=5)
##
##def addLine(event):
##    global lastx, lasty
##    canvas.create_line((lastx, lasty, event.x, event.y), fill=color, width=5, tags='currentline')
##    lastx, lasty = event.x, event.y
##
##def doneStroke(event):
##    canvas.itemconfigure('currentline', width=1)        
##
##canvas.bind("<B1-ButtonRelease>", doneStroke)

# Scrolling
from tkinter import *
from tkinter import ttk
root = Tk()

h = ttk.Scrollbar(root, orient=HORIZONTAL)
v = ttk.Scrollbar(root, orient=VERTICAL)
canvas = Canvas(root, scrollregion=(0, 0, 1000, 1000), yscrollcommand=v.set, xscrollcommand=h.set)
h['command'] = canvas.xview
v['command'] = canvas.yview
ttk.Sizegrip(root).grid(column=1, row=1, sticky=(S,E))

canvas.grid(column=0, row=0, sticky=(N,W,E,S))
h.grid(column=0, row=1, sticky=(W,E))
v.grid(column=1, row=0, sticky=(N,S))
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)

lastx, lasty = 0, 0

def xy(event):
    global lastx, lasty
    lastx, lasty = canvas.canvasx(event.x), canvas.canvasy(event.y)

def setColor(newcolor):
    global color
    color = newcolor
    canvas.dtag('all', 'paletteSelected')
    canvas.itemconfigure('palette', outline='white')
    canvas.addtag('paletteSelected', 'withtag', 'palette%s' % color)
    canvas.itemconfigure('paletteSelected', outline='#999999')

def addLine(event):
    global lastx, lasty
    x, y = canvas.canvasx(event.x), canvas.canvasy(event.y)
    canvas.create_line((lastx, lasty, x, y), fill=color, width=5, tags='currentline')
    lastx, lasty = x, y

def doneStroke(event):
    canvas.itemconfigure('currentline', width=1)        
        
canvas.bind("<Button-1>", xy)
canvas.bind("<B1-Motion>", addLine)
canvas.bind("<B1-ButtonRelease>", doneStroke)

id = canvas.create_rectangle((10, 10, 30, 30), fill="red", tags=('palette', 'palettered'))
canvas.tag_bind(id, "<Button-1>", lambda x: setColor("red"))
id = canvas.create_rectangle((10, 35, 30, 55), fill="blue", tags=('palette', 'paletteblue'))
canvas.tag_bind(id, "<Button-1>", lambda x: setColor("blue"))
id = canvas.create_rectangle((10, 60, 30, 80), fill="black", tags=('palette', 'paletteblack', 'paletteSelected'))
canvas.tag_bind(id, "<Button-1>", lambda x: setColor("black"))

setColor('black')
canvas.itemconfigure('palette', width=5)
root.mainloop()

