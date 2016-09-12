# mclist.tcl --
#
# This demonstration script creates a toplevel window containing a Ttk
# tree widget configured as a multi-column listbox.

##if {![info exists widgetDemo]} {
##    error "This script should be run from the \"widget\" demo."
##}
assert 'widgetDemo' in globals(), \
'This script should be run from the "widget" demo.'

##package require Tk
from tkinter import *

##set w .mclist
##catch {destroy $w}
##toplevel $w
##wm title $w "Multi-Column List"
##wm iconname $w "mclist"
##positionWindow $w
demo_name = 'mclist'
if demo_name in globals()['demo_name']:
    globals()['demo_name'][demo_name].destroy()
w = globals()['demo_name'][demo_name] = Toplevel(root)
w.wm_title('Multi-Column List')
w.wm_iconname('mclist')
positionWindow(w)

## Explanatory text
##ttk::label $w.msg -font $font -wraplength 4i -justify left -anchor n -padding {10 2 10 6} -text "Ttk is the new Tk themed widget set. One of the widgets it includes is a tree widget, which can be configured to display multiple columns of informational data without displaying the tree itself. This is a simple way to build a listbox that has multiple columns. Clicking on the heading for a column will sort the data by that column. You can also change the width of the columns by dragging the boundary between them."
##pack $w.msg -fill x
msg = ttk.Label(w, font=font_, wraplength='4i', justify='left', anchor='n', padding='10 2 10 6', text="Ttk is the new Tk themed widget set. One of the widgets it includes is a tree widget, which can be configured to display multiple columns of informational data without displaying the tree itself. This is a simple way to build a listbox that has multiple columns. Clicking on the heading for a column will sort the data by that column. You can also change the width of the columns by dragging the boundary between them.")
msg.pack(fill='x')

## See Code / Dismiss
##pack [addSeeDismiss $w.seeDismiss $w] -side bottom -fill x
addSeeDismiss(ttk.Frame(w), demo_name).pack(side='bottom', fill='x')

##ttk::frame $w.container
##ttk::treeview $w.tree -columns {country capital currency} -show headings \
##    -yscroll "$w.vsb set" -xscroll "$w.hsb set"
##ttk::scrollbar $w.vsb -orient vertical -command "$w.tree yview"
##ttk::scrollbar $w.hsb -orient horizontal -command "$w.tree xview"
##pack $w.container -fill both -expand 1
##grid $w.tree $w.vsb -in $w.container -sticky nsew
##grid $w.hsb         -in $w.container -sticky nsew
##grid column $w.container 0 -weight 1
##grid row    $w.container 0 -weight 1
container = ttk.Frame(w)
title = 'country capital currency'.split()
tree = ttk.Treeview(container, columns=title, show='headings')
vsb = ttk.Scrollbar(container, orient='vertical', command=tree.yview)
hsb = ttk.Scrollbar(container, orient='horizontal', command=tree.xview)
tree['yscroll'] = vsb.set
tree['xscroll'] = hsb.set
container.pack(fill='both', expand=1)
tree.grid(column=0, row=0, sticky='nsew')
vsb.grid(column=1, row=0, sticky='nsew')
hsb.grid(column=0, row=1, sticky='nsew')
container.columnconfigure(0, weight=1)
container.rowconfigure(0, weight=1)

##image create photo upArrow -data {
##    R0lGODlhDgAOAJEAANnZ2YCAgPz8/P///yH5BAEAAAAALAAAAAAOAA4AAAImhI+
##    py+1LIsJHiBAh+BgmiEAJQITgW6DgUQIAECH4JN8IPqYuNxUAOw==}
##image create photo downArrow -data {
##    R0lGODlhDgAOAJEAANnZ2YCAgPz8/P///yH5BAEAAAAALAAAAAAOAA4AAAInhI+
##    py+1I4ocQ/IgDEYIPgYJICUCE4F+YIBolEoKPEJKZmVJK6ZACADs=}
##image create photo noArrow -height 14 -width 14
upArrow = PhotoImage(data="""
    R0lGODlhDgAOAJEAANnZ2YCAgPz8/P///yH5BAEAAAAALAAAAAAOAA4AAAImhI+
    py+1LIsJHiBAh+BgmiEAJQITgW6DgUQIAECH4JN8IPqYuNxUAOw==
""")
downArrow = PhotoImage(data="""
    R0lGODlhDgAOAJEAANnZ2YCAgPz8/P///yH5BAEAAAAALAAAAAAOAA4AAAInhI+
    py+1I4ocQ/IgDEYIPgYJICUCE4F+YIBolEoKPEJKZmVJK6ZACADs=
""")
noArrow = PhotoImage(height=14, width=14)

