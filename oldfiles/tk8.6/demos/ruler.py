# ruler.tcl --
#
# This demonstration script creates a canvas widget that displays a ruler
# with tab stops that can be set, moved, and deleted.

##if {![info exists widgetDemo]} {
##    error "This script should be run from the \"widget\" demo."
##}
assert 'widgetDemo' in globals(), \
'This script should be run from the "widget" demo.'

##package require Tk

# rulerMkTab --
# This procedure creates a new triangular polygon in a canvas to
# represent a tab stop.
#
# Arguments:
# c -		The canvas window.
# x, y -	Coordinates at which to create the tab stop.

##proc rulerMkTab {c x y} {
##    upvar #0 demo_rulerInfo v
##    $c create polygon $x $y [expr {$x+$v(size)}] [expr {$y+$v(size)}] \
##	    [expr {$x-$v(size)}] [expr {$y+$v(size)}]
##}
def rulerMkTab(c, x, y):
    global demo_rulerInfo
    size = demo_rulerInfo['size']
    return c.create_polygon(x, y, x+size, y+size, x-size, y+size)
    
##set w .ruler
##catch {destroy $w}
##toplevel $w
##wm title $w "Ruler Demonstration"
##wm iconname $w "ruler"
##positionWindow $w
##set c $w.c
demo_name = 'ruler'
if demo_name in globals()['demo_name']:
    globals()['demo_name'][demo_name].destroy()
w = globals()['demo_name'][demo_name] = Toplevel(root)
w.wm_title('Ruler Demonstration')
w.wm_iconname('ruler')
positionWindow(w)

##label $w.msg -font $font -wraplength 5i -justify left -text "This canvas widget shows a mock-up of a ruler.  You can create tab stops by dragging them out of the well to the right of the ruler.  You can also drag existing tab stops.  If you drag a tab stop far enough up or down so that it turns dim, it will be deleted when you release the mouse button."
##pack $w.msg -side top
msg = Label(w, font=font, wraplength='5i', justify=LEFT, text="This canvas widget shows a mock-up of a ruler.  You can create tab stops by dragging them out of the well to the right of the ruler.  You can also drag existing tab stops.  If you drag a tab stop far enough up or down so that it turns dim, it will be deleted when you release the mouse button.")
msg.pack(side=TOP)

## See Code / Dismiss buttons
##set btns [addSeeDismiss $w.buttons $w]
##pack $btns -side bottom -fill x
btns = addSeeDismiss(ttk.Frame(w), demo_name)
btns.pack(side=BOTTOM, fill=X)

##canvas $c -width 14.8c -height 2.5c
##pack $w.c -side top -fill x
c = Canvas(w, width='14.8c', height='2.5c')
c.pack(side=TOP, fill=X)

##set demo_rulerInfo(grid) .25c
##set demo_rulerInfo(left) [winfo fpixels $c 1c]
##set demo_rulerInfo(right) [winfo fpixels $c 13c]
##set demo_rulerInfo(top) [winfo fpixels $c 1c]
##set demo_rulerInfo(bottom) [winfo fpixels $c 1.5c]
##set demo_rulerInfo(size) [winfo fpixels $c .2c]
##set demo_rulerInfo(normalStyle) "-fill black"
### Main widget program sets variable tk_demoDirectory
##if {[winfo depth $c] > 1} {
##    set demo_rulerInfo(activeStyle) "-fill red -stipple {}"
##    set demo_rulerInfo(deleteStyle) [list -fill red \
##	    -stipple @[file join $tk_demoDirectory images gray25.xbm]]
##} else {
##    set demo_rulerInfo(activeStyle) "-fill black -stipple {}"
##    set demo_rulerInfo(deleteStyle) [list -fill black \
##	    -stipple @[file join $tk_demoDirectory images gray25.xbm]]
##}
demo_rulerInfo = dict(grid='.25c',
                      left=c.winfo_fpixels('1c'),
                      right=c.winfo_fpixels('13c'),
                      top=c.winfo_fpixels('1c'),
                      bottom=c.winfo_fpixels('1.5c'),
                      size=c.winfo_fpixels('.2c'),
                      normalStyle=dict(fill='black'))
if c.winfo_depth() > 1:
    demo_rulerInfo['activeStyle'] = dict(fill='red', stipple='')
    demo_rulerInfo['deleteStyle'] = \
        dict(fill='red', stipple='@'+tk_demoDirectory+'/images/gray25.xbm')
else:
    demo_rulerInfo['activeStyle'] = dict(fill='black', stipple='')
    demo_rulerInfo['deleteStyle'] = \
        dict(fill='black', stipple='@'+tk_demoDirectory+'/images/gray25.xbm')

