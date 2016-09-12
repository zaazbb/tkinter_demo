# vscale.tcl --
#
# This demonstration script shows an example with a vertical scale.

##if {![info exists widgetDemo]} {
##    error "This script should be run from the \"widget\" demo."
##}
assert 'widgetDemo' in globals(), \
'This script should be run from the "widget" demo.'

##package require Tk

##set w .vscale
##catch {destroy $w}
##toplevel $w
##wm title $w "Vertical Scale Demonstration"
##wm iconname $w "vscale"
##positionWindow $w
demo_name = 'vscale'
if demo_name in globals()['demo_name']:
    globals()['demo_name'][demo_name].destroy()
w = globals()['demo_name'][demo_name] = Toplevel(root)
w.wm_title('Vertical Scale Demonstration')
w.wm_iconname('vscale')
positionWindow(w)

##label $w.msg -font $font -wraplength 3.5i -justify left -text "An arrow and a vertical scale are displayed below.  If you click or drag mouse button 1 in the scale, you can change the size of the arrow."
##pack $w.msg -side top -padx .5c
msg = Label(w, font=font, wraplength='3.5i', justify=LEFT, text="An arrow and a vertical scale are displayed below.  If you click or drag mouse button 1 in the scale, you can change the size of the arrow.")
msg.pack(side=TOP, padx='.5c')

## See Code / Dismiss buttons
##set btns [addSeeDismiss $w.buttons $w]
##pack $btns -side bottom -fill x
btns = addSeeDismiss(ttk.Frame(w), demo_name)
btns.pack(side='bottom', fill='x')

##frame $w.frame -borderwidth 10
##pack $w.frame
frame = Frame(w, borderwidth=10)
frame.pack()

##scale $w.frame.scale -orient vertical -length 284 -from 0 -to 250 \
##	-command "setHeight $w.frame.canvas" -tickinterval 50
##canvas $w.frame.canvas -width 50 -height 50 -bd 0 -highlightthickness 0
##$w.frame.canvas create polygon 0 0 1 1 2 2 -fill SeaGreen3 -tags poly
##$w.frame.canvas create line 0 0 1 1 2 2 0 0 -fill black -tags line
##frame $w.frame.right -borderwidth 15
##pack $w.frame.scale -side left -anchor ne
##pack $w.frame.canvas -side left -anchor nw -fill y
##$w.frame.scale set 75
##
##proc setHeight {w height} {
##    incr height 21
##    set y2 [expr {$height - 30}]
##    if {$y2 < 21} {
##	set y2 21
##    }
##    $w coords poly 15 20 35 20 35 $y2 45 $y2 25 $height 5 $y2 15 $y2 15 20
##    $w coords line 15 20 35 20 35 $y2 45 $y2 25 $height 5 $y2 15 $y2 15 20
##}
def setHeight(w, height):
    height += 21
    y2 = height - 30
    if y2 < 21:
        y2 = 21
    w.coords('poly',
             15, 20, 35, 20, 35, y2, 45, y2, 25, height, 5, y2, 15, y2, 15, 20)
    w.coords('line',
             15, 20, 35, 20, 35, y2, 45, y2, 25, height, 5, y2, 15, y2, 15, 20)
canvas = Canvas(frame, width=50, height=50, bd=0, highlightthickness=0)
canvas.create_polygon(0, 0, 1, 1, 2, 2, fill='SeaGreen3', tags='poly')
canvas.create_line(0, 0, 1, 1, 2, 2, 0, 0, fill='black', tags='line')
globals().update(locals())
scale = Scale(frame, orient='vertical', length=284, from_=0, to_=250,
              command=lambda height: setHeight(canvas, int(height)),
              tickinterval=50)
scale.pack(side=LEFT, anchor='ne')
canvas.pack(side=LEFT, anchor='nw', fill=Y)
scale.set(75)