## The data we're going to insert
##set data {
##    Argentina		{Buenos Aires}		ARS
##    Australia		Canberra		AUD
##    Brazil		Brazilia		BRL
##    Canada		Ottawa			CAD
##    China		Beijing			CNY
##    France		Paris			EUR
##    Germany		Berlin			EUR
##    India		{New Delhi}		INR
##    Italy		Rome			EUR
##    Japan		Tokyo			JPY
##    Mexico		{Mexico City}		MXN
##    Russia		Moscow			RUB
##    {South Africa}	Pretoria		ZAR
##    {United Kingdom}	London			GBP
##    {United States}	{Washington, D.C.}	USD
##}
data =[
    ['Argentina',	'{Buenos Aires}',	'ARS'],
    ['Australia',	'Canberra',		'AUD'],
    ['Brazil',		'Brazilia',		'BRL'],
    ['Canada',		'Ottawa',		'CAD'],
    ['China',		'Beijing',		'CNY'],
    ['France',		'Paris',		'EUR'],
    ['Germany',		'Berlin',		'EUR'],
    ['India',		'{New Delhi}',		'INR'],
    ['Italy',		'Rome',			'EUR'],
    ['Japan',		'Tokyo',		'JPY'],
    ['Mexico',		'{Mexico City}',	'MXN'],
    ['Russia',		'Moscow',		'RUB'],
    ['{South Africa}',	'Pretoria',		'ZAR'],
    ['{United Kingdom}','London',		'GBP'],
    ['{United States}',	'{Washington, D.C.}',	'USD']]

## Code to insert the data nicely
##set font [ttk::style lookup Heading -font]
##foreach col {country capital currency} name {Country Capital Currency} {
##    $w.tree heading $col -text $name -image noArrow -anchor w \
##	-command [list SortBy $w.tree $col 0]
##    $w.tree column $col -width [expr {
##	[font measure $font $name] + [image width noArrow] + 5
##    }]
##}
##set font [ttk::style lookup Treeview -font]
##foreach {country capital currency} $data {
##    $w.tree insert {} end -values [list $country $capital $currency]
##    foreach col {country capital currency} {
##	set len [font measure $font "[set $col]  "]
##	if {[$w.tree column $col -width] < $len} {
##	    $w.tree column $col -width $len
##	}
##    }
##}
treeState = {}
def SortBy(tree, col, direction):
    for c in title:
##        s = tree.heading(c)['tate']
        try :
            s =  treeState[c]
        except:
            treeState[c] = {'active':False, 'selected':False, 'alternate':False, 'user1':False}
            treeState[c]['active'] = True if col == c else False
            s =  treeState[c]
##        if 'selected' in s or 'alternate' in s and col != c:
##            tree.heading(c, image=vars_['noArrow'], state='!selected !alternate !user1')
        if treeState[c]['selected'] or treeState[c]['alternate'] and col != c:
            tree.heading(c, image=noArrow)
            treeState[c]['selected'] = False
            treeState[c]['alternate'] = False
            treeState[c]['user1'] = False
            direction = 'alternate' in s
    data = []
    for row in tree.get_children():
        data.append((tree.set(row, col), row))
    for i,info in enumerate(sorted(data, key=lambda data: data[0], reverse=direction)):
        tree.move(info[1], '', i)
##    tree.heading(col, command=lambda vars_=vars_: vars_['SortBy'](tree, col, not direction),
##                 state='!selected alternate' if direction else 'selected !alternate')
    tree.heading(col, command=lambda: SortBy(tree, col, not direction))
    treeState[col]['selected'] = False if direction else True
    treeState[col]['alternate'] = True if direction else False
    if ttk.Style().theme_use() == 'aque':
        tree.heading(col, state='user1')
        treeState[col]['user1'] = True
    else:
        tree.heading(col, image=upArrow if direction else downArrow)
style = ttk.Style()
from tkinter.font import Font
font_ = Font(name=style.lookup('Heading', 'font'), exists=True)
globals().update(locals())
for col in title:
    name = col
    tree.heading(col, text=name, image=noArrow, anchor='w',
        command=lambda col=col: SortBy(tree, col, False))
    tree.column(col, width=font_.measure(name)+noArrow.width()+5)
font_ = Font(name=style.lookup('Treeview', 'font'), exists=True)
for i in data:
    tree.insert('', 'end', values=' '.join(i))
    for n in i:
        len_ = font_.measure(col+'  ')
        if tree.column(col, 'width') < len_:
            tree.column(col, width=len_)

## Code to do the sorting of the tree contents when clicked on
##proc SortBy {tree col direction} {
##    # Determine currently sorted column and its sort direction
##    foreach c {country capital currency} {
##	set s [$tree heading $c state]
##	if {("selected" in $s || "alternate" in $s) && $col ne $c} {
##	    # Sorted column has changed
##	    $tree heading $c -image noArrow state {!selected !alternate !user1}
##	    set direction [expr {"alternate" in $s}]
##	}
##    }
##
##    # Build something we can sort
##    set data {}
##    foreach row [$tree children {}] {
##	lappend data [list [$tree set $row $col] $row]
##    }
##
##    set dir [expr {$direction ? "-decreasing" : "-increasing"}]
##    set r -1
##
##    # Now reshuffle the rows into the sorted order
##    foreach info [lsort -dictionary -index 0 $dir $data] {
##	$tree move [lindex $info 1] {} [incr r]
##    }
##
##    # Switch the heading so that it will sort in the opposite direction
##    $tree heading $col -command [list SortBy $tree $col [expr {!$direction}]] \
##	state [expr {$direction?"!selected alternate":"selected !alternate"}]
##    if {[ttk::style theme use] eq "aqua"} {
##	# Aqua theme displays native sort arrows when user1 state is set
##	$tree heading $col state "user1"
##    } else {
##	$tree heading $col -image [expr {$direction?"upArrow":"downArrow"}]
##    }
##}


