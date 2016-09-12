# bind.tcl --
#
# This demonstration script creates a text widget with bindings set
# up for hypertext-like effects.

##if {![info exists widgetDemo]} {
##    error "This script should be run from the \"widget\" demo."
##}
assert 'widgetDemo' in globals(), \
'This script should be run from the "widget" demo.'

##package require Tk
from tkinter import *

##set w .bind
##catch {destroy $w}
##toplevel $w
##wm title $w "Text Demonstration - Tag Bindings"
##wm iconname $w "bind"
##positionWindow $w
demo_name = 'bind'
if demo_name in globals()['demo_name']:
    globals()['demo_name'][demo_name].destroy()
w = globals()['demo_name'][demo_name] = Toplevel(root)
w.wm_title('Text Demonstration - Tag Bindings')
w.wm_iconname('bind')
positionWindow(w)

## See Code / Dismiss buttons
##set btns [addSeeDismiss $w.buttons $w]
##pack $btns -side bottom -fill x
btns = addSeeDismiss(ttk.Frame(w), demo_name)
btns.pack(side='bottom', fill='x')

##text $w.text -yscrollcommand "$w.scroll set" -setgrid true \
##	-width 60 -height 24 -font $font -wrap word
##scrollbar $w.scroll -command "$w.text yview"
##pack $w.scroll -side right -fill y
##pack $w.text -expand yes -fill both
text = Text(w, setgrid=True, width=60, height=24, font=font_, wrap='word')
scroll = Scrollbar(w, command=text.yview)
text['yscrollcommand'] = scroll.set
scroll.pack(side='right', fill='y')
text.pack(expand='yes', fill='both')

# Set up display styles.

##if {[winfo depth $w] > 1} {
##    set bold "-background #43ce80 -relief raised -borderwidth 1"
##    set normal "-background {} -relief flat"
##} else {
##    set bold "-foreground white -background black"
##    set normal "-foreground {} -background {}"
##}
if w.winfo_depth() > 1:
    bold = dict(background='#43ce80', relief='raised', borderwidth=1)
    normal = dict(background='', relief='flat')
else:
    bold = dict(foreground='white', background='black')
    normal = dict(foreground='', background='')

# Add text to widget.

##$w.text insert 0.0 {\
##The same tag mechanism that controls display styles in text widgets can also be used to associate Tcl commands with regions of text, so that mouse or keyboard actions on the text cause particular Tcl commands to be invoked.  For example, in the text below the descriptions of the canvas demonstrations have been tagged.  When you move the mouse over a demo description the description lights up, and when you press button 1 over a description then that particular demonstration is invoked.
##
##}
##$w.text insert end \
##{1. Samples of all the different types of items that can be created in canvas widgets.} d1
##$w.text insert end \n\n
##$w.text insert end \
##{2. A simple two-dimensional plot that allows you to adjust the positions of the data points.} d2
##$w.text insert end \n\n
##$w.text insert end \
##{3. Anchoring and justification modes for text items.} d3
##$w.text insert end \n\n
##$w.text insert end \
##{4. An editor for arrow-head shapes for line items.} d4
##$w.text insert end \n\n
##$w.text insert end \
##{5. A ruler with facilities for editing tab stops.} d5
##$w.text insert end \n\n
##$w.text insert end \
##{6. A grid that demonstrates how canvases can be scrolled.} d6
text.insert('0.0',
"""The same tag mechanism that controls display styles in text widgets can also be used to associate Tcl commands with regions of text, so that mouse or keyboard actions on the text cause particular Tcl commands to be invoked.  For example, in the text below the descriptions of the canvas demonstrations have been tagged.  When you move the mouse over a demo description the description lights up, and when you press button 1 over a description then that particular demonstration is invoked.

""")
text.insert('end', 
'1. Samples of all the different types of items that can be created in canvas widgets.', 'd1')
text.insert('end', '\n\n')
text.insert('end', 
'2. A simple two-dimensional plot that allows you to adjust the positions of the data points.', 'd2')
text.insert('end', '\n\n')
text.insert('end',
'3. Anchoring and justification modes for text items.', 'd3')
text.insert('end', '\n\n')
text.insert('end',
'4. An editor for arrow-head shapes for line items.', 'd4')
text.insert('end', '\n\n')
text.insert('end',
'5. A ruler with facilities for editing tab stops.', 'd5')
text.insert('end', '\n\n')
text.insert('end',
'6. A grid that demonstrates how canvases can be scrolled.', 'd6')

# Create bindings for tags.

##foreach tag {d1 d2 d3 d4 d5 d6} {
##    $w.text tag bind $tag <Any-Enter> "$w.text tag configure $tag $bold"
##    $w.text tag bind $tag <Any-Leave> "$w.text tag configure $tag $normal"
##}
### Main widget program sets variable tk_demoDirectory
##$w.text tag bind d1 <1> {source [file join $tk_demoDirectory items.tcl]}
##$w.text tag bind d2 <1> {source [file join $tk_demoDirectory plot.tcl]}
##$w.text tag bind d3 <1> {source [file join $tk_demoDirectory ctext.tcl]}
##$w.text tag bind d4 <1> {source [file join $tk_demoDirectory arrow.tcl]}
##$w.text tag bind d5 <1> {source [file join $tk_demoDirectory ruler.tcl]}
##$w.text tag bind d6 <1> {source [file join $tk_demoDirectory cscroll.tcl]}
for tag in ('d1', 'd2', 'd3', 'd4', 'd5', 'd6'):
    text.tag_bind(tag, '<Any-Enter>',
                  lambda e, w=text, t=tag, cnf=bold: w.tag_configure(t, **cnf))
    text.tag_bind(tag, '<Any-Leave>',
                  lambda e, w=text, t=tag, cnf=normal: w.tag_configure(t, **cnf))
# Main widget program sets variable tk_demoDirectory
def run_demo(demo):
    global tk_demoDirectory
    demo_file = '%s/%s.py' % (tk_demoDirectory, demo)
    global_dict = {'widgetDemo':widgetDemo,
                   'tk_demoDirectory':tk_demoDirectory,
                   'root':root,
                   'font_':font_,
                   'positionWindow':positionWindow,
                   'addSeeDismiss':addSeeDismiss,
                   'demo_name':demo_name}
    exec(compile(open(demo_file).read(), demo_file, 'exec'), global_dict, {})
text.tag_bind('d1', '<1>', lambda e, f=run_demo: f('items'))
text.tag_bind('d2', '<1>', lambda e, f=run_demo: f('plot'))
text.tag_bind('d3', '<1>', lambda e, f=run_demo: f('ctext'))
text.tag_bind('d4', '<1>', lambda e, f=run_demo: f('arrow'))
text.tag_bind('d5', '<1>', lambda e, f=run_demo: f('ruler'))
text.tag_bind('d6', '<1>', lambda e, f=run_demo: f('cscroll'))

##$w.text mark set insert 0.0
##$w.text configure -state disabled
text.mark_set('insert', '0.0')
text['state'] = 'disabled'
