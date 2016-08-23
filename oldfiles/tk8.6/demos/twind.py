# twind.tcl --
#
# This demonstration script creates a text widget with a bunch of
# embedded windows.

##if {![info exists widgetDemo]} {
##    error "This script should be run from the \"widget\" demo."
##}
assert 'widgetDemo' in globals(), \
'This script should be run from the "widget" demo.'

##package require Tk
from tkinter import *

##set w .twind
##catch {destroy $w}
##toplevel $w
##wm title $w "Text Demonstration - Embedded Windows and Other Features"
##wm iconname $w "Embedded Windows"
##positionWindow $w
demo_name = 'twind'
if demo_name in globals()['demo_name']:
    globals()['demo_name'][demo_name].destroy()
w = globals()['demo_name'][demo_name] = Toplevel(root)
w.wm_title('Text Demonstration - Embedded Windows and Other Features')
w.wm_iconname('Embedded Windows')
positionWindow(w)

## See Code / Dismiss buttons
##set btns [addSeeDismiss $w.buttons $w]
##pack $btns -side bottom -fill x
buttons = ttk.Frame(w)
btns = addSeeDismiss(buttons, demo_name)
btns.pack(side='bottom', fill='x')

##frame $w.f -highlightthickness 1 -borderwidth 1 -relief sunken
##set t $w.f.text
##text $t -yscrollcommand "$w.scroll set" - true -font $font -width 70 \
##	-height 35 -wrap word -highlightthickness 0 -borderwidth 0
##pack $t -expand  yes -fill both
##scrollbar $w.scroll -command "$t yview"
##pack $w.scroll -side right -fill y
##panedwindow $w.pane
##pack $w.pane -expand yes -fill both
##$w.pane add $w.f
### Import to raise given creation order above
##raise $w.f
f = Frame(w, highlightthickness=1, borderwidth=1, relief='sunken')
text = Text(f, setgrid=True, font=font_, width=70,
            height=35, wrap='word', highlightthickness=0, borderwidth=0)
scroll = Scrollbar(w, command=text.yview)
text['yscrollcommand'] = scroll.set
scroll.pack(side='right', fill='y')
text.pack(expand='yes', fill='both')
pane = PanedWindow(w)
pane.pack(expand='yes', fill='both')
pane.add(f)
# Import to raise given creation order above
f.tkraise()

##$t tag configure center -justify center -spacing1 5m -spacing3 5m
##$t tag configure buttons -lmargin1 1c -lmargin2 1c -rmargin 1c \
##	-spacing1 3m -spacing2 0 -spacing3 0
text.tag_configure('center', justify='center', spacing1='5m', spacing3='5m')
text.tag_configure('buttons', lmargin1='1c', lmargin2='1c', rmargin='1c',
                   spacing1='3m', spacing2=0, spacing3=0)

##button $t.on -text "Turn On" -command "textWindOn $w" \
##	-cursor top_left_arrow
##button $t.off -text "Turn Off" -command "textWindOff $w" \
##	-cursor top_left_arrow
def textWindOn():
    from tkinter import Scrollbar
    global w, text, buttons
    global scroll2
    try:
        scroll2.destroy()
    except:
        pass
    scroll2 = Scrollbar(w, orient='horizontal', command=text.xview)
    scroll2.pack(after=buttons, side='bottom', fill='x')
    text.configure(xscrollcommand=scroll2.set, wrap='none')
def textWindOff():
    global text
    global scroll2
    try:
        scroll2.destroy()
    except:
        pass
    text.configure(xscrollcommand='', wrap='word')
##proc textWindOn w {
##    catch {destroy $w.scroll2}
##    set t $w.f.text
##    scrollbar $w.scroll2 -orient horizontal -command "$t xview"
##    pack $w.scroll2 -after $w.buttons -side bottom -fill x
##    $t configure -xscrollcommand "$w.scroll2 set" -wrap none
##}
##proc textWindOff w {
##    catch {destroy $w.scroll2}
##    set t $w.f.text
##    $t configure -xscrollcommand {} -wrap word
##}
on = Button(text, text='Turn On', command=textWindOn,
            cursor='top_left_arrow')
