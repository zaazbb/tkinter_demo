# Copyright (C) 2008 Pat Thoyts <patthoyts@users.sourceforge.net>
#
#	Calculate a Knight's tour of a chessboard.
#
#	This uses Warnsdorff's rule to calculate the next square each
#	time. This specifies that the next square should be the one that
#	has the least number of available moves.
#
#	Using this rule it is possible to get to a position where
#	there are no squares available to move into. In this implementation
#	this occurs when the starting square is d6.
#
#	To solve this fault an enhancement to the rule is that if we
#	have a choice of squares with an equal score, we should choose
#	the one nearest the edge of the board.
#
#	If the call to the Edgemost function is commented out you can see
#	this occur.
#
#	You can drag the knight to a specific square to start if you wish.
#	If you let it repeat then it will choose random start positions
#	for each new tour.

##package require Tk 8.5

# Return a list of accessible squares from a given square
##proc ValidMoves {square} {
##    set moves {}
##    foreach pair {{-1 -2} {-2 -1} {-2 1} {-1 2} {1 2} {2 1} {2 -1} {1 -2}} {
##        set col [expr {($square % 8) + [lindex $pair 0]}]
##        set row [expr {($square / 8) + [lindex $pair 1]}]
##        if {$row > -1 && $row < 8 && $col > -1 && $col < 8} {
##            lappend moves [expr {$row * 8 + $col}]
##        }
##    }
##    return $moves
##}

# Return the number of available moves for this square
##proc CheckSquare {square} {
##    variable visited
##    set moves 0
##    foreach test [ValidMoves $square] {
##        if {[lsearch -exact -integer $visited $test] == -1} {
##            incr moves
##        }
##    }
##    return $moves
##}

# Select the next square to move to. Returns -1 if there are no available
# squares remaining that we can move to.
##proc Next {square} {
##    variable visited
##    set minimum 9
##    set nextSquare -1
##    foreach testSquare [ValidMoves $square] {
##        if {[lsearch -exact -integer $visited $testSquare] == -1} {
##            set count [CheckSquare $testSquare]
##            if {$count < $minimum} {
##                set minimum $count
##                set nextSquare $testSquare
##            } elseif {$count == $minimum} {
##                # to remove the enhancement to Warnsdorff's rule
##                # remove the next line:
##                set nextSquare [Edgemost $nextSquare $testSquare]
##            }
##        }
##    }
##    return $nextSquare
##}

# Select the square nearest the edge of the board
##proc Edgemost {a b} {
##    set colA [expr {3-int(abs(3.5-($a%8)))}]
##    set colB [expr {3-int(abs(3.5-($b%8)))}]
##    set rowA [expr {3-int(abs(3.5-($a/8)))}]
##    set rowB [expr {3-int(abs(3.5-($b/8)))}]
##    return [expr {($colA * $rowA) < ($colB * $rowB) ? $a : $b}]
##}

# Display a square number as a standard chess square notation.
##proc N {square} {
##    return [format %c%d [expr {97 + $square % 8}] \
##                [expr {$square / 8 + 1}]]
##}
def N(square):
    pass

# Perform a Knight's move and schedule the next move.
##proc MovePiece {dlg last square} {
##    variable visited
##    variable delay
##    variable continuous
##    $dlg.f.txt insert end "[llength $visited]. [N $last] .. [N $square]\n" {}
##    $dlg.f.txt see end
##    $dlg.f.c itemconfigure [expr {1+$last}] -state normal -outline black
##    $dlg.f.c itemconfigure [expr {1+$square}] -state normal -outline red
##    $dlg.f.c moveto knight {*}[lrange [$dlg.f.c coords [expr {1+$square}]] 0 1]
##    lappend visited $square
##    set next [Next $square]
##    if {$next ne -1} {
##        variable aid [after $delay [list MovePiece $dlg $square $next]]
##    } else {
##        $dlg.tf.b1 configure -state normal
##        if {[llength $visited] == 64} {
##            variable initial
##            if {$initial == $square} {
##                $dlg.f.txt insert end "Closed tour!"
##            } else {
##                $dlg.f.txt insert end "Success\n" {}
##                if {$continuous} {
##                    after [expr {$delay * 2}] [namespace code \
##                        [list Tour $dlg [expr {int(rand() * 64)}]]]
##                }
##            }
##        } else {
##            $dlg.f.txt insert end "FAILED!\n" {}
##        }
##    }
##}
def MovePiece(ws, last, square):
    global visited, delay, continuous
    txt, c, b1 = *ws
    txt.insert(END,
               str(len(visited))+'. '+str(N(last))+' .. '+str(N(square))+'\n')
    txt.see(END)
    c.itemconfigure(1+last, state='normal', outline='black')
    c.itemconfigure(1+square, state='normal', outline='red')
    c.moveto('knight', *c.coords(1+square)[:2])
    visited.append(square)
    next = Next(square)
    if next != -1:
        aid = c.after(delay, lambda: MovePiece(ws, square, next))
    else:
        b1['state'] = 'normal'
        if len(visited) == 64:
            global initial
            if initial == square:
                txt.insert(END, 'Closed tour!')
            else:
                txt.insert(END, 'Success\n')
                if continuous:
                    c.after(delay * 2,
                            lambda: Tour(ws, int(random.random() * 64)))
        else:
            txt.insert(END, 'FAILED!\n')

