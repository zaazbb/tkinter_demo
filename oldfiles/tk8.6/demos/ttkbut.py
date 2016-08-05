# ttkbut.tcl --
#
# This demonstration script creates a toplevel window containing several
# simple Ttk widgets, such as labels, labelframes, buttons, checkbuttons and
# radiobuttons.

##if {![info exists widgetDemo]} {
##    error "This script should be run from the \"widget\" demo."
##}
assert 'widgetDemo' in globals(), \
'This script should be run from the "widget" demo.'

##package require Tk
from tkinter import *

##set w .ttkbut
##catch {destroy $w}
##toplevel $w
##wm title $w "Simple Ttk Widgets"
##wm iconname $w "ttkbut"
##positionWindow $w
demo_name = 'ttkbut'
if demo_name in globals()['demo_name']:
    globals()['demo_name'][demo_name].destroy()
w = globals()['demo_name'][demo_name] = Toplevel(root)
w.wm_title('Simple Ttk Widgets')
w.wm_iconname('ttkbut')
positionWindow(w)

##ttk::label $w.msg -font $font -wraplength 4i -justify left -text "Ttk is the new Tk themed widget set. This is a Ttk themed label, and below are three groups of Ttk widgets in Ttk labelframes. The first group are all buttons that set the current application theme when pressed. The second group contains three sets of checkbuttons, with a separator widget between the sets. Note that the \u201cEnabled\u201d button controls whether all the other themed widgets in this toplevel are in the disabled state. The third group has a collection of linked radiobuttons."
##pack $w.msg -side top -fill x
msg = ttk.Label(w, font=font_, wraplength='4i', justify='left', text="Ttk is the new Tk themed widget set. This is a Ttk themed label, and below are three groups of Ttk widgets in Ttk labelframes. The first group are all buttons that set the current application theme when pressed. The second group contains three sets of checkbuttons, with a separator widget between the sets. Note that the \u201cEnabled\u201d button controls whether all the other themed widgets in this toplevel are in the disabled state. The third group has a collection of linked radiobuttons.")
msg.pack(side='top', fill='x')

## See Code / Dismiss
##pack [addSeeDismiss $w.seeDismiss $w {enabled cheese tomato basil oregano happyness}]\
##	-side bottom -fill x
enabled = BooleanVar(name='enabled')
cheese = BooleanVar(name='cheese')
tomato = BooleanVar(name='tomato')
basil = BooleanVar(name='basil')
oregano = BooleanVar(name='oregano')
happyness = StringVar(name='happyness')
addSeeDismiss(w, demo_name, [enabled, cheese, tomato, basil, oregano, happyness]
              ).pack(side='bottom', fill='x')

## Add buttons for setting the theme
##ttk::labelframe $w.buttons -text "Buttons"
##foreach theme [ttk::themes] {
##    ttk::button $w.buttons.$theme -text $theme \
##	    -command [list ttk::setTheme $theme]
##    pack $w.buttons.$theme -pady 2
##}
f = ttk.Frame(w)
f.pack(fill='both', expand=1)
buttons = ttk.LabelFrame(f, text='Buttons')
style = ttk.Style()
for theme in style.theme_names():
    button = ttk.Button(buttons, text=theme,
                        command=lambda  theme=theme: style.theme_use(theme))
    button.pack(pady=2)

## Helper procedure for the top checkbutton
##proc setState {rootWidget exceptThese value} {
##    if {$rootWidget in $exceptThese} {
##	return
##    }
##    ## Non-Ttk widgets (e.g. the toplevel) will fail, so make it silent
##    catch {
##	$rootWidget state $value
##    }
##    ## Recursively invoke on all children of this root that are in the same
##    ## toplevel widget
##    foreach w [winfo children $rootWidget] {
##	if {[winfo toplevel $w] eq [winfo toplevel $rootWidget]} {
##	    setState $w $exceptThese $value
##	}
##    }
##}
def setState(rootWidget, exceptThese, value):
    if rootWidget in exceptThese: return
    try: rootWidget['state'] = value
    except: pass
    for w in rootWidget.winfo_children():
        if w.winfo_toplevel() == rootWidget.winfo_toplevel():
            setState(w, exceptThese, value)