off = Button(text, text='Turn Off', command=textWindOff,
             cursor='top_left_arrow')

##$t insert end "A text widget can contain many different kinds of items, "
##$t insert end "both active and passive.  It can lay these out in various "
##$t insert end "ways, with wrapping, tabs, centering, etc.  In addition, "
##$t insert end "when the contents are too big for the window, smooth "
##$t insert end "scrolling in all directions is provided.\n\n"
text.insert('end', "A text widget can contain many different kinds of items, ")
text.insert('end', "both active and passive.  It can lay these out in various ")
text.insert('end', "ways, with wrapping, tabs, centering, etc.  In addition, ")
text.insert('end', "when the contents are too big for the window, smooth ")
text.insert('end', "scrolling in all directions is provided.\n\n")

##$t insert end "A text widget can contain other widgets embedded "
##$t insert end "it.  These are called \"embedded windows\", "
##$t insert end "and they can consist of arbitrary widgets.  "
##$t insert end "For example, here are two embedded button "
##$t insert end "widgets.  You can click on the first button to "
##$t window create end -window $t.on
##$t insert end " horizontal scrolling, which also turns off "
##$t insert end "word wrapping.  Or, you can click on the second "
##$t insert end "button to\n"
##$t window create end -window $t.off
##$t insert end " horizontal scrolling and turn back on word wrapping.\n\n"
text.insert('end', "A text widget can contain other widgets embedded ")
text.insert('end', "it.  These are called \"embedded windows\", ")
text.insert('end', "and they can consist of arbitrary widgets.  ")
text.insert('end', "For example, here are two embedded button ")
text.insert('end', "widgets.  You can click on the first button to ")
text.window_create('end', window=on)
text.insert('end', " horizontal scrolling, which also turns off ")
text.insert('end', "word wrapping.  Or, you can click on the second ")
text.insert('end', "button to\n")
text.window_create('end', window=off)
text.insert('end', " horizontal scrolling and turn back on word wrapping.\n\n")

##$t insert end "Or, here is another example.  If you "
##$t window create end -create {
##    button %W.click -text "Click Here" -command "textWindPlot %W" \
##	    -cursor top_left_arrow}
def embPlotDown(w, x, y):
    pass
def embPlotMove(w, x, y):
    pass
##set embPlot(lastX) 0
##set embPlot(lastY) 0
##proc embPlotDown {w x y} {
##    global embPlot
##    $w dtag selected
##    $w addtag selected withtag current
##    $w raise current
##    set embPlot(lastX) $x
##    set embPlot(lastY) $y
##}
##proc embPlotMove {w x y} {
##    global embPlot
##    $w move selected [expr {$x-$embPlot(lastX)}] [expr {$y-$embPlot(lastY)}]
##    set embPlot(lastX) $x
##    set embPlot(lastY) $y
##}
def createPlot(t):
    pass
##proc createPlot {t} {
##    set c $t.c
##
##    canvas $c -relief sunken -width 450 -height 300 -cursor top_left_arrow
##
##    set font {Helvetica 18}
##
##    $c create line 100 250 400 250 -width 2
##    $c create line 100 250 100 50 -width 2
##    $c create text 225 20 -text "A Simple Plot" -font $font -fill brown
##    
##    for {set i 0} {$i <= 10} {incr i} {
##	set x [expr {100 + ($i*30)}]
##	$c create line $x 250 $x 245 -width 2
##	$c create text $x 254 -text [expr {10*$i}] -anchor n -font $font
##    }
##    for {set i 0} {$i <= 5} {incr i} {
##	set y [expr {250 - ($i*40)}]
##	$c create line 100 $y 105 $y -width 2
##	$c create text 96 $y -text [expr {$i*50}].0 -anchor e -font $font
##    }
##    
##    foreach point {
##	{12 56} {20 94} {33 98} {32 120} {61 180} {75 160} {98 223}
##    } {
##	set x [expr {100 + (3*[lindex $point 0])}]
##	set y [expr {250 - (4*[lindex $point 1])/5}]
##	set item [$c create oval [expr {$x-6}] [expr {$y-6}] \
##		[expr {$x+6}] [expr {$y+6}] -width 1 -outline black \
##		-fill SkyBlue2]
##	$c addtag point withtag $item
##    }
##
##    $c bind point <Any-Enter> "$c itemconfig current -fill red"
##    $c bind point <Any-Leave> "$c itemconfig current -fill SkyBlue2"
##    $c bind point <1> "embPlotDown $c %x %y"
##    $c bind point <ButtonRelease-1> "$c dtag selected"
##    bind $c <B1-Motion> "embPlotMove $c %x %y"
##    return $c
##}
def textWindPlot(w):
    pass
