# menu.tcl --
#
# This demonstration script creates a window with a bunch of menus
# and cascaded menus using menubars.

##if {![info exists widgetDemo]} {
##    error "This script should be run from the \"widget\" demo."
##}
assert 'widgetDemo' in globals(), \
'This script should be run from the "widget" demo.'

##package require Tk

##set w .menu
##catch {destroy $w}
##toplevel $w
##wm title $w "Menu Demonstration"
##wm iconname $w "menu"
##positionWindow $w
demo_name = 'menu'
if demo_name in globals()['demo_name']:
    globals()['demo_name'][demo_name].destroy()
w = globals()['demo_name'][demo_name] = Toplevel(root)
w.wm_title('Menu Demonstration')
w.wm_iconname('menu')
positionWindow(w)

##label $w.msg -font $font -wraplength 4i -justify left 
##if {[tk windowingsystem] eq "aqua"} {
##    catch {set origUseCustomMDEF $::tk::mac::useCustomMDEF; set ::tk::mac::useCustomMDEF 1}
##    $w.msg configure -text "This window has a menubar with cascaded menus.  You can invoke entries with an accelerator by typing Command+x, where \"x\" is the character next to the command key symbol. The rightmost menu can be torn off into a palette by selecting the first item in the menu."
##} else {
##    $w.msg configure -text "This window contains a menubar with cascaded menus.  You can post a menu from the keyboard by typing Alt+x, where \"x\" is the character underlined on the menu.  You can then traverse among the menus using the arrow keys.  When a menu is posted, you can invoke the current entry by typing space, or you can invoke any entry by typing its underlined character.  If a menu entry has an accelerator, you can invoke the entry without posting the menu just by typing the accelerator. The rightmost menu can be torn off into a palette by selecting the first item in the menu."
##}
##pack $w.msg -side top
msg = Label(w, font=font, wraplength='4i', justify=LEFT)
if sys.platform == 'darwin':
    try:
        root.tk.call("set", "origUseCustomMDEF", "$::tk::mac::useCustomMDEF")
        root.tk.call("set", "::tk::mac::useCustomMDEF", "1")
    except:
        pass
    msg['text'] = "This window has a menubar with cascaded menus.  You can invoke entries with an accelerator by typing Command+x, where \"x\" is the character next to the command key symbol. The rightmost menu can be torn off into a palette by selecting the first item in the menu."
else:
    msg['text'] = "This window contains a menubar with cascaded menus.  You can post a menu from the keyboard by typing Alt+x, where \"x\" is the character underlined on the menu.  You can then traverse among the menus using the arrow keys.  When a menu is posted, you can invoke the current entry by typing space, or you can invoke any entry by typing its underlined character.  If a menu entry has an accelerator, you can invoke the entry without posting the menu just by typing the accelerator. The rightmost menu can be torn off into a palette by selecting the first item in the menu."
msg.pack(side=TOP)

##set menustatus "    "
##frame $w.statusBar
##label $w.statusBar.label -textvariable menustatus -relief sunken -bd 1 -font "Helvetica 10" -anchor w
##pack $w.statusBar.label -side left -padx 2 -expand yes -fill both
##pack $w.statusBar -side bottom -fill x -pady 2
menustatus = StringVar(value="    ")
statusBar = Frame(w)
label = Label(statusBar, textvariable=menustatus, relief=SUNKEN, bd=1,
              font="Helvetica 10", anchor=W)
label.pack(side=LEFT, padx=2, expand=YES, fill=BOTH)
statusBar.pack(side=BOTTOM, fill=X, pady=2)

## See Code / Dismiss buttons
##set btns [addSeeDismiss $w.buttons $w]
##pack $btns -side bottom -fill x
btns = addSeeDismiss(ttk.Frame(w), demo_name)
btns.pack(side=BOTTOM, fill=X)

