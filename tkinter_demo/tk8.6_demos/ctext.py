# ctext.tcl --
#
# This demonstration script creates a canvas widget with a text
# item that can be edited and reconfigured in various ways.

##if {![info exists widgetDemo]} {
##    error "This script should be run from the \"widget\" demo."
##}
assert 'widgetDemo' in globals(), \
'This script should be run from the "widget" demo.'

##package require Tk

##set w .ctext
##catch {destroy $w}
##toplevel $w
##wm title $w "Canvas Text Demonstration"
##wm iconname $w "Text"
##positionWindow $w
##set c $w.c
demo_name = 'ctext'
if demo_name in globals()['demo_name']:
    globals()['demo_name'][demo_name].destroy()
w = globals()['demo_name'][demo_name] = Toplevel(root)
w.wm_title('Canvas Text Demonstration')
w.wm_iconname('Text')
positionWindow(w)

##label $w.msg -font $font -wraplength 5i -justify left -text "This window displays a string of text to demonstrate the text facilities of canvas widgets.  You can click in the boxes to adjust the position of the text relative to its positioning point or change its justification, and on a pie slice to change its angle.  The text also supports the following simple bindings for editing:
##  1. You can point, click, and type.
##  2. You can also select with button 1.
##  3. You can copy the selection to the mouse position with button 2.
##  4. Backspace and Control+h delete the selection if there is one;
##     otherwise they delete the character just before the insertion cursor.
##  5. Delete deletes the selection if there is one; otherwise it deletes
##     the character just after the insertion cursor."
##pack $w.msg -side top
msg = Label(w, font=font, wraplength='5i', justify='left', text="""This window displays a string of text to demonstrate the text facilities of canvas widgets.  You can click in the boxes to adjust the position of the text relative to its positioning point or change its justification, and on a pie slice to change its angle.  The text also supports the following simple bindings for editing:
  1. You can point, click, and type.
  2. You can also select with button 1.
  3. You can copy the selection to the mouse position with button 2.
  4. Backspace and Control+h delete the selection if there is one;
     otherwise they delete the character just before the insertion cursor.
  5. Delete deletes the selection if there is one; otherwise it deletes
     the character just after the insertion cursor.""")
msg.pack(side='top')

## See Code / Dismiss buttons
##set btns [addSeeDismiss $w.buttons $w]
##pack $btns -side bottom -fill x
btns = addSeeDismiss(ttk.Frame(w), demo_name)
btns.pack(side='bottom', fill='x')

##canvas $c -relief flat -borderwidth 0 -width 500 -height 350
##pack $w.c -side top -expand yes -fill both
c = Canvas(w, relief='flat', borderwidth='0', width='500', height='350')
c.pack(side='top', expand='yes', fill='both')

##set textFont {Helvetica 24}
##
##$c create rectangle 245 195 255 205 -outline black -fill red
##
### First, create the text item and give it bindings so it can be edited.
##
##$c addtag text withtag [$c create text 250 200 -text "This is just a string of text to demonstrate the text facilities of canvas widgets. Bindings have been been defined to support editing (see above)." -width 440 -anchor n -font $textFont -justify left]
##$c bind text <1> "textB1Press $c %x %y"
##$c bind text <B1-Motion> "textB1Move $c %x %y"
##$c bind text <Shift-1> "$c select adjust current @%x,%y"
##$c bind text <Shift-B1-Motion> "textB1Move $c %x %y"
##$c bind text <KeyPress> "textInsert $c %A"
##$c bind text <Return> "textInsert $c \\n"
##$c bind text <Control-h> "textBs $c"
##$c bind text <BackSpace> "textBs $c"
##$c bind text <Delete> "textDel $c"
##$c bind text <2> "textPaste $c @%x,%y"
textConfigFill = ''
def textEnter (w):
    global textConfigFill
    textConfigFill = w.itemconfig ('current', 'fill')[4]
    w.itemconfig ('current', fill='black')