##proc textWindPlot t {
##    set c $t.c
##    if {[winfo exists $c]} {
##	return
##    }
##
##    while {[string first [$t get plot] " \t\n"] >= 0} {
##	$t delete plot
##    }
##    $t insert plot "\n"
##
##    $t window create plot -create {createPlot %W}
##    $t tag add center plot
##    $t insert plot "\n"
##}
click = Button(text, text='Click Here', command=lambda w=w: textWindPlot(w),
               cursor='top_left_arrow')
text.insert('end', "Or, here is another example.  If you ")
text.window_create('end', window=click)

##$t insert end " a canvas displaying an x-y plot will appear right here."
##$t mark set plot insert
##$t mark gravity plot left
##$t insert end "  You can drag the data points around with the mouse, "
##$t insert end "or you can click here to "
##$t window create end -create {
##    button %W.delete -text "Delete" -command "textWindDel %W" \
##	    -cursor top_left_arrow
##}
##$t insert end " the plot again.\n\n"
def textWindDel(w):
    pass
##proc textWindDel t {
##    if {[winfo exists $t.c]} {
##	$t delete $t.c
##	while {[string first [$t get plot] " \t\n"] >= 0} {
##	    $t delete plot
##	}
##	$t insert plot "  "
##    }
##}
delete = Button(text, text='Delete', command=lambda w=w: textWindDel(w),
                cursor='top_left_arrow')
text.insert('end', " a canvas displaying an x-y plot will appear right here.")
text.mark_set('plot', 'insert')
text.mark_gravity('plot', 'left')
text.insert('end', "  You can drag the data points around with the mouse, ")
text.insert('end', "or you can click here to ")
text.window_create('end', window=delete)
text.insert('end', " the plot again.\n\n")

##$t insert end "You can also create multiple text widgets each of which "
##$t insert end "display the same underlying text. Click this button to "
##$t window create end \
##  -create {button %W.peer -text "Make A Peer" -command "textMakePeer %W" \
##  -cursor top_left_arrow} -padx 3
##$t insert end " widget.  Notice how peer widgets can have different "
##$t insert end "font settings, and by default contain all the images "
##$t insert end "of the 'parent', but many of the embedded windows, "
##$t insert end "such as buttons will not be there.  The easiest way "
##$t insert end "to ensure they are in all peers is to use '-create' "
##$t insert end "embedded window creation scripts "
##$t insert end "(the plot above and the 'Make A Peer' button are "
##$t insert end "designed to show up in all peers).  A good use of "
##$t insert end "peers is for "
##$t window create end \
##  -create {button %W.split -text "Split Windows" -command "textSplitWindow %W" \
##  -cursor top_left_arrow} -padx 3
##$t insert end " \n\n"
def create_peer(text, master, name, cnf={}, **kw):
    class textpeer(Text):
        """Internal class used to represent a text peer."""
        def __init__(self, master, name):
            BaseWidget._setup(self, master, {'name': name})
    text.peer_create('%s.%s' % (master, name), cnf, **kw)
    return textpeer(master, name)
