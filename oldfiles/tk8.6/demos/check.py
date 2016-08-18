# check.tcl --
#
# This demonstration script creates a toplevel window containing
# several checkbuttons.

##if {![info exists widgetDemo]} {
##    error "This script should be run from the \"widget\" demo."
##}
assert 'widgetDemo' in globals(), \
'This script should be run from the "widget" demo.'

##package require Tk
from tkinter import *

##set w .check
##catch {destroy $w}
##toplevel $w
##wm title $w "Checkbutton Demonstration"
##wm iconname $w "check"
##positionWindow $w
demo_name = 'check'
if demo_name in globals()['demo_name']:
    globals()['demo_name'][demo_name].destroy()
w = globals()['demo_name'][demo_name] = Toplevel(root)
w.wm_title('Checkbutton Demonstration')
w.wm_iconname('check')
positionWindow(w)

##label $w.msg -font $font -wraplength 4i -justify left -text "Four checkbuttons are displayed below.  If you click on a button, it will toggle the button's selection state and set a Tcl variable to a value indicating the state of the checkbutton.  The first button also follows the state of the other three.  If only some of the three are checked, the first button will display the tri-state mode. Click the \"See Variables\" button to see the current values of the variables."
##pack $w.msg -side top
msg = Label(w, font=font_, wraplength='4i', justify='left', text="Four checkbuttons are displayed below.  If you click on a button, it will toggle the button's selection state and set a Tcl variable to a value indicating the state of the checkbutton.  The first button also follows the state of the other three.  If only some of the three are checked, the first button will display the tri-state mode. Click the \"See Variables\" button to see the current values of the variables.")
msg.pack(side='top')

## See Code / Dismiss buttons
##set btns [addSeeDismiss $w.buttons $w [list safety wipers brakes sober]]
##pack $btns -side bottom -fill x
safety = StringVar(name='safety')
wipers = BooleanVar(name='wipers')
brakes = BooleanVar(name='brakes')
sober = BooleanVar(name='sober')
btns = addSeeDismiss(ttk.Frame(w), demo_name, [safety, wipers, brakes, sober])
btns.pack(side='bottom', fill='x')

##checkbutton $w.b0 -text "Safety Check" -variable safety -relief flat \
##    -onvalue "all" \
##    -offvalue "none" \
##    -tristatevalue "partial"
##checkbutton $w.b1 -text "Wipers OK" -variable wipers -relief flat
##checkbutton $w.b2 -text "Brakes OK" -variable brakes -relief flat
##checkbutton $w.b3 -text "Driver Sober" -variable sober -relief flat
##pack $w.b0 -side top -pady 2 -anchor w
##pack $w.b1 $w.b2 $w.b3 -side top -pady 2 -anchor w -padx 15
b0 = Checkbutton(w, text='Safety Check', variable=safety, relief='flat',
                 onvalue='all', offvalue='none', tristatevalue='partial')
b1 = Checkbutton(w, text='Wipers OK', variable=wipers, relief='flat')
b2 = Checkbutton(w, text='Brakes OK', variable=brakes, relief='flat')
b3 = Checkbutton(w, text='Driver Sober', variable=sober, relief='flat')
b0.pack(side='top', pady=2, anchor='w')
for b in [b1,b2,b3] : b.pack(side='top', pady=2, anchor='w', padx=15)

## This code makes $w.b0 function as a tri-state button; it's not
## needed at all for just straight yes/no buttons.

##set in_check 0
##proc tristate_check {n1 n2 op} {
##    global safety wipers brakes sober in_check
##    if {$in_check} {
##	return
##    }
##    set in_check 1
##    if {$n1 eq "safety"} {
##	if {$safety eq "none"} {
##	    set wipers 0
##	    set brakes 0
##	    set sober 0
##	} elseif {$safety eq "all"} {
##	    set wipers 1
##	    set brakes 1
##	    set sober 1
##	}
##    } else {
##	if {$wipers == 1 && $brakes == 1 && $sober == 1} {
##	    set safety all
##	} elseif {$wipers == 1 || $brakes == 1 || $sober == 1} {
##	    set safety partial
##	} else {
##	    set safety none
##	}
##    }
##    set in_check 0
##}
in_check = 0
def tristate_check(n1, n2, op, vars_=locals()):
    if vars_['in_check']:
        return
    vars_['in_check'] = 1
    safety = vars_['safety']
    wipers = vars_['wipers']
    brakes = vars_['brakes']
    sober = vars_['sober']
    if n1 == safety._name:
        if safety.get() == 'none':
            wipers.set(False)
            brakes.set(False)
            sober.set(False)
        elif safety.get() == 'all':
            wipers.set(True)
            brakes.set(True)
            sober.set(True)
    else:
        if wipers.get() and brakes.get() and sober.get():
            safety.set('all')
        elif wipers.get() or brakes.get() or sober.get():
            safety.set('partial')
        else:
            safety.set('none')
    vars_['in_check'] = 0 

##trace variable wipers w tristate_check
##trace variable brakes w tristate_check
##trace variable sober  w tristate_check
##trace variable safety w tristate_check
wipers.trace_variable('w', tristate_check)
brakes.trace_variable('w', tristate_check)
sober.trace_variable('w', tristate_check)
safety.trace_variable('w', tristate_check)