#set textConfigFill {}
#proc textEnter {w} {
#    global textConfigFill
#    set textConfigFill [lindex [$w itemconfig current -fill] 4]
#    $w itemconfig current -fill black
#}
def textInsert(w, string):
    if string == '':
        return
    try:
        w.dchars('text', sel.first, sel.last)
    except:
        pass
    w.insert('text', 'insert', string)
#proc textInsert {w string} {
#    if {$string == ""} {
#	return
#    }
#    catch {$w dchars text sel.first sel.last}
#    $w insert text insert $string
#}
def textPaste(w, pos):
    try:
        w.insert('text', pos, w.selection_get())
    except:
        pass
#proc textPaste {w pos} {
#    catch {
#	$w insert text $pos [selection get]
#    }
#}
def textB1Press(w, x, y):
    w.icursor('current', '@%i,%i'%(x, y))
    w.focus('current')
    w.focus()
    w.select_from('current', '@%i,%i'%(x,y))
#proc textB1Press {w x y} {
#    $w icursor current @$x,$y
#    $w focus current
#    focus $w
#    $w select from current @$x,$y
#}
def textB1Move(w, x, y):
    w.select_to('current', '@%i,@i'%(x,y))
#proc textB1Move {w x y} {
#    $w select to current @$x,$y
#}
def textBs(w):
    try:
        w.dchars('text', sel.first, sel.last)
        return
    except:
        char = w.index('text', 'insert') - 1
        if char >= 0:
            w.dchar('text', char)
#proc textBs {w} {
#    if {![catch {$w dchars text sel.first sel.last}]} {
#	return
#    }
#    set char [expr {[$w index text insert] - 1}]
#    if {$char >= 0} {$w dchar text $char}
#}
def textDel(w):
    try:
        w.dchars('text', sel.first, sel.last)
        return
    except:
        w.dchars('text', 'insert')
#proc textDel {w} {
#    if {![catch {$w dchars text sel.first sel.last}]} {
#	return
#    }
#    $w dchars text insert
#}
textFont = 'Helvetica 24'
c.create_rectangle ('245 195 255 205', outline='black', fill='red')
c.addtag_withtag('text', c.create_text ('250 200', text="This is just a string of text to demonstrate the text facilities of canvas widgets. Bindings have been been defined to support editing (see above).", width='440', anchor='n', font=textFont, justify='left'))
globals().update(locals())
c.tag_bind ('text', '<1>', lambda e: textB1Press (c, e.x, e.y))
c.tag_bind ('text', '<B1-Motion>', lambda e: textB1Move (c, e.x, e.y))
c.tag_bind ('text', '<Shift-1>', lambda e: c.select_adjust ('current', '@%i,%i'%(e.x, e.y)))
c.tag_bind ('text', '<Shift-B1-Motion>', lambda e: textB1Move (c, e.x, e.y))
c.tag_bind ('text', '<KeyPress>', lambda e: textInsert (c, e.char))
c.tag_bind ('text', '<Return>', lambda e: textInsert (c, r'\n'))
c.tag_bind ('text', '<Control-h>', lambda e: textBs (c))
c.tag_bind ('text', '<BackSpace>', lambda e: textBs (c))
c.tag_bind ('text', '<Delete>', lambda e: textDel (c))
c.tag_bind ('text', '<2>', lambda e: textPaste (c, '@%i,%i'%(e.x, e.y)))

# Next, create some items that allow the text's anchor position
# to be edited.

