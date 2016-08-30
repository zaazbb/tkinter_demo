# hscale.tcl --
#
# This demonstration script shows an example with a horizontal scale.

##if {![info exists widgetDemo]} {
##    error "This script should be run from the \"widget\" demo."
##}
assert 'widgetDemo' in globals(), \
'This script should be run from the "widget" demo.'

##package require Tk

##set w .hscale
##catch {destroy $w}
##toplevel $w
##wm title $w "Horizontal Scale Demonstration"
##wm iconname $w "hscale"
##positionWindow $w
demo_name = 'hscale'
if demo_name in globals()['demo_name']:
    globals()['demo_name'][demo_name].destroy()
w = globals()['demo_name'][demo_name] = Toplevel(root)
w.wm_title('Horizontal Scale Demonstration')
w.wm_iconname('hscale')
positionWindow(w)

##label $w.msg -font $font -wraplength 3.5i -justify left -text "An arrow and a horizontal scale are displayed below.  If you click or drag mouse button 1 in the scale, you can change the length of the arrow."
##pack $w.msg -side top -padx .5c
msg = Label(w, font=font, wraplength='3.5i', justify=LEFT, text="An arrow and a horizontal scale are displayed below.  If you click or drag mouse button 1 in the scale, you can change the length of the arrow.")
msg.pack(side=TOP, padx='.5c')

## See Code / Dismiss buttons
##set btns [addSeeDismiss $w.buttons $w]
##pack $btns -side bottom -fill x
btns = addSeeDismiss(ttk.Frame(w), demo_name)
btns.pack(side='bottom', fill='x')

##frame $w.frame -borderwidth 10
##pack $w.frame -side top -fill x
frame = Frame(w, borderwidth=10)
frame.pack(side=TOP, fill=X)

##canvas $w.frame.canvas -width 50 -height 50 -bd 0 -highlightthickness 0
##$w.frame.canvas create polygon 0 0 1 1 2 2 -fill DeepSkyBlue3 -tags poly
##$w.frame.canvas create line 0 0 1 1 2 2 0 0 -fill black -tags line
##scale $w.frame.scale -orient horizontal -length 284 -from 0 -to 250 \
##	-command "setWidth $w.frame.canvas" -tickinterval 50
##pack $w.frame.canvas -side top -expand yes -anchor s -fill x  -padx 15
##pack $w.frame.scale -side bottom -expand yes -anchor n
##$w.frame.scale set 75
def setWidth(w, width):
    width += 21
    x2 = width - 30
    if x2 < 21:
        x2 = 21
    w.coords('poly',
             20, 15, 20, 35, x2, 35, x2, 45, width, 25, x2, 5, x2, 15, 20, 15)
    w.coords('line',
             20, 15, 20, 35, x2, 35, x2, 45, width, 25, x2, 5, x2, 15, 20, 15)
canvas = Canvas(frame, width=50, height=50, bd=0, highlightthickness=0)
canvas.create_polygon(0, 0, 1, 1, 2, 2, fill='DeepSkyBlue3', tags='poly')
canvas.create_line(0, 0, 1, 1, 2, 2, 0, 0, fill='black', tags='line')
globals().update(locals())
scale = Scale(frame, orient='horizontal', length=284, from_=0, to_=250,
              command=lambda width: setWidth(canvas, int(width)),
              tickinterval=50)
canvas.pack(side=TOP, expand='yes', anchor=S, fill=X, padx=15)
scale.pack(side=BOTTOM, expand=YES, anchor=N)
scale.set(75)

##proc setWidth {w width} {
##    incr width 21
##    set x2 [expr {$width - 30}]
##    if {$x2 < 21} {
##	set x2 21
##    }
##    $w coords poly 20 15 20 35 $x2 35 $x2 45 $width 25 $x2 5 $x2 15 20 15
##    $w coords line 20 15 20 35 $x2 35 $x2 45 $width 25 $x2 5 $x2 15 20 15
##}