def textMakePeer(w):
    pass
def textSplitWindow(textW):
    global text, pane, scroll, w
    global create_peer
    if textW == text:
        global peer
##        if peer.winfo_exists():
##            peer.destroy()
##        else:
        try:
            #print('111')
            print(w)
            print(textW)
            #peer = TextPeer(w, 'text')
            #print(peer)
            #textW.peer_create('%s.peer' % w, yscrollcommand=scroll.set)
            #peer = TextPeer(w, 'peer')
            peer = create_peer(textW, w, 'peer', yscrollcommand=scroll.set)
            print(peer)
            pane.add(peer)
        except TclError:
            peer.destroy()
    else:
        return
##proc textMakePeer {parent} {
##    set n 1
##    while {[winfo exists .peer$n]} { incr n }
##    set w [toplevel .peer$n]
##    wm title $w "Text Peer #$n"
##    frame $w.f -highlightthickness 1 -borderwidth 1 -relief sunken
##    set t [$parent peer create $w.f.text -yscrollcommand "$w.scroll set" \
##	       -borderwidth 0 -highlightthickness 0]
##    pack $t -expand  yes -fill both
##    scrollbar $w.scroll -command "$t yview"
##    pack $w.scroll -side right -fill y
##    pack $w.f -expand yes -fill both
##}
##proc textSplitWindow {textW} {
##    if {$textW eq ".twind.f.text"} {
##	if {[winfo exists .twind.peer]} {
##	    destroy .twind.peer
##	} else {
##	    set parent [winfo parent $textW]
##	    set w [winfo parent $parent]
##	    set t [$textW peer create $w.peer \
##	      -yscrollcommand "$w.scroll set"]
##	    $w.pane add $t
##	}
##    } else {
##        return
##    }
##}
peer = Button(text, text='Make A Peer', command=lambda w=w: textMakePeer(w),
              cursor='top_left_arrow')
split = Button(text, text='Split Windows',
               command=lambda w=text, f=textSplitWindow: f(w),
               cursor='top_left_arrow')
text.insert('end', "You can also create multiple text widgets each of which ")
text.insert('end', "display the same underlying text. Click this button to ")
text.window_create('end', window=peer, padx=3)
text.insert('end', " widget.  Notice how peer widgets can have different ")
text.insert('end', "font settings, and by default contain all the images ")
text.insert('end', "of the 'parent', but many of the embedded windows, ")
text.insert('end', "such as buttons will not be there.  The easiest way ")
text.insert('end', "to ensure they are in all peers is to use '-create' ")
text.insert('end', "embedded window creation scripts ")
text.insert('end', "(the plot above and the 'Make A Peer' button are ")
text.insert('end', "designed to show up in all peers).  A good use of ")
text.insert('end', "peers is for ")
text.window_create('end', window=split, padx=3)
text.insert('end', " \n\n")

##$t insert end "Users of previous versions of Tk will also be interested "
##$t insert end "to note that now cursor movement is now by visual line by "
##$t insert end "default, and that all scrolling of this widget is by pixel.\n\n"
text.insert('end', "Users of previous versions of Tk will also be interested ")
text.insert('end', "to note that now cursor movement is now by visual line by ")
text.insert('end', "default, and that all scrolling of this widget is by pixel.\n\n")