##proc mkTextConfigBox {w x y option value color} {
##    set item [$w create rect $x $y [expr {$x+30}] [expr {$y+30}] \
##	    -outline black -fill $color -width 1]
##    $w bind $item <1> "$w itemconf text $option $value"
##    $w addtag config withtag $item
##}
##proc mkTextConfigPie {w x y a option value color} {
##    set item [$w create arc $x $y [expr {$x+90}] [expr {$y+90}] \
##	    -start [expr {$a-15}] -extent 30 -outline black -fill $color \
##	    -width 1]
##    $w bind $item <1> "$w itemconf text $option $value"
##    $w addtag config withtag $item
##}
def mkTextConfigBox(w, x, y, option, value, color):
    item = w.create_rectangle(x, y, x+30, y+30, outline='black',
                              fill=color, width=1)
    w.tag_bind(item, '<1>',
               lambda e: w.itemconfigure('text', {option: value}))
    w.addtag_withtag('config', item)
def mkTextConfigPie(w, x, y, a, option, value, color):
    item = w.create_arc(x, y, x+90, y+90, start=a-15, extent=30,
                        outline='black', fill=color, width=1)
    w.tag_bind(item, '<1>',
               lambda e: w.itemconfigure('text', {option: value}))
    w.addtag_withtag('config', item)

##set x 50
##set y 50
##set color LightSkyBlue1
##mkTextConfigBox $c $x $y -anchor se $color
##mkTextConfigBox $c [expr {$x+30}] [expr {$y   }] -anchor s      $color
##mkTextConfigBox $c [expr {$x+60}] [expr {$y   }] -anchor sw     $color
##mkTextConfigBox $c [expr {$x   }] [expr {$y+30}] -anchor e      $color
##mkTextConfigBox $c [expr {$x+30}] [expr {$y+30}] -anchor center $color
##mkTextConfigBox $c [expr {$x+60}] [expr {$y+30}] -anchor w      $color
##mkTextConfigBox $c [expr {$x   }] [expr {$y+60}] -anchor ne     $color
##mkTextConfigBox $c [expr {$x+30}] [expr {$y+60}] -anchor n      $color
##mkTextConfigBox $c [expr {$x+60}] [expr {$y+60}] -anchor nw     $color
##set item [$c create rect \
##	[expr {$x+40}] [expr {$y+40}] [expr {$x+50}] [expr {$y+50}] \
##	-outline black -fill red]
##$c bind $item <1> "$c itemconf text -anchor center"
##$c create text [expr {$x+45}] [expr {$y-5}] \
##	-text {Text Position}  -anchor s  -font {Times 20}  -fill brown
x = 50
y = 50
color = 'LightSkyBlue1'
mkTextConfigBox (c, x, y, 'anchor', 'se', color)
mkTextConfigBox (c, x+30, y   , 'anchor', 's',      color)
mkTextConfigBox (c, x+60, y   , 'anchor', 'sw',     color)
mkTextConfigBox (c, x   , y+30, 'anchor', 'e',      color)
mkTextConfigBox (c, x+30, y+30, 'anchor', 'center', color)
mkTextConfigBox (c, x+60, y+30, 'anchor', 'w',      color)
mkTextConfigBox (c, x   , y+60, 'anchor', 'ne',     color)
mkTextConfigBox (c, x+30, y+60, 'anchor', 'n',      color)
mkTextConfigBox (c, x+60, y+60, 'anchor', 'nw',     color)
item = c.create_rectangle(x+40, y+40, x+50, y+50,
        outline='black', fill='red')
c.tag_bind(item, '<1>', lambda e: c.itemconf('text', anchor='center'))
c.create_text(x+45, y-5,
        text='Text Position', anchor='s', font='Times 20', fill='brown')

# Now create some items that allow the text's angle to be changed.