##menu $w.menu -tearoff 0
##
##set m $w.menu.file
##menu $m -tearoff 0
##$w.menu add cascade -label "File" -menu $m -underline 0
##$m add command -label "Open..." -command {error "this is just a demo: no action has been defined for the \"Open...\" entry"}
##$m add command -label "New" -command {error "this is just a demo: no action has been defined for the \"New\" entry"}
##$m add command -label "Save" -command {error "this is just a demo: no action has been defined for the \"Save\" entry"}
##$m add command -label "Save As..." -command {error "this is just a demo: no action has been defined for the \"Save As...\" entry"}
##$m add separator
##$m add command -label "Print Setup..." -command {error "this is just a demo: no action has been defined for the \"Print Setup...\" entry"}
##$m add command -label "Print..." -command {error "this is just a demo: no action has been defined for the \"Print...\" entry"}
##$m add separator
##$m add command -label "Dismiss Menus Demo" -command "destroy $w"
menu = Menu(w, tearoff=0)
m = Menu(menu, tearoff=0)
menu.add_cascade(label='File', menu=m, underline=0)
def error(msg):
    messagebox.showerror('error', msg)
m.add_command(label='Open...', command=lambda: error("this is just a demo: no action has been defined for the \"Open...\" entry"))
m.add_command(label='New.', command=lambda: error("this is just a demo: no action has been defined for the \"New\" entry"))
m.add_command(label='Save', command=lambda: error("this is just a demo: no action has been defined for the \"Save\" entry"))
m.add_command(label='Save As...', command=lambda: error("this is just a demo: no action has been defined for the \"Save As...\" entry"))
m.add_separator()
m.add_command(label='Print Setup...', command=lambda: error("this is just a demo: no action has been defined for the \"Print Setup...\" entry"))
m.add_command(label='Print...', command=lambda: error("this is just a demo: no action has been defined for the \"Print...\" entry"))
m.add_separator()
m.add_command(label='Dismiss Menus Demo', command=w.destroy)

##set m $w.menu.basic
##$w.menu add cascade -label "Basic" -menu $m -underline 0
##menu $m -tearoff 0
##$m add command -label "Long entry that does nothing"
##if {[tk windowingsystem] eq "aqua"} {
##    set modifier Command
##} elseif {[tk windowingsystem] == "win32"} {
##    set modifier Control
##} else {
##    set modifier Meta
##}
##foreach i {A B C D E F} {
##    $m add command -label "Print letter \"$i\"" -underline 14 \
##	    -accelerator Meta+$i -command "puts $i" -accelerator $modifier+$i
##    bind $w <$modifier-[string tolower $i]> "puts $i"
##}
m = Menu(menu, tearoff=0)
menu.add_cascade(label='Basic', menu=m, underline=0)
m.add_command(label='Long entry that does nothing')
if sys.platform == 'darwin':
    modifier = 'Command'
elif sys.platform == 'win32':
    modifier = 'Control'
else:
    modifier = 'Meta'
for i in 'A', 'B', 'C', 'D', 'E', 'F':
    m.add_command(label='Print letter "'+i+'"', underline=14,
                  #accelerator='Meta+'+i,
                  command=lambda i=i: print(i),
                  accelerator=modifier+'+'+i)
    w.bind('<'+modifier+'-'+i.lower()+'>', lambda i=i: print(i))

##set m $w.menu.cascade
##$w.menu add cascade -label "Cascades" -menu $m -underline 0
##menu $m -tearoff 0
##$m add command -label "Print hello" \
##	-command {puts stdout "Hello"} -accelerator $modifier+H -underline 6
##bind $w <$modifier-h> {puts stdout "Hello"}
##$m add command -label "Print goodbye" -command {\
##    puts stdout "Goodbye"} -accelerator $modifier+G -underline 6
##bind $w <$modifier-g> {puts stdout "Goodbye"}
##$m add cascade -label "Check buttons" \
##	-menu $w.menu.cascade.check -underline 0
##$m add cascade -label "Radio buttons" \
##	-menu $w.menu.cascade.radio -underline 0
m = cascade = Menu(menu, tearoff=0)
menu.add_cascade(label='Cascades', menu=m, underline=0)
m.add_command(label='Print hello',
              command=lambda: print('Hello'),
              accelerator=modifier+'+H', underline=6)
