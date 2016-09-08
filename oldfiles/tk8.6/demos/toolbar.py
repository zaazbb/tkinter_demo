# toolbar.tcl --
#
# This demonstration script creates a toolbar that can be torn off.

##if {![info exists widgetDemo]} {
##    error "This script should be run from the \"widget\" demo."
##}
assert 'widgetDemo' in globals(), \
'This script should be run from the "widget" demo.'

##package require Tk

##set w .toolbar
##destroy $w
##toplevel $w
##wm title $w "Toolbar Demonstration"
##wm iconname $w "toolbar"
##positionWindow $w
demo_name = 'toolbar'
if demo_name in globals()['demo_name']:
    globals()['demo_name'][demo_name].destroy()
w = globals()['demo_name'][demo_name] = Toplevel(root)
w.wm_title('Toolbar Demonstration')
w.wm_iconname('toolbar')
positionWindow(w)

##ttk::label $w.msg -wraplength 4i -text "This is a demonstration of how to do\
##	a toolbar that is styled correctly and which can be torn off. The\
##	buttons are configured to be \u201Ctoolbar style\u201D buttons by\
##	telling them that they are to use the Toolbutton style. At the left\
##	end of the toolbar is a simple marker that the cursor changes to a\
##	movement icon over; drag that away from the toolbar to tear off the\
##	whole toolbar into a separate toplevel widget. When the dragged-off\
##	toolbar is no longer needed, just close it like any normal toplevel\
##	and it will reattach to the window it was torn off from."
msg = ttk.Label(w, wraplength='4i', text="This is a demonstration of how to do\
 a toolbar that is styled correctly and which can be torn off. The\
 buttons are configured to be \u201Ctoolbar style\u201D buttons by\
 telling them that they are to use the Toolbutton style. At the left\
 end of the toolbar is a simple marker that the cursor changes to a\
 movement icon over; drag that away from the toolbar to tear off the\
 whole toolbar into a separate toplevel widget. When the dragged-off\
 toolbar is no longer needed, just close it like any normal toplevel\
 and it will reattach to the window it was torn off from.")

## Set up the toolbar hull
##set t [frame $w.toolbar]		;# Must be a frame!
##ttk::separator $w.sep
##ttk::frame $t.tearoff -cursor fleur
##ttk::separator $t.tearoff.to -orient vertical
##ttk::separator $t.tearoff.to2 -orient vertical
##pack $t.tearoff.to -fill y -expand 1 -padx 2 -side left
##pack $t.tearoff.to2 -fill y -expand 1 -side left
##ttk::frame $t.contents
##grid $t.tearoff $t.contents -sticky nsew
##grid columnconfigure $t $t.contents -weight 1
##grid columnconfigure $t.contents 1000 -weight 1
t = toolbar = Frame(w)
sep = ttk.Separator(w)
tearoff = ttk.Frame(t, cursor='fleur')
to = ttk.Separator(tearoff, orient='vertical')
to2 = ttk.Separator(tearoff, orient='vertical')
to.pack(fill=Y, expand=1, padx=2, side=LEFT)
to2.pack(fill=Y, expand=1, side=LEFT)
contents = ttk.Frame(t)
tearoff.grid(sticky='nsew')
contents.grid(sticky='nsew', row=0, column=1)
t.grid_columnconfigure(weight=1)
contents.grid_columnconfigure(weight=1)
contents.grid_columnconfigure(1000, weight=1)

## Bindings so that the toolbar can be torn off and reattached
##bind $t.tearoff     <B1-Motion> [list tearoff $t %X %Y]
##bind $t.tearoff.to  <B1-Motion> [list tearoff $t %X %Y]
##bind $t.tearoff.to2 <B1-Motion> [list tearoff $t %X %Y]
##proc tearoff {w x y} {
##    if {[string match $w* [winfo containing $x $y]]} {
##	return
##    }
##    grid remove $w
##    grid remove $w.tearoff
##    wm manage $w
##    wm protocol $w WM_DELETE_WINDOW [list untearoff $w]
##}
##proc untearoff {w} {
##    wm forget $w
##    grid $w.tearoff
##    grid $w
##}
def tearoff(w, x, y):
    if root.winfo_containing(x, y).startswith(w):
        return
    w.grid_remove()
    tearoff.grid_remove()
    w.wm_manage()
    w.wm_protocol('WM_DELETE_WINDOW', lambda: untearoff(w))