##set x 205
##set y 50
##set color Yellow
##mkTextConfigPie $c $x $y   0 -angle  90 $color
##mkTextConfigPie $c $x $y  30 -angle 120 $color
##mkTextConfigPie $c $x $y  60 -angle 150 $color
##mkTextConfigPie $c $x $y  90 -angle 180 $color
##mkTextConfigPie $c $x $y 120 -angle 210 $color
##mkTextConfigPie $c $x $y 150 -angle 240 $color
##mkTextConfigPie $c $x $y 180 -angle 270 $color
##mkTextConfigPie $c $x $y 210 -angle 300 $color
##mkTextConfigPie $c $x $y 240 -angle 330 $color
##mkTextConfigPie $c $x $y 270 -angle   0 $color
##mkTextConfigPie $c $x $y 300 -angle  30 $color
##mkTextConfigPie $c $x $y 330 -angle  60 $color
##$c create text [expr {$x+45}] [expr {$y-5}] \
##	-text {Text Angle}  -anchor s  -font {Times 20}  -fill brown
x = 205
y = 50
color = 'Yellow'
mkTextConfigPie (c, x, y,   0, 'angle',  90, color)
mkTextConfigPie (c, x, y,  30, 'angle', 120, color)
mkTextConfigPie (c, x, y,  60, 'angle', 150, color)
mkTextConfigPie (c, x, y,  90, 'angle', 180, color)
mkTextConfigPie (c, x, y, 120, 'angle', 210, color)
mkTextConfigPie (c, x, y, 150, 'angle', 240, color)
mkTextConfigPie (c, x, y, 180, 'angle', 270, color)
mkTextConfigPie (c, x, y, 210, 'angle', 300, color)
mkTextConfigPie (c, x, y, 240, 'angle', 330, color)
mkTextConfigPie (c, x, y, 270, 'angle',   0, color)
mkTextConfigPie (c, x, y, 300, 'angle',  30, color)
mkTextConfigPie (c, x, y, 330, 'angle',  60, color)
c.create_text(x+45, y-5,
        text='Text Angle', anchor='s', font='Times 20', fill='brown')

# Lastly, create some items that allow the text's justification to be
# changed.

#set x 350
#set y 50
#set color SeaGreen2
#mkTextConfigBox $c $x $y -justify left $color
#mkTextConfigBox $c [expr {$x+30}] $y -justify center $color
#mkTextConfigBox $c [expr {$x+60}] $y -justify right $color
#$c create text [expr {$x+45}] [expr {$y-5}] \
#	-text {Justification}  -anchor s  -font {Times 20}  -fill brown
#
#$c bind config <Enter> "textEnter $c"
#$c bind config <Leave> "$c itemconf current -fill \$textConfigFill"
x = 350
y = 50
color = 'SeaGreen2'

mkTextConfigBox (c, x, y, 'justify', 'left', color)
mkTextConfigBox (c, x+30, y, 'justify', 'center', color)
mkTextConfigBox (c, x+60, y, 'justify', 'right', color)
c.create_text (x+45, y-5,
	text='Justification', anchor='s', font='Times 20', fill='brown')
c.tag_bind ('config', '<Enter>', lambda e: textEnter(c))
c.tag_bind ('config', '<Leave>',
            lambda e: c.itemconfigure('current', fill=textConfigFill))

##set textConfigFill {}
##
##proc textEnter {w} {
##    global textConfigFill
##    set textConfigFill [lindex [$w itemconfig current -fill] 4]
##    $w itemconfig current -fill black
##}
##
##proc textInsert {w string} {
##    if {$string == ""} {
##	return
##    }
##    catch {$w dchars text sel.first sel.last}
##    $w insert text insert $string
##}
##
##proc textPaste {w pos} {
##    catch {
##	$w insert text $pos [selection get]
##    }
##}
##
##proc textB1Press {w x y} {
##    $w icursor current @$x,$y
##    $w focus current
##    focus $w
##    $w select from current @$x,$y
##}
##
##proc textB1Move {w x y} {
##    $w select to current @$x,$y
##}
##
##proc textBs {w} {
##    if {![catch {$w dchars text sel.first sel.last}]} {
##	return
##    }
##    set char [expr {[$w index text insert] - 1}]
##    if {$char >= 0} {$w dchar text $char}
##}
##
##proc textDel {w} {
##    if {![catch {$w dchars text sel.first sel.last}]} {
##	return
##    }
##    $w dchars text insert
##}
