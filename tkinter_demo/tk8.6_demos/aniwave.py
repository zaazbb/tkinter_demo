# aniwave.tcl --
#
# This demonstration script illustrates how to adjust canvas item
# coordinates in a way that does something fairly similar to waveform
# display.

##if {![info exists widgetDemo]} {
##    error "This script should be run from the \"widget\" demo."
##}
assert 'widgetDemo' in globals(), \
'This script should be run from the "widget" demo.'

##package require Tk

##set w .aniwave
##catch {destroy $w}
##toplevel $w
##wm title $w "Animated Wave Demonstration"
##wm iconname $w "aniwave"
##positionWindow $w
demo_name = 'aniwave'
if demo_name in globals():
    globals()[demo_name].destroy()
w = globals()[demo_name] = Toplevel(root)
w.wm_title('Animated Wave Demonstration')
w.wm_iconname('aniwave')
positionWindow(w)

##label $w.msg -font $font -wraplength 4i -justify left -text "This demonstration contains a canvas widget with a line item inside it. The animation routines work by adjusting the coordinates list of the line; a trace on a variable is used so updates to the variable result in a change of position of the line." 
##pack $w.msg -side top
msg = Label(w, font=font, wraplength='4i', justify=LEFT, text="This demonstration contains a canvas widget with a line item inside it. The animation routines work by adjusting the coordinates list of the line; a trace on a variable is used so updates to the variable result in a change of position of the line." )
msg.pack(side=TOP)

## See Code / Dismiss buttons
##set btns [addSeeDismiss $w.buttons $w]
##pack $btns -side bottom -fill x
btns = addSeeDismiss(ttk.Frame(w), demo_name)
btns.pack(side=BOTTOM, fill=X)

# Create a canvas large enough to hold the wave. In fact, the wave
# sticks off both sides of the canvas to prevent visual glitches.
##pack [canvas $w.c -width 300 -height 200 -background black] -padx 10 -pady 10 -expand yes
c = Canvas(w, width=300, height=200, background='black')
c.pack(padx=10, pady=10, expand=YES)

# Ensure that this this is an array
##array set animationCallbacks {}
animationCallbacks = {}

# Creates a coordinates list of a wave. This code does a very sketchy
# job and relies on Tk's line smoothing to make things look better.
##set waveCoords {}
##for {set x -10} {$x<=300} {incr x 5} {
##    lappend waveCoords $x 100
##}
##lappend waveCoords $x 0 [incr x 5] 200
class ListVar(StringVar, list):
    def __init__(self, master=None, value=[], name=None):
        list.__init__(value)
        super().__init__(master, str(self), name)

    def __str__(self):
        return ' '.join([str(i) for i in self])

    def __iadd__(self, b):
        super().__iadd__(b)
        super().set(str(self))
        return self

    def __setitem__(self, b, c):
        super().__setitem__(b, c)
        super().set(str(self))

    def set(self, value):
        list.__init__(value)
        super().set(str(self))

    def get(self):
        return [int(i) for i in super().get().split()]
waveCoords = ListVar()
for x in range(-10, 301, 5):
    waveCoords += [x, 100]
waveCoords += [x, 0, x+5, 200]

# Create a smoothed line and arrange for its coordinates to be the
# contents of the variable waveCoords.
##$w.c create line $waveCoords -tags wave -width 1 -fill green -smooth 1
##proc waveCoordsTracer {w args} {
##    global waveCoords
##    # Actual visual update will wait until we have finished
##    # processing; Tk does that for us automatically.
##    $w.c coords wave $waveCoords
##}
##trace add variable waveCoords write [list waveCoordsTracer $w]
c.create_line(waveCoords.get(), tags='wave', width=1, fill='green', smooth=1)
def waveCoordsTracer(w):
    global waveCoords
    c.coords('wave', waveCoords.get())
waveCoords.trace_variable('w', lambda *args: waveCoordsTracer(w))

# Basic motion handler. Given what direction the wave is travelling
# in, it advances the y coordinates in the coordinate-list one step in
# that direction.
##proc basicMotion {} {
##    global waveCoords direction
##    set oc $waveCoords
##    for {set i 1} {$i<[llength $oc]} {incr i 2} {
##	if {$direction eq "left"} {
##	    lset waveCoords $i [lindex $oc \
##		    [expr {$i+2>[llength $oc] ? 1 : $i+2}]]
##	} else {
##	    lset waveCoords $i \
##		    [lindex $oc [expr {$i-2<0 ? "end" : $i-2}]]
##	}
##    }
##}
def basicMotion():
    global waveCoords, direction
    oc = waveCoords.get()
    for i in range(1, len(oc), 2):
        if direction == 'left':
            waveCoords[i] = oc[1 if i+2 > len(oc) else i+2]
        else:
            waveCoords[i] = oc[-1 if i-2 < 0 else i-2]

# Oscillation handler. This detects whether to reverse the direction
# of the wave by checking to see if the peak of the wave has moved off
# the screen (whose size we know already.)
##proc reverser {} {
##    global waveCoords direction
##    if {[lindex $waveCoords 1] < 10} {
##	set direction "right"
##    } elseif {[lindex $waveCoords end] < 10} {
##	set direction "left"
##    }
##}
def reverser():
    global waveCoords, direction
    if waveCoords[1] < 10:
        direction = 'right'
    elif waveCoords[-1] < 10:
        direction = 'left'

# Main animation "loop". This calls the two procedures that handle the
# movement repeatedly by scheduling asynchronous calls back to itself
# using the [after] command. This procedure is the fundamental basis
# for all animated effect handling in Tk.
##proc move {} {
##    basicMotion
##    reverser
##
##    # Theoretically 100 frames-per-second (==10ms between frames)
##    global animationCallbacks
##    set animationCallbacks(simpleWave) [after 10 move]
##}
def move():
    basicMotion()
    reverser()
    global animationCallbacks
    animationCallbacks['simpleWave'] = c.after(10, move)

### Initialise our remaining animation variables
##set direction "left"
##set animateAfterCallback {}
### Arrange for the animation loop to stop when the canvas is deleted
##bind $w.c <Destroy> {
##    after cancel $animationCallbacks(simpleWave)
##    unset animationCallbacks(simpleWave)
##}
### Start the animation processing
##move
direction = 'left'
animateAfterCallback = {}
def destroy_callback(e):
    c.after_cancel(animationCallbacks['simpleWave'])
    del animationCallbacks['simpleWave']
c.bind('<Destroy>', destroy_callback)
globals().update(locals())
move()

