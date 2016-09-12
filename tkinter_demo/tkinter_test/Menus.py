
# will return x11, win32 or aqua
##root.tk.call('tk', 'windowingsystem')

# --Menubars

# Before you Start
##root.option_add('*tearOff', FALSE)

# Creating a Menubar
##win = Toplevel(root)
##menubar = Menu(win)
##win['menu'] = menubar

# Adding Menus
##menubar = Menu(parent)
##menu_file = Menu(menubar)
##menu_edit = Menu(menubar)
##menubar.add_cascade(menu=menu_file, label='File')
##menubar.add_cascade(menu=menu_edit, label='Edit')

# Adding Menu Items
##menu_file.add_command(label='New', command=newFile)
##menu_file.add_command(label='Open...', command=openFile)
##menu_file.add_command(label='Close', command=closeFile)

# Types of Menu Items
# "separator"
##menu_file.add_separator()
# "checkbutton" and "radiobutton" menu items
##check = StringVar()
##menu_file.add_checkbutton(label='Check', variable=check, onvalue=1, offvalue=0)
##radio = StringVar()
##menu_file.add_radiobutton(label='One', variable=radio, value=1)
##menu_file.add_radiobutton(label='Two', variable=radio, value=2)

# --Platform Menus

# Windows
##sysmenu = Menu(menubar, name='system')
##menubar.add_cascade(menu=sysmenu)

# --Contextual Menus

from tkinter import *
root = Tk()
menu = Menu(root)
for i in ('One', 'Two', 'Three'):
    menu.add_command(label=i)
if (root.tk.call('tk', 'windowingsystem')=='aqua'):
    root.bind('<2>', lambda e: menu.post(e.x_root, e.y_root))
    root.bind('<Control-1>', lambda e: menu.post(e.x_root, e.y_root))
else:
    root.bind('<3>', lambda e: menu.post(e.x_root, e.y_root))