def untearoff(w):
    w.wm_forget()
    tearoff.grid()
    w.grid()
tearoff.bind('<B1-Motion>', lambda e: tearoff(t, e.x, e.y))
to.bind('<B1-Motion>', lambda e: tearoff(t, e.x, e.y))
to2.bind('<B1-Motion>', lambda e: tearoff(t, e.x, e.y))

#### Toolbar contents
##ttk::button $t.button -text "Button" -style Toolbutton -command [list \
##	$w.txt insert end "Button Pressed\n"]
##ttk::checkbutton $t.check -text "Check" -variable check -style Toolbutton \
##	-command [concat [list $w.txt insert end] {"check is $check\n"}]
##ttk::menubutton $t.menu -text "Menu" -menu $t.menu.m
##ttk::combobox $t.combo -value [lsort [font families]] -state readonly
##menu $t.menu.m
##$t.menu.m add command -label "Just" -command [list $w.txt insert end Just\n]
##$t.menu.m add command -label "An" -command [list $w.txt insert end An\n]
##$t.menu.m add command -label "Example" \
##	-command [list $w.txt insert end Example\n]
##bind $t.combo <<ComboboxSelected>> [list changeFont $w.txt $t.combo]
##proc changeFont {txt combo} {
##    $txt configure -font [list [$combo get] 10]
##}
button = ttk.Button(t, text='Button', style='Toolbutton',
                    command=lambda: txt.insert(END, 'Button Pressed\n'))
checkvar = StringVar()
check = ttk.Checkbutton(t, text='Check', variable=checkvar, style='Toolbutton',
    command=lambda: txt.insert(END, "check is "+checkvar.get()+"\n"))
menu = ttk.Menubutton(t, text='Menu')
combo = ttk.Combobox(t, value=font_families(), state='readonly')
menu['menu'] = m = Menu(menu)
m.add_command(label='Just', command=lambda: txt.insert(END, 'Just\n'))
m.add_command(label='An', command=lambda: txt.insert(END, 'An\n'))
m.add_command(label='Example', command=lambda: txt.insert(END, 'Example\n'))
def changeFont(txt, combo):
    txt.configure(font=combo.get()+' 10')
combo.bind('<<ComboboxSelected>>', lambda: changeFont(txt, combo))

#### Some content for the rest of the toplevel
##text $w.txt -width 40 -height 10
##interp alias {} doInsert {} $w.txt insert end	;# Make bindings easy to write
txt = Text(width=40, height=10)

#### Arrange contents
##grid $t.button $t.check $t.menu $t.combo -in $t.contents -padx 2 -sticky ns
##grid $t -sticky ew
##grid $w.sep -sticky ew
##grid $w.msg -sticky ew
##grid $w.txt -sticky nsew
##grid rowconfigure $w $w.txt -weight 1
##grid columnconfigure $w $w.txt -weight 1
for i, w in enumerate(button, check, menu, combo):
    w.grid(in=contents, padx=2, sticky='ns', row=0, column=i)
t.grid(sticky='ew')
sep.grid(sticky='ew')
msg.grid(sticky='ew')
txt.grid(sticky='ew')
w.grid_rowconfigure(weight=1)
txt.grid_rowconfigure(weight=1)
w.grid_columnconfigure(weight=1)
txt.grid_columnconfigure(weight=1)

## See Code / Dismiss buttons
##set btns [addSeeDismiss $w.buttons $w]
##grid $btns -sticky ew
##btns = addSeeDismiss(ttk.Frame(w), demo_name)
##btns.pack(sticky='ew')
btns = addSeeDismiss(ttk.Frame(w), demo_name)
btns.pack(sticky='ew')
