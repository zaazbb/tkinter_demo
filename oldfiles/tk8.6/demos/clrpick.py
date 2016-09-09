# clrpick.tcl --
#
# This demonstration script prompts the user to select a color.

##if {![info exists widgetDemo]} {
##    error "This script should be run from the \"widget\" demo."
##}
assert 'widgetDemo' in globals(), \
'This script should be run from the "widget" demo.'

##package require Tk

##set w .clrpick
##catch {destroy $w}
##toplevel $w
##wm title $w "Color Selection Dialog"
##wm iconname $w "colors"
##positionWindow $w
demo_name = 'clrpick'
if demo_name in globals()['demo_name']:
    globals()['demo_name'][demo_name].destroy()
w = globals()['demo_name'][demo_name] = Toplevel(root)
w.wm_title('Color Selection Dialog')
w.wm_iconname('colors')
positionWindow(w)

##label $w.msg -font $font -wraplength 4i -justify left -text "Press the buttons below to choose the foreground and background colors for the widgets in this window."
##pack $w.msg -side top
msg = Label(w, font=font, wraplength='4i', justify=LEFT, text="Press the buttons below to choose the foreground and background colors for the widgets in this window.")
msg.pack(side=TOP)

## See Code / Dismiss buttons
##set btns [addSeeDismiss $w.buttons $w]
##pack $btns -side bottom -fill x
btns = addSeeDismiss(ttk.Frame(w), demo_name)
btns.pack(side=BOTTOM, fill=X)

##button $w.back -text "Set background color ..." \
##    -command \
##    "setColor $w $w.back background {-background -highlightbackground}"
##button $w.fore -text "Set foreground color ..." \
##    -command \
##    "setColor $w $w.back foreground -foreground"
##
##pack $w.back $w.fore -side top -anchor c -pady 2m
back = Button(w, text='Set background color ...',
              command=lambda: setColor(w, back, 'background',
                                       ['background', 'highlightbackground']))
fore = Button(w, text='Set foreground color ...',
              command=lambda: setColor(w, back, 'foreground', ['foreground']))
for ww in back, fore:
    ww.pack(side=TOP, anchor='c', pady='2m')

##proc setColor {w button name options} {
##    grab $w
##    set initialColor [$button cget -$name]
##    set color [tk_chooseColor -title "Choose a $name color" -parent $w \
##	-initialcolor $initialColor]
##    if {[string compare $color ""]} {
##	setColor_helper $w $options $color
##    }
##    grab release $w
##}
def setColor(w, button, name, options):
    from tkinter import colorchooser
    w.grab_set()
    initialColor = button.cget(name)
    color = colorchooser.askcolor(initialColor, parent=w,
                                  title='Choose a '+name+' color')
    if color[1]:
        setColor_helper(w, options, color[1])
    w.grab_release()

##proc setColor_helper {w options color} {
##    foreach option $options {
##	catch {
##	    $w config $option $color
##	}
##    }
##    foreach child [winfo children $w] {
##	setColor_helper $child $options $color
##    }
##}
def setColor_helper(w, options, color):
    for option in options:
        try:
            w.config(**{option: color})
        except:
            pass
    for child in w.winfo_children():
        setColor_helper(child, options, color)

globals().update(locals())
