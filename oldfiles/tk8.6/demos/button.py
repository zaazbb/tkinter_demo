# button.tcl --
#
# This demonstration script creates a toplevel window containing
# several button widgets.

##if {![info exists widgetDemo]} {
##    error "This script should be run from the \"widget\" demo."
##}
assert 'widgetDemo' in globals(), \
'This script should be run from the "widget" demo.'

##package require Tk
from tkinter import *

##set w .button
##catch {destroy $w}
##toplevel $w
##wm title $w "Button Demonstration"
##wm iconname $w "button"
##positionWindow $w
demo_name = 'button'
if demo_name in globals()['demo_name']:
    globals()['demo_name'][demo_name].destroy()
w = globals()['demo_name'][demo_name] = Toplevel(root)
w.wm_title('Button Demonstration')
w.wm_iconname('button')
positionWindow(w)

##label $w.msg -font $font -wraplength 4i -justify left -text "If you click on any of the four buttons below, the background of the button area will change to the color indicated in the button.  You can press Tab to move among the buttons, then press Space to invoke the current button."
##pack $w.msg -side top
msg = Label(w, font=font_, wraplength='4i', justify='left', text="If you click on any of the four buttons below, the background of the button area will change to the color indicated in the button.  You can press Tab to move among the buttons, then press Space to invoke the current button.")
msg.pack(side='top')

## See Code / Dismiss buttons
##pack [addSeeDismiss $w.buttons $w] -side bottom -fill x
addSeeDismiss(ttk.Frame(w), demo_name).pack(side='bottom', fill='x')

##proc colorrefresh {w col} {
##    $w configure -bg $col
##    if {[tk windowingsystem] eq "aqua"} {
##	# set highlightbackground of all buttons in $w
##	set l [list $w]
##	while {[llength $l]} {
##	    set l [concat [lassign $l b] [winfo children $b]]
##	    if {[winfo class $b] eq "Button"} {
##		$b configure -highlightbackground $col
##	    }
##	}
##    }
##}

def colorrefresh(w, col):
    w['bg'] = col
    if w._windowingsystem == 'aqua':
        pass

##button $w.b1 -text "Peach Puff" -width 10 \
##    -command [list colorrefresh $w PeachPuff1]
##button $w.b2 -text "Light Blue" -width 10 \
##    -command [list colorrefresh $w LightBlue1]
##button $w.b3 -text "Sea Green" -width 10 \
##    -command [list colorrefresh $w SeaGreen2]
##button $w.b4 -text "Yellow" -width 10 \
##    -command [list colorrefresh $w Yellow1]
##pack $w.b1 $w.b2 $w.b3 $w.b4 -side top -expand yes -pady 2
globals().update(locals())
b1 = Button(w, text='Peach Puff', width=10,
            command=lambda: colorrefresh(w, 'PeachPuff1'))
b2 = Button(w, text='Light Blue', width=10,
            command=lambda: colorrefresh(w, 'LightBlue1'))
b3 = Button(w, text='Sea Green', width=10,
            command=lambda: colorrefresh(w, 'SeaGreen2'))
b4 = Button(w, text='Yellow', width=10,
            command=lambda: colorrefresh(w, 'Yellow1'))
for b in [b1, b2, b3, b4]: b.pack(side='top', expand='yes', pady=2)