# Begin a new tour of the board given a random start position
##proc Tour {dlg {square {}}} {
##    variable visited {}
##    $dlg.f.txt delete 1.0 end
##    $dlg.tf.b1 configure -state disabled
##    for {set n 0} {$n < 64} {incr n} {
##        $dlg.f.c itemconfigure $n -state disabled -outline black
##    }
##    if {$square eq {}} {
##        set coords [lrange [$dlg.f.c coords knight] 0 1]
##        set square [expr {[$dlg.f.c find closest {*}$coords 0 65]-1}]
##    }
##    variable initial $square
##    after idle [list MovePiece $dlg $initial $initial]
##}
def Tour(ws, square=None):
    global visited
    visited = []
    txt, c, b1 = *ws
    txt.delete(1.0, END)
    b1['state'] = 'disabled'
    for n in range(64):
        c.itemconfigure(state='disabled', outline='black')
    if square == None:
        coords = c.coords('knight')[:2]
        square = c.find_closest(*coords, 0, 65) - 1
    initial = square
    c.after_idle(lambda: MovePiece(ws, initial, initial))

##proc Stop {} {
##    variable aid
##    catch {after cancel $aid}
##}
def Stop(dlg):
    global aid
    try:
        dlg.after_cancel(aid)
    except:
        pass

##proc Exit {dlg} {
##    Stop
##    destroy $dlg
##}
def Exit(dlg):
    Stop(dlg)
    dlg.destroy()

##proc SetDelay {new} {
##    variable delay [expr {int($new)}]
##}
def SetDelay(new):
    global delay
    delay.set(new)

##proc DragStart {w x y} {
##    $w dtag selected
##    $w addtag selected withtag current
##    variable dragging [list $x $y]
##}
##proc DragMotion {w x y} {
##    variable dragging
##    if {[info exists dragging]} {
##        $w move selected [expr {$x - [lindex $dragging 0]}] \
##            [expr {$y - [lindex $dragging 1]}]
##        variable dragging [list $x $y]
##    }
##}
##proc DragEnd {w x y} {
##    set square [$w find closest $x $y 0 65]
##    $w moveto selected {*}[lrange [$w coords $square] 0 1]
##    $w dtag selected
##    variable dragging ; unset dragging
##}

