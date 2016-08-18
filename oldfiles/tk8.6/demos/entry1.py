# entry1.tcl --
#
# This demonstration script creates several entry widgets without
# scrollbars.

##if {![info exists widgetDemo]} {
##    error "This script should be run from the \"widget\" demo."
##}
assert 'widgetDemo' in globals(), \
'This script should be run from the "widget" demo.'

##package require Tk
from tkinter import *

##set w .entry1
##catch {destroy $w}
##toplevel $w
##wm title $w "Entry Demonstration (no scrollbars)"
##wm iconname $w "entry1"
##positionWindow $w
demo_name = 'entry1'
if demo_name in globals()['demo_name']:
    globals()['demo_name'][demo_name].destroy()
w = globals()['demo_name'][demo_name] = Toplevel(root)
w.wm_title('Entry Demonstration (no scrollbars)')
w.wm_iconname('entry1')
positionWindow(w)

##label $w.msg -font $font -wraplength 5i -justify left -text "Three different entries are displayed below.  You can add characters by pointing, clicking and typing.  The normal Motif editing characters are supported, along with many Emacs bindings.  For example, Backspace and Control-h delete the character to the left of the insertion cursor and Delete and Control-d delete the chararacter to the right of the insertion cursor.  For entries that are too large to fit in the window all at once, you can scan through the entries by dragging with mouse button2 pressed."
##pack $w.msg -side top
msg = Label(w, font=font_, wraplength='5i', justify='left', text="Three different entries are displayed below.  You can add characters by pointing, clicking and typing.  The normal Motif editing characters are supported, along with many Emacs bindings.  For example, Backspace and Control-h delete the character to the left of the insertion cursor and Delete and Control-d delete the chararacter to the right of the insertion cursor.  For entries that are too large to fit in the window all at once, you can scan through the entries by dragging with mouse button2 pressed.")
msg.pack(side='top')

## See Code / Dismiss buttons
##set btns [addSeeDismiss $w.buttons $w]
##pack $btns -side bottom -fill x
btns = addSeeDismiss(ttk.Frame(w), demo_name)
btns.pack(side='bottom', fill='x')

##entry $w.e1
##entry $w.e2
##entry $w.e3
##pack $w.e1 $w.e2 $w.e3 -side top -pady 5 -padx 10 -fill x
e1 = Entry(w)
e2 = Entry(w)            
e3 = Entry(w)
for w in [e1, e2, e3]: w.pack(side='top', pady=5, padx=10, fill='x')

##$w.e1 insert 0 "Initial value"
##$w.e2 insert end "This entry contains a long value, much too long "
##$w.e2 insert end "to fit in the window at one time, so long in fact "
##$w.e2 insert end "that you'll have to scan or scroll to see the end."
e1.insert(0, "Initial value")
e2.insert('end', "This entry contains a long value, much too long ")
e2.insert('end', "to fit in the window at one time, so long in fact ")
e2.insert('end', "that you'll have to scan or scroll to see the end.")            