##$c create line 1c 0.5c 1c 1c 13c 1c 13c 0.5c -width 1
##for {set i 0} {$i < 12} {incr i} {
##    set x [expr {$i+1}]
##    $c create line ${x}c 1c ${x}c 0.6c -width 1
##    $c create line $x.25c 1c $x.25c 0.8c -width 1
##    $c create line $x.5c 1c $x.5c 0.7c -width 1
##    $c create line $x.75c 1c $x.75c 0.8c -width 1
##    $c create text $x.15c .75c -text $i -anchor sw
##}
##$c addtag well withtag [$c create rect 13.2c 1c 13.8c 0.5c \
##	-outline black -fill [lindex [$c config -bg] 4]]
##$c addtag well withtag [rulerMkTab $c [winfo pixels $c 13.5c] \
##	[winfo pixels $c .65c]]
c.create_line('1c 0.5c 1c 1c 13c 1c 13c 0.5c', width=1)
for i in range(12):
    x = str(i+1)
    c.create_line(x+'c', '1c', x+'c', '0.6c', width=1)
    c.create_line(x+'.25c', '1c', x+'.25c', '0.8c', width=1)
    c.create_line(x+'.5c', '1c', x+'.5c', '0.7c', width=1)
    c.create_line(x+'.75c', '1c', x+'.75c', '0.8c', width=1)
    c.create_text(x+'.15c', '.75c', text=i, anchor='sw')
c.addtag_withtag('well',
                 c.create_rectangle('13.2c 1c 13.8c 0.5c',
                                    outline='black', fill=c.configure('bg')[4]))
c.addtag_withtag('well',
                 rulerMkTab(c, c.winfo_pixels('13.5c'), c.winfo_pixels('.65c')))

##$c bind well <1> "rulerNewTab $c %x %y"
##$c bind tab <1> "rulerSelectTab $c %x %y"
##bind $c <B1-Motion> "rulerMoveTab $c %x %y"
##bind $c <Any-ButtonRelease-1> "rulerReleaseTab $c"
def rulerNewTab(c, x, y):
    global demo_rulerInfo
    c.addtag_withtag('active', rulerMkTab(c, x, y))
    c.addtag_withtag('tab', 'active')
    demo_rulerInfo['x'] = x
    demo_rulerInfo['y'] = y
    rulerMoveTab(c, x, y)
##proc rulerNewTab {c x y} {
##    upvar #0 demo_rulerInfo v
##    $c addtag active withtag [rulerMkTab $c $x $y]
##    $c addtag tab withtag active
##    set v(x) $x
##    set v(y) $y
##    rulerMoveTab $c $x $y
##}
def rulerSelectTab(c, x, y):
    global demo_rulerInfo
    grid = demo_rulerInfo['grid']
    top = demo_rulerInfo['top']
    activeStyle = demo_rulerInfo['activeStyle']
    
    demo_rulerInfo['x'] = c.canvasx(x, grid)
    demo_rulerInfo['y'] = top + 2
    c.addtag_withtag('active', 'current')
    c.itemconfigure('active', **activeStyle)
    c.tkraise('active')
##proc rulerSelectTab {c x y} {
##    upvar #0 demo_rulerInfo v
##    set v(x) [$c canvasx $x $v(grid)]
##    set v(y) [expr {$v(top)+2}]
##    $c addtag active withtag current
##    eval "$c itemconf active $v(activeStyle)"
##    $c raise active
##}
def rulerMoveTab(c, x, y):    
    if c.find_withtag('active'):
        global demo_rulerInfo
        grid = demo_rulerInfo['grid']
        left = demo_rulerInfo['left']
        right = demo_rulerInfo['right']
        top = demo_rulerInfo['top']
        bottom = demo_rulerInfo['bottom']
        size = demo_rulerInfo['size']
        activeStyle = demo_rulerInfo['activeStyle']
        deleteStyle = demo_rulerInfo['deleteStyle']
        x_ = demo_rulerInfo['x']
        y_ = demo_rulerInfo['y']
        
        cx = c.canvasx(x, grid)
        cy = c.canvasy(y)
        if cx < left:
            cx = left
        if cx > right:
            cx = right
        if cy >= top and cy <= bottom:
            cy = top + 2
            c.itemconfigure('active', **activeStyle)
        else:
            cy = cy - size - 2
            c.itemconfigure('active', **deleteStyle)
        c.move('active', cx-x_, cy-y_)
        demo_rulerInfo['x'] = cx
        demo_rulerInfo['y'] = cy
