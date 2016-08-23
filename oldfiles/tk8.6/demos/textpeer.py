# textpeer.tcl --
#
# This demonstration script creates a pair of text widgets that can edit a
# single logical buffer. This is particularly useful when editing related text
# in two (or more) parts of the same file.

##if {![info exists widgetDemo]} {
##    error "This script should be run from the \"widget\" demo."
##}
assert 'widgetDemo' in globals(), \
'This script should be run from the "widget" demo.'

##package require Tk
from tkinter import *

##set w .textpeer
##catch {destroy $w}
##toplevel $w
##wm title $w "Text Widget Peering Demonstration"
##wm iconname $w "textpeer"
##positionWindow $w
demo_name = 'textpeer'
if demo_name in globals()['demo_name']:
    globals()['demo_name'][demo_name].destroy()
w = globals()['demo_name'][demo_name] = Toplevel(root)
w.wm_title('Text Widget Peering Demonstration')
w.wm_iconname('textpeer')
positionWindow(w)

##set count 0
##
#### Define a widget that we peer from; it won't ever actually be shown though
##set first [text $w.text[incr count]]
##$first insert end "This is a coupled pair of text widgets; they are peers to "
##$first insert end "each other. They have the same underlying data model, but "
##$first insert end "can show different locations, have different current edit "
##$first insert end "locations, and have different selections. You can also "
##$first insert end "create additional peers of any of these text widgets using "
##$first insert end "the Make Peer button beside the text widget to clone, and "
##$first insert end "delete a particular peer widget using the Delete Peer "
##$first insert end "button."
count = 0
count += 1
first = globals()['text%i' % count] = Text(w)
first.insert(END, "This is a coupled pair of text widgets; they are peers to ")
first.insert(END, "each other. They have the same underlying data model, but ")
first.insert(END, "can show different locations, have different current edit ")
first.insert(END, "locations, and have different selections. You can also ")
first.insert(END, "create additional peers of any of these text widgets using ")
first.insert(END, "the Make Peer button beside the text widget to clone, and ")
first.insert(END, "delete a particular peer widget using the Delete Peer ")
first.insert(END, "button.")

## Procedures to make and kill clones; most of this is just so that the demo
## looks nice...
##proc makeClone {w parent} {
##    global count
##    set t [$parent peer create $w.text[incr count] -yscroll "$w.sb$count set"\
##		  -height 10 -wrap word]
##    set sb [scrollbar $w.sb$count -command "$t yview" -orient vertical]
##    set b1 [button $w.clone$count -command "makeClone $w $t" \
##		    -text "Make Peer"]
##    set b2 [button $w.kill$count -command "killClone $w $count" \
##		    -text "Delete Peer"]
##    set row [expr {$count * 2}]
##    grid $t $sb $b1 -sticky nsew -row $row
##    grid ^  ^   $b2 -row [incr row]
##    grid configure $b1 $b2 -sticky new
##    grid rowconfigure $w $b2 -weight 1
##}
##proc killClone {w count} {
##    destroy $w.text$count $w.sb$count
##    destroy $w.clone$count $w.kill$count
##}
def create_peer(text, master, name, cnf={}, **kw):
    class textpeer(Text):
        """Internal class used to represent a text peer."""
        def __init__(self, master, name):
            BaseWidget._setup(self, master, {'name': name})
    text.peer_create('%s.%s' % (master, name), cnf, **kw)
    return textpeer(master, name)
def makeClone(w, parent):
    global create_peer, makeClone, killClone
    global count
    count += 1
    t = globals()['text'+str(count)] = \
        create_peer(parent, w, 'text'+str(count), height=10, wrap='word')
    sb = globals()['sb'+str(count)] = \
         Scrollbar(w, command=t.yview, orient='vertical')
    t['yscroll'] = sb.set
    b1 = globals()['clone'+str(count)] = \
         Button(w, text='Make Peer', command=lambda: makeClone(w, t))
    b2 = globals()['kill'+str(count)] = \
         Button(w, text='Delete Peer', command=lambda n=count: killClone(w, n))
    row = count * 2
    t.grid(sticky='nsew', row=row, column=0, rowspan=2)
    sb.grid(sticky='nsew', row=row, column=1, rowspan=2)
    b1.grid(sticky='new', row=row, column=2)
    row += 1
    b2.grid(sticky='new', row=row, column=2)
    w.grid_rowconfigure(b2, weight=1)
def killClone(w, count):
    print(count)
    for name in ('text', 'sb', 'clone', 'kill'):
        globals()[name + str(count)].destroy()   

## Now set up the GUI
##makeClone $w $first
##makeClone $w $first
##destroy $first
makeClone(w, first)
makeClone(w, first)
first.destroy()

## See Code / Dismiss buttons
##grid [addSeeDismiss $w.buttons $w] - - -sticky ew -row 5000
##grid columnconfigure $w 0 -weight 1
addSeeDismiss(ttk.Frame(w), demo_name).grid(columnspan=3, sticky='ew', row=5000)
w.grid_columnconfigure(0, weight=1)
