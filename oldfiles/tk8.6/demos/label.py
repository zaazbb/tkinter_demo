# label.tcl --
#
# This demonstration script creates a toplevel window containing
# several label widgets.

##if {![info exists widgetDemo]} {
##    error "This script should be run from the \"widget\" demo."
##}
assert 'widgetDemo' in globals(), \
'This script should be run from the "widget" demo.'

##package require Tk
from tkinter import *

##set w .label
##catch {destroy $w}
##toplevel $w
##wm title $w "Label Demonstration"
##wm iconname $w "label"
##positionWindow $w
demo_name = 'label'
if demo_name in globals()['demo_name']:
    globals()['demo_name'][demo_name].destroy()
w = globals()['demo_name'][demo_name] = Toplevel(root)
w.wm_title('Label Demonstration')
w.wm_iconname('label')
positionWindow(w)

##label $w.msg -font $font -wraplength 4i -justify left -text "Five labels are displayed below: three textual ones on the left, and an image label and a text label on the right.  Labels are pretty boring because you can't do anything with them."
##pack $w.msg -side top
msg = Label(w, font=font_, wraplength='4i', justify='left', text="Five labels are displayed below: three textual ones on the left, and an image label and a text label on the right.  Labels are pretty boring because you can't do anything with them.")
msg.pack(side='top')

## See Code / Dismiss buttons
##set btns [addSeeDismiss $w.buttons $w]
##pack $btns -side bottom -fill x
addSeeDismiss(ttk.Frame(w), demo_name).pack(side='bottom', fill='x')

##frame $w.left
##frame $w.right
##pack $w.left $w.right -side left -expand yes -padx 10 -pady 10 -fill both
left = Frame(w)
right = Frame(w)
left.pack(side='left', expand='yes', padx=10, pady=10, fill='both')
right.pack(side='left', expand='yes', padx=10, pady=10, fill='both')

##label $w.left.l1 -text "First label"
##label $w.left.l2 -text "Second label, raised" -relief raised
##label $w.left.l3 -text "Third label, sunken" -relief sunken
##pack $w.left.l1 $w.left.l2 $w.left.l3 -side top -expand yes -pady 2 -anchor w
l1 = Label(left, text='First label')
l2 = Label(left, text='Second label, raised', relief='raised')
l3 = Label(left, text='Third label, sunken', relief='sunken')
for l in [l1, l2, l3]: l.pack(side='top', expand='yes', pady=2, anchor='w')

# Main widget program sets variable tk_demoDirectory
##image create photo label.ousterhout \
##    -file [file join $tk_demoDirectory images ouster.png]
##label $w.right.picture -borderwidth 2 -relief sunken -image label.ousterhout
##label $w.right.caption -text "Tcl/Tk Creator"
##pack $w.right.picture $w.right.caption -side top
import os.path
ousterhout = PhotoImage(file=os.path.join(tk_demoDirectory,
                                          'images', 'ouster.png'))
picture = Label(right, borderwidth=2, relief='sunken', image=ousterhout)
# keep a reference,
# to prevent image object be garbage-collected by Python.
picture.image = ousterhout 
caption = Label(right, text='Tcl/Tk Creator')
picture.pack(side='top')
caption.pack(side='top')