##$t insert end "You may also find it useful to put embedded windows in "
##$t insert end "a text without any actual text.  In this case the "
##$t insert end "text widget acts like a geometry manager.  For "
##$t insert end "example, here is a collection of buttons laid out "
##$t insert end "neatly into rows by the text widget.  These buttons "
##$t insert end "can be used to change the background color of the "
##$t insert end "text widget (\"Default\" restores the color to "
##$t insert end "its default).  If you click on the button labeled "
##$t insert end "\"Short\", it changes to a longer string so that "
##$t insert end "you can see how the text widget automatically "
##$t insert end "changes the layout.  Click on the button again "
##$t insert end "to restore the short string.\n"
text.insert('end', "You may also find it useful to put embedded windows in ")
text.insert('end', "a text without any actual text.  In this case the ")
text.insert('end', "text widget acts like a geometry manager.  For ")
text.insert('end', "example, here is a collection of buttons laid out ")
text.insert('end', "neatly into rows by the text widget.  These buttons ")
text.insert('end', "can be used to change the background color of the ")
text.insert('end', "text widget (\"Default\" restores the color to ")
text.insert('end', "its default).  If you click on the button labeled ")
text.insert('end', "\"Short\", it changes to a longer string so that ")
text.insert('end', "you can see how the text widget automatically ")
text.insert('end', "changes the layout.  Click on the button again ")
text.insert('end', "to restore the short string.\n")

##button $t.default -text Default -command "embDefBg $t" \
##	-cursor top_left_arrow
##$t window create end -window $t.default -padx 3
##global embToggle
##set embToggle Short
##checkbutton $t.toggle -textvariable embToggle -indicatoron 0 \
##	-variable embToggle -onvalue "A much longer string" \
##	-offvalue "Short" -cursor top_left_arrow -pady 5 -padx 2
##$t window create end -window $t.toggle -padx 3 -pady 2
##set i 1
##foreach color {AntiqueWhite3 Bisque1 Bisque2 Bisque3 Bisque4
##	SlateBlue3 RoyalBlue1 SteelBlue2 DeepSkyBlue3 LightBlue1
##	DarkSlateGray1 Aquamarine2 DarkSeaGreen2 SeaGreen1
##	Yellow1 IndianRed1 IndianRed2 Tan1 Tan4} {
##    button $t.color$i -text $color -cursor top_left_arrow -command \
##	    "$t configure -bg $color"
##    $t window create end -window $t.color$i -padx 3 -pady 2
##    incr i
##}
##$t tag add buttons $t.default end
default = Button(text, text='Default',
                 command=lambda t=text:\
                     t.configure(background=t.configure('background')[3]),
                 cursor='top_left_arrow')
# if arg without value in configure(),
#     return 5 values, the third vale is default value. 
# int Tk_ConfigureInfo(interp, tkwin, specs, widgRec, argvName, flags)
# If argvName is NULL, the list will contain five values:
# argvName, dbName, dbClass, defValue, and current value
text.window_create('end', window=default, padx=3)
embToggle = StringVar()
embToggle.set('Short')
toggle = Checkbutton(text, textvariable=embToggle, indicatoron=0,
                     variable=embToggle, onvalue='A much longer string',
                     offvalue='Short', cursor='top_left_arrow', pady=5, padx=2)
text.window_create('end', window=toggle, padx=3, pady=2)
for color in ('AntiqueWhite3', 'Bisque1', 'Bisque2', 'Bisque3', 'Bisque4',
	'SlateBlue3', 'RoyalBlue1', 'SteelBlue2', 'DeepSkyBlue3', 'LightBlue1',
	'DarkSlateGray1', 'Aquamarine2', 'DarkSeaGreen2', 'SeaGreen1',
	'Yellow1', 'IndianRed1', 'IndianRed2', 'Tan1', 'Tan4'):
    colorbtn = Button(text, text=color, cursor='top_left_arrow',
                      command=lambda t=text, c=color: t.configure(bg=c))
    text.window_create('end', window=colorbtn, padx=3, pady=2)
text.tag_add('buttons', default, 'end')

##button $t.bigB -text "Big borders" -command "textWindBigB $t" \
##  -cursor top_left_arrow
##button $t.smallB -text "Small borders" -command "textWindSmallB $t" \
##  -cursor top_left_arrow
##button $t.bigH -text "Big highlight" -command "textWindBigH $t" \
##  -cursor top_left_arrow
##button $t.smallH -text "Small highlight" -command "textWindSmallH $t" \
##  -cursor top_left_arrow
##button $t.bigP -text "Big pad" -command "textWindBigP $t" \
##  -cursor top_left_arrow
##button $t.smallP -text "Small pad" -command "textWindSmallP $t" \
##  -cursor top_left_arrow
text_normal = dict(border = text['borderwidth'],
                   highlight = text['highlightthickness'],
                   pad = text['padx'])