##proc rulerMoveTab {c x y} {
##    upvar #0 demo_rulerInfo v
##    if {[$c find withtag active] == ""} {
##	return
##    }
##    set cx [$c canvasx $x $v(grid)]
##    set cy [$c canvasy $y]
##    if {$cx < $v(left)} {
##	set cx $v(left)
##    }
##    if {$cx > $v(right)} {
##	set cx $v(right)
##    }
##    if {($cy >= $v(top)) && ($cy <= $v(bottom))} {
##	set cy [expr {$v(top)+2}]
##	eval "$c itemconf active $v(activeStyle)"
##    } else {
##	set cy [expr {$cy-$v(size)-2}]
##	eval "$c itemconf active $v(deleteStyle)"
##    }
##    $c move active [expr {$cx-$v(x)}] [expr {$cy-$v(y)}]
##    set v(x) $cx
##    set v(y) $cy
##}
def rulerReleaseTab(c):
    if c.find_withtag('active'):
        global demo_rulerInfo
        y = demo_rulerInfo['y']
        top = demo_rulerInfo['top']
        normalStyle = demo_rulerInfo['normalStyle']
        
        if y != top+2:
            c.delete('active')
        else:
            c.itemconfigure('active', **normalStyle)
            c.dtag('active')
##proc rulerReleaseTab c {
##    upvar #0 demo_rulerInfo v
##    if {[$c find withtag active] == {}} {
##	return
##    }
##    if {$v(y) != $v(top)+2} {
##	$c delete active
##    } else {
##	eval "$c itemconf active $v(normalStyle)"
##	$c dtag active
##    }
##}
globals().update(locals())
c.tag_bind('well', '<1>', lambda e: rulerNewTab(c, e.x, e.y))
c.tag_bind('tab', '<1>', lambda e: rulerSelectTab(c, e.x, e.y))
c.bind('<B1-Motion>', lambda e: rulerMoveTab(c, e.x, e.y))
c.bind('<Any-ButtonRelease-1>', lambda e: rulerReleaseTab(c))

# rulerNewTab --
# Does all the work of creating a tab stop, including creating the
# triangle object and adding tags to it to give it tab behavior.
#
# Arguments:
# c -		The canvas window.
# x, y -	The coordinates of the tab stop.

##proc rulerNewTab {c x y} {
##    upvar #0 demo_rulerInfo v
##    $c addtag active withtag [rulerMkTab $c $x $y]
##    $c addtag tab withtag active
##    set v(x) $x
##    set v(y) $y
##    rulerMoveTab $c $x $y
##}

# rulerSelectTab --
# This procedure is invoked when mouse button 1 is pressed over
# a tab.  It remembers information about the tab so that it can
# be dragged interactively.
#
# Arguments:
# c -		The canvas widget.
# x, y -	The coordinates of the mouse (identifies the point by
#		which the tab was picked up for dragging).

##proc rulerSelectTab {c x y} {
##    upvar #0 demo_rulerInfo v
##    set v(x) [$c canvasx $x $v(grid)]
##    set v(y) [expr {$v(top)+2}]
##    $c addtag active withtag current
##    eval "$c itemconf active $v(activeStyle)"
##    $c raise active
##}

# rulerMoveTab --
# This procedure is invoked during mouse motion events to drag a tab.
# It adjusts the position of the tab, and changes its appearance if
# it is about to be dragged out of the ruler.
#
# Arguments:
# c -		The canvas widget.
# x, y -	The coordinates of the mouse.

##proc rulerMoveTab {c x y} {
##    upvar #0 demo_rulerInfo v
##    if {[$c find withtag active] == ""} {
##	return
##    }
##    set cx [$c canvasx $x $v(grid)]
##    set cy [$c canvasy $y]
##    if {$cx < $v(left)} {
##	set cx $v(left)
##    }
##    if {$cx > $v(right)} {
##	set cx $v(right)
##    }
##    if {($cy >= $v(top)) && ($cy <= $v(bottom))} {
##	set cy [expr {$v(top)+2}]
##	eval "$c itemconf active $v(activeStyle)"
##    } else {
##	set cy [expr {$cy-$v(size)-2}]
##	eval "$c itemconf active $v(deleteStyle)"
##    }
##    $c move active [expr {$cx-$v(x)}] [expr {$cy-$v(y)}]
##    set v(x) $cx
##    set v(y) $cy
##}

# rulerReleaseTab --
# This procedure is invoked during button release events that end
# a tab drag operation.  It deselects the tab and deletes the tab if
# it was dragged out of the ruler.
#
# Arguments:
# c -		The canvas widget.
# x, y -	The coordinates of the mouse.

##proc rulerReleaseTab c {
##    upvar #0 demo_rulerInfo v
##    if {[$c find withtag active] == {}} {
##	return
##    }
##    if {$v(y) != $v(top)+2} {
##	$c delete active
##    } else {
##	eval "$c itemconf active $v(normalStyle)"
##	$c dtag active
##    }
##}
