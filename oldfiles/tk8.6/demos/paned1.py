# paned1.tcl --
#
# This demonstration script creates a toplevel window containing
# a paned window that separates two windows horizontally.

##if {![info exists widgetDemo]} {
##    error "This script should be run from the \"widget\" demo."
##}
assert 'widgetDemo' in globals(), \
'This script should be run from the "widget" demo.'

##package require Tk

##set w .paned1
##catch {destroy $w}
##toplevel $w
##wm title $w "Horizontal Paned Window Demonstration"
##wm iconname $w "paned1"
##positionWindow $w
demo_name = 'paned1'
if demo_name in globals()['demo_name']:
    globals()['demo_name'][demo_name].destroy()
w = globals()['demo_name'][demo_name] = Toplevel(root)
w.wm_title('Horizontal Paned Window Demonstration')
w.wm_iconname('paned1')
positionWindow(w)

##label $w.msg -font $font -wraplength 4i -justify left -text "The sash between the two coloured windows below can be used to divide the area between them.  Use the left mouse button to resize without redrawing by just moving the sash, and use the middle mouse button to resize opaquely (always redrawing the windows in each position.)"
##pack $w.msg -side top
msg = Label(w, font=font, wraplength='4i', justify=LEFT, text="The sash between the two coloured windows below can be used to divide the area between them.  Use the left mouse button to resize without redrawing by just moving the sash, and use the middle mouse button to resize opaquely (always redrawing the windows in each position.)")
msg.pack(side=TOP)

## See Code / Dismiss buttons
##set btns [addSeeDismiss $w.buttons $w]
##pack $btns -side bottom -fill x
btns = addSeeDismiss(ttk.Frame(w), demo_name)
btns.pack(side=BOTTOM, fill=X)

##panedwindow $w.pane
##pack $w.pane -side top -expand yes -fill both -pady 2 -padx 2m
##
##label $w.pane.left  -text "This is the\nleft side"  -bg yellow
##label $w.pane.right -text "This is the\nright side" -bg cyan
##
##$w.pane add $w.pane.left $w.pane.right
pane = PanedWindow(w)
pane.pack(side=TOP, expand=YES, fill=BOTH, pady=2, padx='2m')
left = Label(pane, text='This is the\nleft side', bg='yellow')
right = Label(pane, text='This is the\nright side', bg='cyan')
pane.add(left)
pane.add(right)