bigB = Button(text, text='Big borders',
              command=lambda t=text: t.configure(borderwidth=15),
              cursor='top_left_arrow')
smallB = Button(
    text, text='Small borders',
    command=lambda t=text, tnormal=text_normal: \
        t.configure(borderwidth=tnormal['border']),
    cursor='top_left_arrow')
bigH = Button(text, text='Big highlight',
              command=lambda t=text: t.configure(highlightthickness=15),
              cursor='top_left_arrow')
smallH = Button(
    text, text='Small highlight',
    command=lambda t=text, tnormal=text_normal:\
        t.configure(highlightthickness=tnormal['highlight']),
    cursor='top_left_arrow')
bigP = Button(text, text='Big pad',
              command=lambda t=text: t.configure(padx=15, pady=15),
              cursor='top_left_arrow')
smallP = Button(
    text, text='Small pad',
    command=lambda t=text, tnormal=text_normal: \
        t.configure(padx=tnormal['pad'],
                    pady=tnormal['pad']),
    cursor='top_left_arrow')

##set text_normal(border) [$t cget -borderwidth]
##set text_normal(highlight) [$t cget -highlightthickness]
##set text_normal(pad) [$t cget -padx]
##
##$t insert end "\nYou can also change the usual border width and "
##$t insert end "highlightthickness and padding.\n"
##$t window create end -window $t.bigB
##$t window create end -window $t.smallB
##$t window create end -window $t.bigH
##$t window create end -window $t.smallH
##$t window create end -window $t.bigP
##$t window create end -window $t.smallP
##
##$t insert end "\n\nFinally, images fit comfortably in text widgets too:"
##
##$t image create end -image \
##    [image create photo -file [file join $tk_demoDirectory images ouster.png]]
text.insert('end', "\nYou can also change the usual border width and ")
text.insert('end', "highlightthickness and padding.\n")
text.window_create('end', window=bigB)
text.window_create('end', window=smallB)
text.window_create('end', window=bigH)
text.window_create('end', window=smallH)
text.window_create('end', window=bigP)
text.window_create('end', window=smallP)

text.insert('end', "\n\nFinally, images fit comfortably in text widgets too:")

import os.path
ousterhout = PhotoImage(file=os.path.join(tk_demoDirectory,
                                          'images', 'ouster.png'))
text.image_create('end', image=ousterhout)
# keep a reference,
# to prevent image object be garbage-collected by Python.
text.image = ousterhout


##proc textWindBigB w {
##    $w configure -borderwidth 15 
##}
##
##proc textWindBigH w {
##    $w configure -highlightthickness 15
##}
##
##proc textWindBigP w {
##    $w configure -padx 15 -pady 15
##}
##
##proc textWindSmallB w {
##    $w configure -borderwidth $::text_normal(border)
##}
##
##proc textWindSmallH w {
##    $w configure -highlightthickness $::text_normal(highlight)
##}
##
##proc textWindSmallP w {
##    $w configure -padx $::text_normal(pad) -pady $::text_normal(pad)
##}


##proc textWindOn w {
##    catch {destroy $w.scroll2}
##    set t $w.f.text
##    scrollbar $w.scroll2 -orient horizontal -command "$t xview"
##    pack $w.scroll2 -after $w.buttons -side bottom -fill x
##    $t configure -xscrollcommand "$w.scroll2 set" -wrap none
##}

##proc textWindOff w {
##    catch {destroy $w.scroll2}
##    set t $w.f.text
##    $t configure -xscrollcommand {} -wrap word
##}

##proc textWindPlot t {
##    set c $t.c
##    if {[winfo exists $c]} {
##	return
##    }
##
##    while {[string first [$t get plot] " \t\n"] >= 0} {
##	$t delete plot
##    }
##    $t insert plot "\n"
##
##    $t window create plot -create {createPlot %W}
##    $t tag add center plot
##    $t insert plot "\n"
##}

