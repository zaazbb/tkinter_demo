# ttkprogress.tcl --
#
# This demonstration script creates several progress bar widgets.

##if {![info exists widgetDemo]} {
##    error "This script should be run from the \"widget\" demo."
##}
assert 'widgetDemo' in globals(), \
'This script should be run from the "widget" demo.'

##package require Tk

##set w .ttkprogress
##catch {destroy $w}
##toplevel $w
##wm title $w "Progress Bar Demonstration"
##wm iconname $w "ttkprogress"
##positionWindow $w
demo_name = 'ttkprogress'
if demo_name in globals()['demo_name']:
    globals()['demo_name'][demo_name].destroy()
w = globals()['demo_name'][demo_name] = Toplevel(root)
w.wm_title('Progress Bar Demonstration')
w.wm_iconname('ttkprogress')
positionWindow(w)

##ttk::label $w.msg -font $font -wraplength 4i -justify left -text "Below are two progress bars. The top one is a \u201Cdeterminate\u201D progress bar, which is used for showing how far through a defined task the program has got. The bottom one is an \u201Cindeterminate\u201D progress bar, which is used to show that the program is busy but does not know how long for. Both are run here in self-animated mode, which can be turned on and off using the buttons underneath."
##pack $w.msg -side top -fill x
msg = ttk.Label(w, font=font, wraplength='4i', justify=LEFT, text="Below are two progress bars. The top one is a \u201Cdeterminate\u201D progress bar, which is used for showing how far through a defined task the program has got. The bottom one is an \u201Cindeterminate\u201D progress bar, which is used to show that the program is busy but does not know how long for. Both are run here in self-animated mode, which can be turned on and off using the buttons underneath.")
msg.pack(side=TOP, fill=X)

## See Code / Dismiss buttons
##set btns [addSeeDismiss $w.buttons $w]
##pack $btns -side bottom -fill x
btns = addSeeDismiss(ttk.Frame(w), demo_name)
btns.pack(side=BOTTOM, fill=X)

##ttk::frame $w.f
##pack $w.f -fill both -expand 1
##set w $w.f
w = ttk.Frame(w)
w.pack(fill=BOTH, expand=1)

##proc doBars {op args} {
##    foreach w $args {
##	$w $op
##    }
##}
##ttk::progressbar $w.p1 -mode determinate
##ttk::progressbar $w.p2 -mode indeterminate
##ttk::button $w.start -text "Start Progress" -command [list \
##	doBars start $w.p1 $w.p2]
##ttk::button $w.stop -text "Stop Progress" -command [list \
##	doBars stop $w.p1 $w.p2]
def doBars(op, *args):
    for w in args:
        getattr(w, op)()
p1 = ttk.Progressbar(w, mode='determinate')
p2 = ttk.Progressbar(w, mode='indeterminate')
globals().update(locals())
start = ttk.Button(w, text='Start Progress',
                   command=lambda: doBars('start', p1, p2))
stop = ttk.Button(w, text='Stop Progress',
                  command=lambda: doBars('stop', p1, p2))

##grid $w.p1 - -pady 5 -padx 10
##grid $w.p2 - -pady 5 -padx 10
##grid $w.start $w.stop -padx 10 -pady 5
##grid configure $w.start -sticky e
##grid configure $w.stop -sticky w
##grid columnconfigure $w all -weight 1
p1.grid(pady=5, padx=10, columnspan=2)
p2.grid(pady=5, padx=10, columnspan=2)
start.grid(padx=10, pady=5)
stop.grid(padx=10, pady=5, row=2, column=1)
start.grid_configure(sticky=E)
stop.grid_configure(sticky=W)
w.grid_columnconfigure('all', weight=1)