##proc CreateGUI {} {
##    catch {destroy .knightstour}
##    set dlg [toplevel .knightstour]
##    wm title $dlg "Knights tour"
##    wm withdraw $dlg
##    set f [ttk::frame $dlg.f]
##    set c [canvas $f.c -width 240 -height 240]
##    text $f.txt -width 10 -height 1 -background white \
##        -yscrollcommand [list $f.vs set] -font {Arial 8}
##    ttk::scrollbar $f.vs -command [list $f.txt yview]
##
##    variable delay 600
##    variable continuous 0
##    ttk::frame $dlg.tf
##    ttk::label $dlg.tf.ls -text Speed
##    ttk::scale $dlg.tf.sc  -from 8 -to 2000 -command [list SetDelay] \
##        -variable [namespace which -variable delay]
##    ttk::checkbutton $dlg.tf.cc -text Repeat \
##        -variable [namespace which -variable continuous]
##    ttk::button $dlg.tf.b1 -text Start -command [list Tour $dlg]
##    ttk::button $dlg.tf.b2 -text Exit -command [list Exit $dlg]
##    set square 0
##    for {set row 7} {$row != -1} {incr row -1} {
##        for {set col 0} {$col < 8} {incr col} {
##            if {(($col & 1) ^ ($row & 1))} {
##                set fill tan3 ; set dfill tan4
##            } else {
##                set fill bisque ; set dfill bisque3
##            }
##            set coords [list [expr {$col * 30 + 4}] [expr {$row * 30 + 4}] \
##                            [expr {$col * 30 + 30}] [expr {$row * 30 + 30}]]
##            $c create rectangle $coords -fill $fill -disabledfill $dfill \
##                -width 2 -state disabled
##        }
##    }
##    if {[tk windowingsystem] ne "x11"} {
##        catch {eval font create KnightFont -size -24}
##        $c create text 0 0 -font KnightFont -text "\u265e" \
##            -anchor nw -tags knight -fill black -activefill "#600000"
##    } else {
##        # On X11 we cannot reliably tell if the \u265e glyph is available
##        # so just use a polygon
##        set pts {
##            2 25   24 25  21 19   20 8   14 0   10 0   0 13   0 16
##            2 17    4 14   5 15    3 17   5 17   9 14  10 15  5 21
##        }
##        $c create polygon $pts -tag knight -offset 8 \
##            -fill black -activefill "#600000"
##    }
##    $c moveto knight {*}[lrange [$c coords [expr {1 + int(rand() * 64)}]] 0 1]
##    $c bind knight <ButtonPress-1> [namespace code [list DragStart %W %x %y]]
##    $c bind knight <Motion> [namespace code [list DragMotion %W %x %y]]
##    $c bind knight <ButtonRelease-1> [namespace code [list DragEnd %W %x %y]]
##    
##    grid $c $f.txt $f.vs  -sticky news
##    grid rowconfigure    $f 0 -weight 1
##    grid columnconfigure $f 1 -weight 1
##
##    grid $f - - - - - -sticky news
##    set things [list $dlg.tf.ls $dlg.tf.sc $dlg.tf.cc $dlg.tf.b1]
##    if {![info exists ::widgetDemo]} {
##	lappend things $dlg.tf.b2
##	if {[tk windowingsystem] ne "aqua"} {
##	    set things [linsert $things 0 [ttk::sizegrip $dlg.tf.sg]]
##	}
##    }
##    pack {*}$things -side right
##    if {[tk windowingsystem] eq "aqua"} {
##	pack configure {*}$things -padx {4 4} -pady {12 12}
##	pack configure [lindex $things 0] -padx {4 24}
##	pack configure [lindex $things end] -padx {16 4}
##    }
##    grid $dlg.tf  - - - - - -sticky ew
##    if {[info exists ::widgetDemo]} {
##        grid [addSeeDismiss $dlg.buttons $dlg] - - - - - -sticky ew
##    }
##    
##    grid rowconfigure $dlg 0 -weight 1
##    grid columnconfigure $dlg 0 -weight 1
##
##    bind $dlg <Control-F2> {console show}
##    bind $dlg <Return> [list $dlg.tf.b1 invoke]
##    bind $dlg <Escape> [list $dlg.tf.b2 invoke]
##    bind $dlg <Destroy> [namespace code [list Stop]]
##    wm protocol $dlg WM_DELETE_WINDOW [namespace code [list Exit $dlg]]
##
##    wm deiconify $dlg
##    tkwait window $dlg
##}