##proc createPlot {t} {
##    set c $t.c
##
##    canvas $c -relief sunken -width 450 -height 300 -cursor top_left_arrow
##
##    set font {Helvetica 18}
##
##    $c create line 100 250 400 250 -width 2
##    $c create line 100 250 100 50 -width 2
##    $c create text 225 20 -text "A Simple Plot" -font $font -fill brown
##    
##    for {set i 0} {$i <= 10} {incr i} {
##	set x [expr {100 + ($i*30)}]
##	$c create line $x 250 $x 245 -width 2
##	$c create text $x 254 -text [expr {10*$i}] -anchor n -font $font
##    }
##    for {set i 0} {$i <= 5} {incr i} {
##	set y [expr {250 - ($i*40)}]
##	$c create line 100 $y 105 $y -width 2
##	$c create text 96 $y -text [expr {$i*50}].0 -anchor e -font $font
##    }
##    
##    foreach point {
##	{12 56} {20 94} {33 98} {32 120} {61 180} {75 160} {98 223}
##    } {
##	set x [expr {100 + (3*[lindex $point 0])}]
##	set y [expr {250 - (4*[lindex $point 1])/5}]
##	set item [$c create oval [expr {$x-6}] [expr {$y-6}] \
##		[expr {$x+6}] [expr {$y+6}] -width 1 -outline black \
##		-fill SkyBlue2]
##	$c addtag point withtag $item
##    }
##
##    $c bind point <Any-Enter> "$c itemconfig current -fill red"
##    $c bind point <Any-Leave> "$c itemconfig current -fill SkyBlue2"
##    $c bind point <1> "embPlotDown $c %x %y"
##    $c bind point <ButtonRelease-1> "$c dtag selected"
##    bind $c <B1-Motion> "embPlotMove $c %x %y"
##    return $c
##}

##set embPlot(lastX) 0
##set embPlot(lastY) 0
##
##proc embPlotDown {w x y} {
##    global embPlot
##    $w dtag selected
##    $w addtag selected withtag current
##    $w raise current
##    set embPlot(lastX) $x
##    set embPlot(lastY) $y
##}
##
##proc embPlotMove {w x y} {
##    global embPlot
##    $w move selected [expr {$x-$embPlot(lastX)}] [expr {$y-$embPlot(lastY)}]
##    set embPlot(lastX) $x
##    set embPlot(lastY) $y
##}

##proc textWindDel t {
##    if {[winfo exists $t.c]} {
##	$t delete $t.c
##	while {[string first [$t get plot] " \t\n"] >= 0} {
##	    $t delete plot
##	}
##	$t insert plot "  "
##    }
##}

##proc embDefBg t {
##    $t configure -background [lindex [$t configure -background] 3]
##}

##proc textMakePeer {parent} {
##    set n 1
##    while {[winfo exists .peer$n]} { incr n }
##    set w [toplevel .peer$n]
##    wm title $w "Text Peer #$n"
##    frame $w.f -highlightthickness 1 -borderwidth 1 -relief sunken
##    set t [$parent peer create $w.f.text -yscrollcommand "$w.scroll set" \
##	       -borderwidth 0 -highlightthickness 0]
##    pack $t -expand  yes -fill both
##    scrollbar $w.scroll -command "$t yview"
##    pack $w.scroll -side right -fill y
##    pack $w.f -expand yes -fill both
##}

##proc textSplitWindow {textW} {
##    if {$textW eq ".twind.f.text"} {
##	if {[winfo exists .twind.peer]} {
##	    destroy .twind.peer
##	} else {
##	    set parent [winfo parent $textW]
##	    set w [winfo parent $parent]
##	    set t [$textW peer create $w.peer \
##	      -yscrollcommand "$w.scroll set"]
##	    $w.pane add $t
##	}
##    } else {
##        return
##    }
##}
