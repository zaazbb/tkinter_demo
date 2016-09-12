# msgbox.tcl --
#
# This demonstration script creates message boxes of various type

##if {![info exists widgetDemo]} {
##    error "This script should be run from the \"widget\" demo."
##}
assert 'widgetDemo' in globals(), \
'This script should be run from the "widget" demo.'

##package require Tk

##set w .msgbox
##catch {destroy $w}
##toplevel $w
##wm title $w "Message Box Demonstration"
##wm iconname $w "messagebox"
##positionWindow $w
demo_name = 'msgbox'
if demo_name in globals():
    globals()[demo_name].destroy()
w = globals()[demo_name] = Toplevel(root)
w.wm_title('Message Box Demonstration')
w.wm_iconname('messagebox')
positionWindow(w)

##label $w.msg -font $font -wraplength 4i -justify left -text "Choose the icon and type option of the message box. Then press the \"Message Box\" button to see the message box."
##pack $w.msg -side top
msg = Label(w, font=font, wraplength='4i', justify=LEFT, text="Choose the icon and type option of the message box. Then press the \"Message Box\" button to see the message box.")
msg.pack(side=TOP)

##pack [addSeeDismiss $w.buttons $w {} {
##    ttk::button $w.buttons.vars -text "Message Box" -command "showMessageBox $w"
##}] -side bottom -fill x
###pack $w.buttons.dismiss $w.buttons.code $w.buttons.vars -side left -expand 1
buttons = ttk.Frame(w)
vars = ttk.Button(buttons, text='Message Box',
                  command=lambda: showMessageBox(w))
addSeeDismiss(buttons, demo_name, None, [vars]).pack(side=BOTTOM, fill=X)

##frame $w.left 
##frame $w.right
##pack $w.left $w.right -side left -expand yes -fill y  -pady .5c -padx .5c
left = Frame(w)
right = Frame(w)
for ww in left, right:
    ww.pack(side=LEFT, expand=YES, fill=Y, pady='.5c', padx='.5c')

##label $w.left.label -text "Icon"
##frame $w.left.sep -relief ridge -bd 1 -height 2
##pack $w.left.label -side top
##pack $w.left.sep -side top -fill x -expand no
label = Label(left, text='Icon')
sep = Frame(left, relief='ridge', bd=1, height=2)
label.pack(side=TOP)
sep.pack(side=TOP, fill=X, expand='no')

##set msgboxIcon info
##foreach i {error info question warning} {
##    radiobutton $w.left.b$i -text $i -variable msgboxIcon \
##	-relief flat -value $i -width 16 -anchor w
##    pack $w.left.b$i  -side top -pady 2 -anchor w -fill x
##}
msgboxIcon = StringVar(value='info')
for i in 'error', 'info', 'question', 'warning':
    Radiobutton(left, text=i, variable=msgboxIcon,
                relief=FLAT, value=i, width=16, anchor=W)\
        .pack(side=TOP, pady=2, anchor=W, fill=X)  

##label $w.right.label -text "Type"
##frame $w.right.sep -relief ridge -bd 1 -height 2
##pack $w.right.label -side top
##pack $w.right.sep -side top -fill x -expand no
label = Label(right, text='Type')
sep = Frame(right, relief='ridge', bd=1, height=2)
label.pack(side=TOP)
sep.pack(side=TOP, fill=X, expand='no')

##set msgboxType ok
##foreach t {abortretryignore ok okcancel retrycancel yesno yesnocancel} {
##    radiobutton $w.right.$t -text $t -variable msgboxType \
##	-relief flat -value $t -width 16 -anchor w
##    pack $w.right.$t -side top -pady 2 -anchor w -fill x
##}
msgboxType = StringVar(value='ok')
for t in ('abortretryignore', 'ok', 'okcancel',
          'retrycancel', 'yesno', 'yesnocancel'):
    Radiobutton(right, text=t, variable=msgboxType,
                relief=FLAT, value=t, width=16, anchor=W)\
        .pack(side=TOP, pady=2, anchor=W, fill=X)

##proc showMessageBox {w} {
##    global msgboxIcon msgboxType
##    set button [tk_messageBox -icon $msgboxIcon -type $msgboxType \
##	-title Message -parent $w\
##	-message "This is a \"$msgboxType\" type messagebox with the \"$msgboxIcon\" icon"]
##    
##    tk_messageBox -icon info -message "You have selected \"$button\"" -type ok\
##	-parent $w
##}
def showMessageBox(w):
    global msgboxIcon, msgboxType
    button = messagebox._show(icon=msgboxIcon.get(), type=msgboxType.get(),
                              title='Message', parent=w,
                              message='This is a "'\
                                  +msgboxType.get()\
                                  +'" type messagebox with the "'\
                                  +msgboxIcon.get()\
                                  +'" icon')
    messagebox.showinfo(message='You have selected "'+button+'"')


locals_ = locals()
del locals_['t']
globals().update(locals_)
