# fontchoose.tcl --
#
# Show off the stock font selector dialog

##if {![info exists widgetDemo]} {
##    error "This script should be run from the \"widget\" demo."
##}
assert 'widgetDemo' in globals(), \
'This script should be run from the "widget" demo.'

##package require Tk

##set w .fontchoose
##catch {destroy $w}
##toplevel $w
##wm title $w "Font Selection Dialog"
##wm iconname $w "fontchooser"
##positionWindow $w
demo_name = 'fontchoose'
if demo_name in globals()['demo_name']:
    globals()['demo_name'][demo_name].destroy()
w = globals()['demo_name'][demo_name] = Toplevel(root)
w.wm_title('Font Selection Dialog')
w.wm_iconname('fontchoose')
positionWindow(w)

##catch {font create FontchooseDemoFont {*}[font actual TkDefaultFont]}
try:
    FontchooseDemoFont = Font()
except:
    pass

# The font chooser needs to be configured and then shown.
##proc SelectFont {parent} {
##    tk fontchooser configure -font FontchooseDemoFont \
##        -command ApplyFont -parent $parent
##    tk fontchooser show
##}
def SelectFont(parent):
    pass

##proc ApplyFont {font} {
##    font configure FontchooseDemoFont {*}[font actual $font]
##}
def ApplyFont(font):
    pass

# When the visibility of the fontchooser changes, the following event is fired
# to the parent widget.
#
##bind $w <<TkFontchooserVisibility>> {
##    if {[tk fontchooser configure -visible]} {
##        %W.f.font state disabled
##    } else {
##        %W.f.font state !disabled
##    }
##}
def fontChooserVisibilityEvent(e):
    pass

##set f [ttk::frame $w.f -relief sunken -padding 2]
##
##text $f.msg -font FontchooseDemoFont -width 40 -height 6 -borderwidth 0 \
##    -yscrollcommand [list $f.vs set]
##ttk::scrollbar $f.vs -command [list $f.msg yview]
##
##$f.msg insert end "Press the buttons below to choose a new font for the\
##  text shown in this window.\n" {}
##
##ttk::button $f.font -text "Set font ..." -command [list SelectFont $w]
##
##grid $f.msg $f.vs -sticky news
##grid $f.font -    -sticky e
##grid columnconfigure $f 0 -weight 1
##grid rowconfigure $f 0 -weight 1
##bind $w <Visibility> {
##    bind %W <Visibility> {}
##    grid propagate %W.f 0    
##}
f = ttk.Frame(w, relief=SUNKEN, padding=2)
msg = Text(f, font=FontchooseDemoFont, width=40, height=6, borderwidth=0)
vs = ttk.Scrollbar(f, command=msg.yview)
msg['yscrollcommand'] = vs.set
msg.insert(END,
           'Press the buttons below to choose a new font for the'
           ' text shown in this window.\n', '')
font = ttk.Button(f, text='Set font ...', command=lambda: SelectFont(w))
msg.grid(sticky='news')
vs.grid(sticky='news', row=0, column=1)
font.grid(sticky=E, columnspan=2)
f.grid_columnconfigure(0, weight=1)
f.rowconfigure(0, weight=1)
def wVisibilityEvent(e):
    w.bind('<Visibility>', '')
    f.grid_propagate(0)
w.bind('<Visibility>', wVisibilityEvent)

## See Code / Dismiss buttons
##set btns [addSeeDismiss $w.buttons $w]
btns = addSeeDismiss(ttk.Frame(w), demo_name)

##grid $f -sticky news
##grid $btns -sticky ew
##grid columnconfigure $w 0 -weight 1
##grid rowconfigure $w 0 -weight 1
f.grid(sticky='news')
btns.grid(sticky='ew')
w.grid_columnconfigure(0, weight=1)
w.grid_rowconfigure(0, weight=1)
