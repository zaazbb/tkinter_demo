# labelframe.tcl --
#
# This demonstration script creates a toplevel window containing
# several labelframe widgets.

##if {![info exists widgetDemo]} {
##    error "This script should be run from the \"widget\" demo."
##}
assert 'widgetDemo' in globals(), \
'This script should be run from the "widget" demo.'

##package require Tk
from tkinter import *

##set w .labelframe
##catch {destroy $w}
##toplevel $w
##wm title $w "Labelframe Demonstration"
##wm iconname $w "labelframe"
##positionWindow $w
demo_name = 'labelframe'
if demo_name in globals()['demo_name']:
    globals()['demo_name'][demo_name].destroy()
w = globals()['demo_name'][demo_name] = Toplevel(root)
w.wm_title('Labelframe Demonstration')
w.wm_iconname('labelframe')
positionWindow(w)

# Some information

##label $w.msg -font $font -wraplength 4i -justify left -text "Labelframes are\
##	used to group related widgets together.  The label may be either \
##	plain text or another widget."
##pack $w.msg -side top
msg = Label(w, font=font_, wraplength='4i', justify='left', text="Labelframes are\
 used to group related widgets together.  The label may be either \
 plain text or another widget.")
msg.pack(side='top')

## See Code / Dismiss buttons
##set btns [addSeeDismiss $w.buttons $w]
##pack $btns -side bottom -fill x
btns = addSeeDismiss(w, demo_name)
btns.pack(side='bottom', fill='x')

# Demo area

##frame $w.f
##pack $w.f -side bottom -fill both -expand 1
##set w $w.f
f = Frame(w)
f.pack(side='bottom', fill='both', expand=1)
w = f

# A group of radiobuttons in a labelframe

##labelframe $w.f -text "Value" -padx 2 -pady 2
##grid $w.f -row 0 -column 0 -pady 2m -padx 2m
f = LabelFrame(w, text='Value', padx=2, pady=2)
f.grid(row=0, column=0, pady='2m', padx='2m')

##foreach value {1 2 3 4} {
##    radiobutton $w.f.b$value -text "This is value $value" \
##            -variable lfdummy -value $value
##    pack $w.f.b$value -side top -fill x -pady 2
##}
b = [0]*4
lfdummy = IntVar()
for value in range(4):
    b[value] = Radiobutton(f, text='This is value %i'%(value+1),
                           variable=lfdummy, value=value+1)
    b[value].pack(side='top', fill='x', pady=2)

# Using a label window to control a group of options.

##proc lfEnableButtons {w} {
##    foreach child [winfo children $w] {
##        if {$child == "$w.cb"} continue
##        if {$::lfdummy2} {
##            $child configure -state normal
##        } else {
##            $child configure -state disabled
##        }
##    }
##}
def lfEnableButtons(w, cb):
    for child in w.winfo_children():
        if child == cb: continue
        if lfdummy2.get(): child['state'] = 'normal'
        else: child['state'] = 'disabled'

##labelframe $w.f2 -pady 2 -padx 2
##checkbutton $w.f2.cb -text "Use this option." -variable lfdummy2 \
##        -command "lfEnableButtons $w.f2" -padx 0
##$w.f2 configure -labelwidget $w.f2.cb
##grid $w.f2 -row 0 -column 1 -pady 2m -padx 2m
f2 = LabelFrame(w, pady=2, padx=2)
lfdummy2 = IntVar()
cb = Checkbutton(f2, text='Use this option.', variable=lfdummy2, padx=0)
f2['labelwidget'] = cb
f2.grid(row=0, column=1, pady='2m', padx='2m')
globals().update(locals())
cb['command'] = command=lambda: lfEnableButtons(f2, cb)

##set t 0
##foreach str {Option1 Option2 Option3} {
##    checkbutton $w.f2.b$t -text $str
##    pack $w.f2.b$t -side top -fill x -pady 2
##    incr t
##}
##lfEnableButtons $w.f2
b1 = [0]*3
for t, str_ in enumerate(['Option1', 'Option2', 'Option3']):
    b1[t] = Checkbutton(f2, text=str_)
    b1[t].pack(side='top', fill='x', pady=2)

##grid columnconfigure $w {0 1} -weight 1
w.grid_columnconfigure('0 1', weight=1)
