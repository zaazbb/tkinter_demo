# radio.tcl --
#
# This demonstration script creates a toplevel window containing
# several radiobutton widgets.

##if {![info exists widgetDemo]} {
##    error "This script should be run from the \"widget\" demo."
##}
assert 'widgetDemo' in globals(), \
'This script should be run from the "widget" demo.'

##package require Tk
from tkinter import *

##set w .radio
##catch {destroy $w}
##toplevel $w
##wm title $w "Radiobutton Demonstration"
##wm iconname $w "radio"
##positionWindow $w
demo_name = 'radio'
if demo_name in globals()['demo_name']:
    globals()['demo_name'][demo_name].destroy()
w = globals()['demo_name'][demo_name] = Toplevel(root)
w.wm_title('Radiobutton Demonstration')
w.wm_iconname('radio')
positionWindow(w)

##label $w.msg -font $font -wraplength 5i -justify left -text "Three groups of radiobuttons are displayed below.  If you click on a button then the button will become selected exclusively among all the buttons in its group.  A Tcl variable is associated with each group to indicate which of the group's buttons is selected.  When the 'Tristate' button is pressed, the radio buttons will display the tri-state mode. Selecting any radio button will return the buttons to their respective on/off state. Click the \"See Variables\" button to see the current values of the variables."
##grid $w.msg -row 0 -column 0 -columnspan 3 -sticky nsew
msg = Label(w, font=font_, wraplength='5i', justify='left', text="Three groups of radiobuttons are displayed below.  If you click on a button then the button will become selected exclusively among all the buttons in its group.  A Tcl variable is associated with each group to indicate which of the group's buttons is selected.  When the 'Tristate' button is pressed, the radio buttons will display the tri-state mode. Selecting any radio button will return the buttons to their respective on/off state. Click the \"See Variables\" button to see the current values of the variables.")
msg.grid(row=0, column=0, columnspan=3, sticky='nsew')

## See Code / Dismiss buttons
##set btns [addSeeDismiss $w.buttons $w [list size color align]]
##grid $btns -row 3 -column 0 -columnspan 3 -sticky ew
size = StringVar(name='size')
color = StringVar(name='color')
align = StringVar(name='align')
btns = addSeeDismiss(ttk.Frame(w), demo_name, [size, color, align])
btns.grid(row=3, column=0, columnspan=3, sticky='ew')

##labelframe $w.left -pady 2 -text "Point Size" -padx 2
##labelframe $w.mid -pady 2 -text "Color" -padx 2
##labelframe $w.right -pady 2 -text "Alignment" -padx 2
##button $w.tristate -text Tristate -command "set size multi; set color multi" \
##    -pady 2 -padx 2
##if {[tk windowingsystem] eq "aqua"} {
##    $w.tristate configure -padx 10
##}
##grid $w.left     -column 0 -row 1 -pady .5c -padx .5c -rowspan 2
##grid $w.mid      -column 1 -row 1 -pady .5c -padx .5c -rowspan 2
##grid $w.right    -column 2 -row 1 -pady .5c -padx .5c
##grid $w.tristate -column 2 -row 2 -pady .5c -padx .5c
def tristate_callback(size=size, color=color):
    size.set('multi')
    color.set('multi')
left = LabelFrame(w, pady=2, text='Point Size', padx=2)
mid = LabelFrame(w, pady=2, text='Color', padx=2)
right = LabelFrame(w, pady=2, text='Alignment', padx=2)
tristate = Button(w, text='Tristate', pady=2, padx=2,
                  command=tristate_callback)
if root._windowingsystem == 'aque': pass
left.grid(column=0, row=1, pady='.5c', padx='.5c', rowspan=2)
mid.grid(column=1, row=1, pady='.5c', padx='.5c', rowspan=2)
right.grid(column=2, row=1, pady='.5c', padx='.5c')
tristate.grid(column=2, row=2, pady='.5c', padx='.5c')

##foreach i {10 12 14 18 24} {
##    radiobutton $w.left.b$i -text "Point Size $i" -variable size \
##	    -relief flat -value $i -tristatevalue "multi"
##    pack $w.left.b$i  -side top -pady 2 -anchor w -fill x
##}
for i in [10,12,14,18,24]:
    b = Radiobutton(left, text='Point Size %i'%i, variable=size, relief='flat',
                    value=i, tristatevalue='multi')
    b.pack(side='top', pady=2, anchor='w', fill='x')

##foreach c {Red Green Blue Yellow Orange Purple} {
##    set lower [string tolower $c]
##    radiobutton $w.mid.$lower -text $c -variable color \
##	    -relief flat -value $lower -anchor w \
##	    -command "$w.mid configure -fg \$color" \
##	-tristatevalue "multi"
##    pack $w.mid.$lower -side top -pady 2 -fill x
##}
globals().update(locals())
for c in ['Red', 'Green', 'Blue', 'Yellow', 'Orange', 'Purple']:
    lower = Radiobutton(mid, text=c, variable=color, relief='flat',
        value=c.lower(), anchor='w', tristatevalue='multi',
        command=lambda: mid.config(fg=color.get()))
    lower.pack(side='top', pady=2, fill='x')

##label $w.right.l -text "Label" -bitmap questhead -compound left
##$w.right.l configure -width [winfo reqwidth $w.right.l] -compound top
##$w.right.l configure -height [winfo reqheight $w.right.l]
##foreach a {Top Left Right Bottom} {
##    set lower [string tolower $a]
##    radiobutton $w.right.$lower -text $a -variable align \
##	    -relief flat -value $lower -indicatoron 0 -width 7 \
##	    -command "$w.right.l configure -compound \$align"
##}
l = Label(right, text='Label', bitmap='questhead', compound='left')
l['width'] = l.winfo_reqwidth()
l['compound'] = 'top'
l['height'] = l.winfo_reqheight()
right_radio = {}
globals().update(locals())
for a in ['Top', 'Left', 'Right', 'Bottom']:
    right_radio[a.lower()] = Radiobutton(right, text=a, variable=align,
        relief='flat', value=a.lower(), indicatoron=0, width=7,
        command=lambda: l.config(compound=align.get()))

##grid x $w.right.top
##grid $w.right.left $w.right.l $w.right.right
##grid x $w.right.bottom
right_radio['top'].grid(column=1, row=0)
right_radio['left'].grid(column=0, row=1)
l.grid(column=1, row=1)
right_radio['right'].grid(column=2, row=1) 
right_radio['bottom'].grid(column=1, row=2)
