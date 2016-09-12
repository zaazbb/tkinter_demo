# ttkmenu.tcl --
#
# This demonstration script creates a toplevel window containing several Ttk
# menubutton widgets.

##if {![info exists widgetDemo]} {
##    error "This script should be run from the \"widget\" demo."
##}
assert 'widgetDemo' in globals(), \
'This script should be run from the "widget" demo.'

##package require Tk

##set w .ttkmenu
##catch {destroy $w}
##toplevel $w
##wm title $w "Ttk Menu Buttons"
##wm iconname $w "ttkmenu"
##positionWindow $w
demo_name = 'ttkmenu'
if demo_name in globals()['demo_name']:
    globals()['demo_name'][demo_name].destroy()
w = globals()['demo_name'][demo_name] = Toplevel(root)
w.wm_title('Ttk Menu Buttons')
w.wm_iconname('ttkmenu')
positionWindow(w)

##ttk::label $w.msg -font $font -wraplength 4i -justify left -text "Ttk is the new Tk themed widget set, and one widget that is available in themed form is the menubutton. Below are some themed menu buttons that allow you to pick the current theme in use. Notice how picking a theme changes the way that the menu buttons themselves look, and that the central menu button is styled differently (in a way that is normally suitable for toolbars). However, there are no themed menus; the standard Tk menus were judged to have a sufficiently good look-and-feel on all platforms, especially as they are implemented as native controls in many places."
##pack $w.msg [ttk::separator $w.msgSep] -side top -fill x
msg = ttk.Label(w, font=font, wraplength='4i', justify=LEFT, text="Ttk is the new Tk themed widget set, and one widget that is available in themed form is the menubutton. Below are some themed menu buttons that allow you to pick the current theme in use. Notice how picking a theme changes the way that the menu buttons themselves look, and that the central menu button is styled differently (in a way that is normally suitable for toolbars). However, there are no themed menus; the standard Tk menus were judged to have a sufficiently good look-and-feel on all platforms, especially as they are implemented as native controls in many places.")
msgSep = ttk.Separator(w)
msg.pack(side=TOP, fill=X)
msgSep.pack(side=TOP, fill=X)

## See Code / Dismiss
##pack [addSeeDismiss $w.seeDismiss $w] -side bottom -fill x
addSeeDismiss(ttk.Frame(w), demo_name).pack(side=BOTTOM, fill=X)

##ttk::menubutton $w.m1 -menu $w.m1.menu -text "Select a theme" -direction above
##ttk::menubutton $w.m2 -menu $w.m1.menu -text "Select a theme" -direction left
##ttk::menubutton $w.m3 -menu $w.m1.menu -text "Select a theme" -direction right
##ttk::menubutton $w.m4 -menu $w.m1.menu -text "Select a theme" \
##	-direction flush -style TMenubutton.Toolbutton
##ttk::menubutton $w.m5 -menu $w.m1.menu -text "Select a theme" -direction below
m1 = ttk.Menubutton(w, text='Select a theme', direction='above')
m2 = ttk.Menubutton(w, text='Select a theme', direction=LEFT)
m3 = ttk.Menubutton(w, text='Select a theme', direction=RIGHT)
m4 = ttk.Menubutton(w, text='Select a theme', direction='flush',
                    style='TMenubutton.Toolbutton')
m5 = ttk.Menubutton(w, text='Select a theme', direction='below')

##menu $w.m1.menu -tearoff 0
##menu $w.m2.menu -tearoff 0
##menu $w.m3.menu -tearoff 0
##menu $w.m4.menu -tearoff 0
##menu $w.m5.menu -tearoff 0
m1['menu'] = menu1 = Menu(m1, tearoff=0)
m2['menu'] = menu2 = Menu(m2, tearoff=0)
m3['menu'] = menu3 = Menu(m3, tearoff=0)
m4['menu'] = menu4 = Menu(m4, tearoff=0)
m5['menu'] = menu5 = Menu(m5, tearoff=0)

##foreach theme [ttk::themes] {
##    $w.m1.menu add command -label $theme -command [list ttk::setTheme $theme]
##    $w.m2.menu add command -label $theme -command [list ttk::setTheme $theme]
##    $w.m3.menu add command -label $theme -command [list ttk::setTheme $theme]
##    $w.m4.menu add command -label $theme -command [list ttk::setTheme $theme]
##    $w.m5.menu add command -label $theme -command [list ttk::setTheme $theme]
##}
global style
style = ttk.Style()
for theme in style.theme_names():
    menu1.add_command(label=theme,
                      command=lambda theme=theme: style.theme_use(theme))
    menu2.add_command(label=theme,
                      command=lambda theme=theme: style.theme_use(theme))
    menu3.add_command(label=theme,
                      command=lambda theme=theme: style.theme_use(theme))
    menu4.add_command(label=theme,
                      command=lambda theme=theme: style.theme_use(theme))
    menu5.add_command(label=theme,
                      command=lambda theme=theme: style.theme_use(theme))

##pack [ttk::frame $w.f] -fill x
##pack [ttk::frame $w.f1] -fill both -expand yes
##lower $w.f
f = ttk.Frame(w)
f.pack(fill=X)
f1 = ttk.Frame(w)
f1.pack(fill=BOTH, expand=YES)
f.lower()

##grid anchor $w.f center
##grid   x   $w.m1   x    -in $w.f -padx 3 -pady 2
##grid $w.m2 $w.m4 $w.m3  -in $w.f -padx 3 -pady 2
##grid   x   $w.m5   x    -in $w.f -padx 3 -pady 2
f.grid_anchor(CENTER)
m1.grid(in_=f, padx=3, pady=2, column=1)
m2.grid(in_=f, padx=3, pady=2, row=3, column=0)
m4.grid(in_=f, padx=3, pady=2, row=3, column=1)
m3.grid(in_=f, padx=3, pady=2, row=3, column=2)
m5.grid(in_=f, padx=3, pady=2, row=5, column=1)