##if {![winfo exists .knightstour]} {
##    if {![info exists widgetDemo]} { wm withdraw . }
##    set r [catch [linsert $argv 0 CreateGUI] err]
##    if {$r} {
##	tk_messageBox -icon error -title "Error" -message $err
##    }
##    if {![info exists widgetDemo]} { exit $r }
##}
def CreateGUI():
    import random

    class MyCavas(Canvas):
        def moveto(self, tagOrId, xPos, yPos):
            self.tk.call(self._w, 'moveto', tagOrId, xPos, yPos)
    
    try:
        knightstour.destroy()
    except:
        pass
    dlg = knightstour = Toplevel(root)
    dlg.wm_title('Knights tour')
    dlg.wm_withdraw()
    f = ttk.Frame(dlg)
    c = MyCavas(f, width=240, height=240)
    txt = Text(f, width=10, height=1, background='white', font='Arial 8')
    vs = ttk.Scrollbar(f, command=txt.yview)
    txt['yscrollcommand'] = vs.set

    global delay
    delay = IntVar(value=600)
    continuous = IntVar(value=0)
    tf = ttk.Frame(dlg)
    ls = ttk.Label(tf, text='Speed')
    sc = ttk.Scale(tf, from_=8, to=2000, command=SetDelay, variable=delay)
    cc = ttk.Checkbutton(tf, text='Repeat', variable=continuous)
    b1 = ttk.Button(tf, text='Start', command=lambda: Tour((txt, c, b1)))
    b2 = ttk.Button(tf, text='Exit', command=lambda: Exit(dlg))
    square = 0
    for row in range(7, -1, -1):
        for col in range(8):
            if (col & 1) ^ (row & 1):
                fill = 'tan3'
                dfill = 'tan4'
            else:
                fill = 'bisque'
                dfill = 'bisque3'
            coords = (col * 30 + 4, row * 30 + 4, col * 30 + 30, row * 30 + 30)
            c.create_rectangle(coords, fill=fill, disabledfill=dfill,
                               width=2, state='disabled')
    if dlg._windowingsystem != 'x11':
        try:
            knightFont = Font(size=-24)
        except:
            pass
        c.create_text(0, 0, font=knightFont, text='\u265e', anchor='nw',
                      tags='knight', fill='black', activefill='#600000')
    else:
        pts = ('2 25   24 25  21 19   20 8   14 0   10 0   0 13   0 16 '
               '2 17    4 14   5 15    3 17   5 17   9 14  10 15  5 21')
        c.create_polygon(pts, tag='knight', offset=8,
                         fill='black', activefill='#600000')
    c.moveto('knight', *c.coords(int(1 + random.random() * 64))[:2]) 
    c.tag_bind('knight', '<ButtonPress-1>',
               lambda e: DragStart(e.widget, e.x, e.y))
    c.tag_bind('knight', '<Motion>', lambda e: DragMotion(e.widget, e.x, e.y))
    c.tag_bind('knight', '<ButtonRelease-1>',
               lambda e: DragEnd(e.widget, e.x, e.y))

    for i, w in enumerate((c, txt, vs)):
        w.grid(sticky='news', column=i, row=0)
    f.grid_rowconfigure(0, weight=1)
    f.grid_columnconfigure(1, weight=1)

    f.grid(sticky='news', columnspan=6)
    things = [ls, sc, cc, b1]
    if 'widgetDemo' not in globals():
        things.append(b2)
    if dlg._windowingsystem != 'aqua':
        sg = ttk.Sizegrip(tf)
        things.insert(0, sg)
    for w in things:
        w.pack(side=RIGHT)
    if dlg._windowingsystem == 'aque':
        for w in things:
            w.pack_configure(padx=(4, 4), pady=(12, 12))
        thing[0].pack_configure(padx=(4, 24))
        things[-1].pack_configure(padx=(16, 4))
    tf.grid(sticky='ew', columnspan=6)
    if 'widgetDemo' in globals():
        addSeeDismiss(ttk.Frame(w), demo_name).grid(sticky='ew', columnspan=6)

    dlg.grid_rowconfigure(0, weight=1)
    dlg.grid_columnconfigure(0, weight=1)

    dlg.bind('<Control-F2>', lambda e: sys.system('idle'))
    dlg.bind('<Return>', lambda e: b1.invoke())
    dlg.bind('<Escape>', lambda e: b2.invoke())
    dlg.bind('<Destroy>', lambda e: Stop(dlg))
    dlg.wm_protocol('WM_DELETE_WINDOW', lambda: Exit(dlg))

    dlg.wm_deiconify()
    dlg.wait_window()
    
if 'knightstour' not in globals() \
        or not globals()['knightstour'].winfo_exists():
    from tkinter import *
    from tkinter import ttk
    from tkinter.font import Font
    if 'widgetDemo' not in globals():
        root = Tk()
        root.wm_withdraw()
    try:
        CreateGUI()
    except:
        from tkinter.messagebox import showerror
        import traceback
        showerror(title='Error', message=traceback.format_exc())
