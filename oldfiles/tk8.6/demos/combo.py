# combo.tcl --
#
# This demonstration script creates several combobox widgets.

##if {![info exists widgetDemo]} {
##    error "This script should be run from the \"widget\" demo."
##}
assert 'widgetDemo' in globals(), \
'This script should be run from the "widget" demo.'

##package require Tk
from tkinter import *

##set w .combo
##catch {destroy $w}
##toplevel $w
##wm title $w "Combobox Demonstration"
##wm iconname $w "combo"
##positionWindow $w
demo_name = 'combo'
if demo_name in globals()['demo_name']:
    globals()['demo_name'][demo_name].destroy()
w = globals()['demo_name'][demo_name] = Toplevel(root)
w.wm_title('Combobox Demonstration')
w.wm_iconname('combo')
positionWindow(w)

##ttk::label $w.msg -font $font -wraplength 5i -justify left -text "Three different\
##	combo-boxes are displayed below. You can add characters to the first\
##	one by pointing, clicking and typing, just as with an entry; pressing\
##	Return will cause the current value to be added to the list that is\
##	selectable from the drop-down list, and you can choose other values\
##	by pressing the Down key, using the arrow keys to pick another one,\
##	and pressing Return again. The second combo-box is fixed to a\
##	particular value, and cannot be modified at all. The third one only\
##	allows you to select values from its drop-down list of Australian\
##	cities."
##pack $w.msg -side top -fill x
msg = ttk.Label(w, font=font_, wraplength='5i', justify='left', text="Three different\
 combo-boxes are displayed below. You can add characters to the first\
 one by pointing, clicking and typing, just as with an entry; pressing\
 Return will cause the current value to be added to the list that is\
 selectable from the drop-down list, and you can choose other values\
 by pressing the Down key, using the arrow keys to pick another one,\
 and pressing Return again. The second combo-box is fixed to a\
 particular value, and cannot be modified at all. The third one only\
 allows you to select values from its drop-down list of Australian\
 cities.")
msg.pack(side='top', fill='x')

## See Code / Dismiss buttons
##set btns [addSeeDismiss $w.buttons $w {firstValue secondValue ozCity}]
##pack $btns -side bottom -fill x
firstValue = StringVar(name='firstValue')
secondValue = StringVar(name='secondValue', value='unchangable')
ozCity = StringVar(name='ozCity', value='Sydney')
btns = addSeeDismiss(ttk.Frame(w), demo_name, [firstValue, secondValue, ozCity])
btns.pack(side='bottom', fill='x')

##ttk::frame $w.f
##pack $w.f -fill both -expand 1
##set w $w.f
f = ttk.Frame(w)
f.pack(fill='both', expand=1)
w = f

##set australianCities {
##    Canberra Sydney Melbourne Perth Adelaide Brisbane
##    Hobart Darwin "Alice Springs"
##}
##set secondValue unchangable
##set ozCity Sydney
australianCities = 'Canberra Sydney Melbourne Perth Adelaide\
 Brisbane Hobart Darwin "Alice Springs"'

##ttk::labelframe $w.c1 -text "Fully Editable"
##ttk::combobox $w.c1.c -textvariable firstValue
##ttk::labelframe $w.c2 -text Disabled
##ttk::combobox $w.c2.c -textvariable secondValue -state disabled
##ttk::labelframe $w.c3 -text "Defined List Only"
##ttk::combobox $w.c3.c -textvariable ozCity -state readonly \
##	-values $australianCities
##bind $w.c1.c <Return> {
##    if {[%W get] ni [%W cget -values]} {
##	%W configure -values [concat [%W cget -values] [list [%W get]]]
##    }
##}
c1 = ttk.LabelFrame(w, text='Fully Editable')
c1c = ttk.Combobox(c1, textvariable=firstValue)
c2 = ttk.LabelFrame(w, text='Disabled')
c2c = ttk.Combobox(c2, textvariable=secondValue, state='disabled')
c3 = ttk.LabelFrame(w, text='Defined List Only')
c3c = ttk.Combobox(c3, textvariable=ozCity, state='readonly', values=australianCities)
def onReturn(e):
    if e.widget.get() not in e.widget.cget('values'):
        e.widget['values']=' '.join(e.widget.cget('values'), e.widget.get())
c1c.bind('<Return>', onReturn)

##pack $w.c1 $w.c2 $w.c3 -side top -pady 5 -padx 10
##pack $w.c1.c -pady 5 -padx 10
##pack $w.c2.c -pady 5 -padx 10
##pack $w.c3.c -pady 5 -padx 10
for w in [c1, c2, c3]: w.pack(side='top', pady=5, padx=10)
for w in [c1c, c2c, c3c]: w.pack(pady=5, padx=10)