## Set up the checkbutton group
##ttk::labelframe $w.checks -text "Checkbuttons"
##ttk::checkbutton $w.checks.e  -text Enabled -variable enabled -command {
##    setState .ttkbut .ttkbut.checks.e \
##	    [expr {$enabled ? "!disabled" : "disabled"}]
##}
##set enabled 1
#### See ttk_widget(n) for other possible state flags
##ttk::separator   $w.checks.sep1
##ttk::checkbutton $w.checks.c1 -text Cheese  -variable cheese
##ttk::checkbutton $w.checks.c2 -text Tomato  -variable tomato
##ttk::separator   $w.checks.sep2
##ttk::checkbutton $w.checks.c3 -text Basil   -variable basil
##ttk::checkbutton $w.checks.c4 -text Oregano -variable oregano
##pack $w.checks.e $w.checks.sep1 $w.checks.c1 $w.checks.c2 $w.checks.sep2 \
##	$w.checks.c3 $w.checks.c4   -fill x -pady 2
checks = ttk.LabelFrame(f, text='Checkbuttons')
e = ttk.Checkbutton(checks, text='Enabled', variable=enabled)
globals().update(locals())
e['command'] = lambda: setState(w, [e], '!disabled' if enabled.get() else 'disabled')
enabled.set(1)
sep1 = ttk.Separator(checks)
c1 = ttk.Checkbutton(checks, text='Cheese', variable=cheese)
c2 = ttk.Checkbutton(checks, text='Tomato', variable=tomato)
sep2 = ttk.Separator(checks)
c3 = ttk.Checkbutton(checks, text='Basil', variable=basil)
c4 = ttk.Checkbutton(checks, text='Oregano', variable=oregano)
for w in [e, sep1, c1, c2, sep2, c3, c4]: w.pack(fill='x', pady=2)
                
## Set up the radiobutton group
##ttk::labelframe $w.radios -text "Radiobuttons"
##ttk::radiobutton $w.radios.r1 -text "Great" -variable happyness -value great
##ttk::radiobutton $w.radios.r2 -text "Good" -variable happyness -value good
##ttk::radiobutton $w.radios.r3 -text "OK" -variable happyness -value ok
##ttk::radiobutton $w.radios.r4 -text "Poor" -variable happyness -value poor
##ttk::radiobutton $w.radios.r5 -text "Awful" -variable happyness -value awful
##pack $w.radios.r1 $w.radios.r2 $w.radios.r3 $w.radios.r4 $w.radios.r5 \
##	-fill x -padx 3 -pady 2
radios = ttk.LabelFrame(f, text='Radiobuttons')
r1 = ttk.Radiobutton(radios, text='Great', variable=happyness, value='great')
r2 = ttk.Radiobutton(radios, text='Good', variable=happyness, value='good')
r3 = ttk.Radiobutton(radios, text='OK', variable=happyness, value='ok')
r4 = ttk.Radiobutton(radios, text='Poor', variable=happyness, value='poor')
r5 = ttk.Radiobutton(radios, text='Awful', variable=happyness, value='awful')
for w in [r1, r2, r3, r4, r5]: w.pack(fill='x', padx=3, pady=3)

## Arrange things neatly
##pack [ttk::frame $w.f] -fill both -expand 1
##lower $w.f
##grid $w.buttons $w.checks $w.radios -in $w.f -sticky nwe -pady 2 -padx 3
##grid columnconfigure $w.f {0 1 2} -weight 1 -uniform yes
##f = ttk.Frame(w)
##f.pack(fill='both', expand=1)
f.lower()
for i, w in enumerate([buttons, checks, radios]):
    w.grid(column=i, row=0, sticky='nwe', pady=2, padx=3)
f.grid_columnconfigure('0 1 2', weight=1, uniform='yes')