w.bind('<'+modifier+'-h>', lambda: print('Hello'))
m.add_command(label='Print goodbye',
              command=lambda: print('Goodbye'),
              accelerator=modifier+'+G', underline=6)
w.bind('<'+modifier+'-g>', lambda: print('Goodbye'))

##set m $w.menu.cascade.check
##menu $m -tearoff 0
##$m add check -label "Oil checked" -variable oil
##$m add check -label "Transmission checked" -variable trans
##$m add check -label "Brakes checked" -variable brakes
##$m add check -label "Lights checked" -variable lights
##$m add separator
##$m add command -label "Show current values" \
##    -command "showVars $w.menu.cascade.dialog oil trans brakes lights"
##$m invoke 1
##$m invoke 3
m = check = Menu(cascade, tearoff=0)
oil=BooleanVar(name='oil')
trans=BooleanVar(name='trans')
brakes=BooleanVar(name='brakes')
lights=BooleanVar(name='lights')
m.add_checkbutton(label='Oil checked', variable=oil)
m.add_checkbutton(label='Transmission checked', variable=trans)
m.add_checkbutton(label='Brakes checked', variable=brakes)
m.add_checkbutton(label='Lights checked', variable=lights)
m.add_separator()
m.add_command(label='Show current values',
              command=lambda: showVars(cascade, oil, trans, brakes, lights))
m.invoke(1)
m.invoke(3)

##set m $w.menu.cascade.radio
##menu $m -tearoff 0
##$m add radio -label "10 point" -variable pointSize -value 10
##$m add radio -label "14 point" -variable pointSize -value 14
##$m add radio -label "18 point" -variable pointSize -value 18
##$m add radio -label "24 point" -variable pointSize -value 24
##$m add radio -label "32 point" -variable pointSize -value 32
##$m add sep
##$m add radio -label "Roman" -variable style -value roman
##$m add radio -label "Bold" -variable style -value bold
##$m add radio -label "Italic" -variable style -value italic
##$m add sep
##$m add command -label "Show current values" \
##	-command "showVars $w.menu.cascade.dialog pointSize style"
##$m invoke 1
##$m invoke 7
m = radio = Menu(cascade, tearoff=0)
pointSize = IntVar(name='pointSize')
m.add_radiobutton(label='10 point', variable=pointSize, value=10)
m.add_radiobutton(label='14 point', variable=pointSize, value=14)
m.add_radiobutton(label='18 point', variable=pointSize, value=18)
m.add_radiobutton(label='24 point', variable=pointSize, value=24)
m.add_radiobutton(label='32 point', variable=pointSize, value=32)
m.add_separator()
style = StringVar(name='style')
m.add_radiobutton(label='Roman', variable=style, value='roman')
m.add_radiobutton(label='Bold', variable=style, value='bold')
m.add_radiobutton(label='Italic', variable=style, value='italic')
m.add_separator()
m.add_command(label='Show current values',
              command=lambda: showVars(cascade, pointSize, style))
m.invoke(1)
m.invoke(7)
cascade.add_cascade(label='Check buttons', menu=check, underline=0)
cascade.add_cascade(label='Radio buttons', menu=radio, underline=0)

