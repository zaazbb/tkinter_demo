# tree.tcl --
#
# This demonstration script creates a toplevel window containing a Ttk
# tree widget.

##if {![info exists widgetDemo]} {
##    error "This script should be run from the \"widget\" demo."
##}
assert 'widgetDemo' in globals(), \
'This script should be run from the "widget" demo.'

##package require Tk
from tkinter import *

##set w .tree
##catch {destroy $w}
##toplevel $w
##wm title $w "Directory Browser"
##wm iconname $w "tree"
##positionWindow $w
demo_name = 'tree'
if demo_name in globals()['demo_name']:
    globals()['demo_name'][demo_name].destroy()
w = globals()['demo_name'][demo_name] = Toplevel(root)
w.wm_title('Directory Browser')
w.wm_iconname('tree')
positionWindow(w)

## Explanatory text
##ttk::label $w.msg -font $font -wraplength 4i -justify left -anchor n -padding {10 2 10 6} -text "Ttk is the new Tk themed widget set. One of the widgets it includes is a tree widget, which allows the user to browse a hierarchical data-set such as a filesystem. The tree widget not only allows for the tree part itself, but it also supports an arbitrary number of additional columns which can show additional data (in this case, the size of the files found in your filesystem). You can also change the width of the columns by dragging the boundary between them."
##pack $w.msg -fill x
msg = ttk.Label(w, font=font_, wraplength='4i', justify='left', anchor='n', padding='10 2 10 6', text="Ttk is the new Tk themed widget set. One of the widgets it includes is a tree widget, which allows the user to browse a hierarchical data-set such as a filesystem. The tree widget not only allows for the tree part itself, but it also supports an arbitrary number of additional columns which can show additional data (in this case, the size of the files found in your filesystem). You can also change the width of the columns by dragging the boundary between them.")
msg.pack(fill='x')

## See Code / Dismiss
##pack [addSeeDismiss $w.seeDismiss $w] -side bottom -fill x
addSeeDismiss(w, demo_name).pack(side='bottom', fill='x')

## Code to populate the roots of the tree (can be more than one on Windows)
##proc populateRoots {tree} {
##    foreach dir [lsort -dictionary [file volumes]] {
##	populateTree $tree [$tree insert {} end -text $dir \
##		-values [list $dir directory]]
##    }
##}

## Code to populate a node of the tree
##proc populateTree {tree node} {
##    if {[$tree set $node type] ne "directory"} {
##	return
##    }
##    set path [$tree set $node fullpath]
##    $tree delete [$tree children $node]
##    foreach f [lsort -dictionary [glob -nocomplain -dir $path *]] {
##	set type [file type $f]
##	set id [$tree insert $node end -text [file tail $f] \
##		-values [list $f $type]]
##
##	if {$type eq "directory"} {
##	    ## Make it so that this node is openable
##	    $tree insert $id 0 -text dummy ;# a dummy
##	    $tree item $id -text [file tail $f]/
##
##	} elseif {$type eq "file"} {
##	    set size [file size $f]
##	    ## Format the file size nicely
##	    if {$size >= 1024*1024*1024} {
##		set size [format %.1f\ GB [expr {$size/1024/1024/1024.}]]
##	    } elseif {$size >= 1024*1024} {
##		set size [format %.1f\ MB [expr {$size/1024/1024.}]]
##	    } elseif {$size >= 1024} {
##		set size [format %.1f\ kB [expr {$size/1024.}]]
##	    } else {
##		append size " bytes"
##	    }
##	    $tree set $id size $size
##	}
##    }
##
##    # Stop this code from rerunning on the current node
##    $tree set $node type processedDirectory
##}
import os
import os.path
import glob
def populateTree(tree, node):
    if tree.set(node, 'type') != 'directory': return
    path = tree.set(node, 'fullpath')
    try: tree.delete(tree.get_children(node))
    except: pass
    for f in glob.glob(os.path.join(path, '*')):
        try:
            type_ = root.tk.call('file', 'type', f)
            id_ = tree.insert(node, 'end', text=os.path.basename(f),
                              values=root.tk.call('list', f, type_))
            if type_=='directory':
                tree.insert(id_, 0, text='dummy')
                tree.item(id_, text=os.path.basename(f)+'/')
            elif type_=='file':
                size = int(root.tk.call('file', 'size', f))
                if size >= 1024*1024*1024:
                    size = '%.1f GB' % (size/1024/1024/1024)
                elif size >= 1024*1024:
                    size = '%.1f MB' % (size/1024/1024)
                elif size >= 1024:
                    size = '%.1f kB' % (size/1024)
                else:
                    size = '%i bytes' % size
                tree.set(id_, 'size', size)
        except: pass
    tree.set(node, 'type', 'processedDirectory')
globals().update(locals())
def populateRoots(tree):
    for dir_ in root.tk.call('file', 'volumes'):
        populateTree(tree, tree.insert('', 'end', text=dir_,
            values=root.tk.call('list', dir_, 'directory')))

## Create the tree and set it up
##ttk::treeview $w.tree -columns {fullpath type size} -displaycolumns {size} \
##	-yscroll "$w.vsb set" -xscroll "$w.hsb set"
##ttk::scrollbar $w.vsb -orient vertical -command "$w.tree yview"
##ttk::scrollbar $w.hsb -orient horizontal -command "$w.tree xview"
##$w.tree heading \#0 -text "Directory Structure"
##$w.tree heading size -text "File Size"
##$w.tree column size -stretch 0 -width 70
##populateRoots $w.tree
##bind $w.tree <<TreeviewOpen>> {populateTree %W [%W focus]}
global tree
tree = ttk.Treeview(w, columns='fullpath type size', displaycolumns='size')
vsb = ttk.Scrollbar(w, orient='vertical', command=tree.yview)
hsb = ttk.Scrollbar(w, orient='horizontal', command=tree.xview)
tree['yscroll'] = vsb.set
tree['xscroll'] = hsb.set
tree.heading('#0', text='Directory Structure')
tree.heading('size', text='File Size')
tree.column('size', stretch=0, width=70)
populateRoots(tree)
tree.bind('<<TreeviewOpen>>', lambda e: populateTree(e.widget, e.widget.focus()))

## Arrange the tree and its scrollbars in the toplevel
##lower [ttk::frame $w.dummy]
##pack $w.dummy -fill both -expand 1
##grid $w.tree $w.vsb -sticky nsew -in $w.dummy
##grid $w.hsb -sticky nsew -in $w.dummy
##grid columnconfigure $w.dummy 0 -weight 1
##grid rowconfigure $w.dummy 0 -weight 1
dummy = ttk.Frame(w)
dummy.lower()
dummy.pack(fill='both', expand=1)
for i,w in enumerate([tree, vsb]):
    w.grid(column=i, row=0, sticky='nsew', in_=dummy)
hsb.grid(sticky='nsew', in_=dummy)
dummy.grid_columnconfigure(0, weight=1)
dummy.grid_rowconfigure(0, weight=1)