##set m $w.menu.icon
##$w.menu add cascade -label "Icons" -menu $m -underline 0
##menu $m -tearoff 0
### Main widget program sets variable tk_demoDirectory
##$m add command -bitmap @[file join $tk_demoDirectory images pattern.xbm] \
##    -hidemargin 1 -command [list \
##	tk_dialog $w.pattern {Bitmap Menu Entry} \
##		"The menu entry you invoked displays a bitmap rather than\
##		a text string.  Other than this, it is just like any other\
##		menu entry." {} 0 OK ]
##foreach i {info questhead error} {
##    $m add command -bitmap $i -hidemargin 1 -command [list \
##	    puts "You invoked the $i bitmap" ]
##}
##$m entryconfigure 2 -columnbreak 1
m = Menu(menu, tearoff=0)
menu.add_cascade(label='Icons', menu=m, underline=0)
from tkinter.dialog import Dialog
globals().update(locals())
m.add_command(bitmap='@'+tk_demoDirectory+'/images/pattern.xbm', hidemargin=1,
    command=lambda: Dialog(w, title='Bitmap Menu Entry',
        text=
            "The menu entry you invoked displays a bitmap rather than "
            "a text string.  Other than this, it is just like any other "
            "menu entry.",
        bitmap='', default=0, strings=('OK',)))
for i in 'info', 'questhead', 'error':
    m.add_command(bitmap=i, hidemargin=1,
                  command=lambda i=i: print('You invoked the', i, 'bitmap'))
m.entryconfigure(2, columnbreak=1)

##set m $w.menu.more
##$w.menu add cascade -label "More" -menu $m -underline 0
##menu $m -tearoff 0
##foreach i {{An entry} {Another entry} {Does nothing} {Does almost nothing} {Make life meaningful}} {
##    $m add command -label $i -command [list puts "You invoked \"$i\""]
##}
##$m entryconfigure "Does almost nothing" -bitmap questhead -compound left \
##	-command [list \
##	tk_dialog $w.compound {Compound Menu Entry} \
##		"The menu entry you invoked displays both a bitmap and a\
##		text string.  Other than this, it is just like any other\
##		menu entry." {} 0 OK ]
m = Menu(menu, tearoff=0)
menu.add_cascade(label='More', menu=m, underline=0)
for i in ('An entry', 'Another entry', 'Does nothing',
          'Does almost nothing', 'Make life meaningful'):
    m.add_command(label=i, command=lambda i=i: print('You invoked "', i, '"'))
m.entryconfigure('Does almost nothing', bitmap='questhead', compound=LEFT,
    command=lambda: Dialog(w, title='Compound Menu Entry',
        text=
            "The menu entry you invoked displays both a bitmap and a "
            "text string.  Other than this, it is just like any other "
            "menu entry.",
        bitmap='', default=0, strings=('OK',)))

##set m $w.menu.colors
##$w.menu add cascade -label "Colors" -menu $m -underline 1
##menu $m -tearoff 1
##foreach i {red orange yellow green blue} {
##    $m add command -label $i -background $i -command [list \
##	    puts "You invoked \"$i\"" ]
##}
m = Menu(menu, tearoff=1)
menu.add_cascade(label='Colors', menu=m, underline=1)
for i in 'red', 'orange', 'yellow', 'green', 'blue':
    m.add_command(label=i, background=i,
                  command=lambda i=i: print('You invoked "', i, '"'))

##$w configure -menu $w.menu
##
##bind Menu <<MenuSelect>> {
##    global $menustatus
##    if {[catch {%W entrycget active -label} label]} {
##	set label "    "
##    }
##    set menustatus $label
##    update idletasks
##}
w['menu'] = menu
def menu_select():
    global menustatus
    try:
        label = w.entrycget_active('label')
    except:
        label = "    "
    menustatus = label
    root.update_idletasks()
    
root.bind_class(Menu, '<<MenuSelect>>', menu_select)

#if {[tk windowingsystem] eq "aqua"} {catch {set ::tk::mac::useCustomMDEF $origUseCustomMDEF}}
if sys.platform == 'darwin':
    try:
        root.tk.call("set", "::tk::mac::useCustomMDEF", "$origUseCustomMDEF")
    except:
        pass
