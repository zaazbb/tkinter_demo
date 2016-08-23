# search.tcl --
#
# This demonstration script creates a collection of widgets that
# allow you to load a file into a text widget, then perform searches
# on that file.

##if {![info exists widgetDemo]} {
##    error "This script should be run from the \"widget\" demo."
##}
assert 'widgetDemo' in globals(), \
'This script should be run from the "widget" demo.'

##package require Tk
from tkinter import *

# textLoadFile --
# This procedure below loads a file into a text widget, discarding
# the previous contents of the widget. Tags for the old widget are
# not affected, however.
#
# Arguments:
# w -		The window into which to load the file.  Must be a
#		text widget.
# file -	The name of the file to load.  Must be readable.

##proc textLoadFile {w file} {
##    set f [open $file]
##    $w delete 1.0 end
##    while {![eof $f]} {
##	$w insert end [read $f 10000]
##    }
##    close $f
##}

# textSearch --
# Search for all instances of a given string in a text widget and
# apply a given tag to each instance found.
#
# Arguments:
# w -		The window in which to search.  Must be a text widget.
# string -	The string to search for.  The search is done using
#		exact matching only;  no special characters.
# tag -		Tag to apply to each instance of a matching string.

##proc textSearch {w string tag} {
##    $w tag remove search 0.0 end
##    if {$string == ""} {
##	return
##    }
##    set cur 1.0
##    while 1 {
##	set cur [$w search -count length $string $cur end]
##	if {$cur == ""} {
##	    break
##	}
##	$w tag add $tag $cur "$cur + $length char"
##	set cur [$w index "$cur + $length char"]
##    }
##}

# textToggle --
# This procedure is invoked repeatedly to invoke two commands at
# periodic intervals.  It normally reschedules itself after each
# execution but if an error occurs (e.g. because the window was
# deleted) then it doesn't reschedule itself.
#
# Arguments:
# cmd1 -	Command to execute when procedure is called.
# sleep1 -	Ms to sleep after executing cmd1 before executing cmd2.
# cmd2 -	Command to execute in the *next* invocation of this
#		procedure.
# sleep2 -	Ms to sleep after executing cmd2 before executing cmd1 again.

##proc textToggle {cmd1 sleep1 cmd2 sleep2} {
##    catch {
##	eval $cmd1
##	after $sleep1 [list textToggle $cmd2 $sleep2 $cmd1 $sleep1]
##    }
##}

##set w .search
##catch {destroy $w}
##toplevel $w
##wm title $w "Text Demonstration - Search and Highlight"
##wm iconname $w "search"
##positionWindow $w
demo_name = 'search'
if demo_name in globals()['demo_name']:
    globals()['demo_name'][demo_name].destroy()
w = globals()['demo_name'][demo_name] = Toplevel(root)
w.wm_title('Text Demonstration - Search and Highlight')
w.wm_iconname('search')
positionWindow(w)

## See Code / Dismiss buttons
##set btns [addSeeDismiss $w.buttons $w]
##pack $btns -side bottom -fill x
btns = addSeeDismiss(ttk.Frame(w), demo_name)
btns.pack(side='bottom', fill='x')

##frame $w.file
##label $w.file.label -text "File name:" -width 13 -anchor w
##entry $w.file.entry -width 40 -textvariable fileName
##button $w.file.button -text "Load File" \
##	-command "textLoadFile $w.text \$fileName"
##pack $w.file.label $w.file.entry -side left
##pack $w.file.button -side left -pady 5 -padx 10
##bind $w.file.entry <Return> "
##    textLoadFile $w.text \$fileName
##    focus $w.string.entry
##"
##focus $w.file.entry
def textLoadFile(w, file):
    with open(file) as f:
        w.delete(1.0, END)
        w.insert(END, f.read())
##proc textLoadFile {w file} {
##    set f [open $file]
##    $w delete 1.0 end
##    while {![eof $f]} {
##	$w insert end [read $f 10000]
##    }
##    close $f
##}
text = Text(w, setgrid=True)     
file = Frame(w)
label = Label(file, text='File name:', width=13, anchor='w')
fileName = StringVar()
entry1 = Entry(file, width=40, textvariable=fileName)
button = Button(file, text='Load File',
                command=lambda t=text, var=fileName, f=textLoadFile:
                    f(t, var.get()))
label.pack(side='left')
entry1.pack(side='left')
button.pack(side='left', pady=5, padx=10)
##entry.bind('<Return>',
##           lambda e, t=text, var=fileName, entry=entry, f=textLoadFile:
##               f(t, var.get()) and entry.focus())
entry1.focus()

##frame $w.string
##label $w.string.label -text "Search string:" -width 13 -anchor w
##entry $w.string.entry -width 40 -textvariable searchString
##button $w.string.button -text "Highlight" \
##	-command "textSearch $w.text \$searchString search"
##pack $w.string.label $w.string.entry -side left
##pack $w.string.button -side left -pady 5 -padx 10
##bind $w.string.entry <Return> "textSearch $w.text \$searchString search"
def textSearch(w, string, tag):
    w.tag_remove('search', 0.0, END)
    if string == '':
        return
    cur = 1.0
    length=0
    while True:
        cur = w.search(count=length, string, cur, END)
        if cur == '':
            break
        w.tag_add(tag, cur, '%i + %i char' % (cur, length))
        cur = w.index('%i + %i char' % (cur, length))
##proc textSearch {w string tag} {
##    $w tag remove search 0.0 end
##    if {$string == ""} {
##	return
##    }
##    set cur 1.0
##    while 1 {
##	set cur [$w search -count length $string $cur end]
##	if {$cur == ""} {
##	    break
##	}
##	$w tag add $tag $cur "$cur + $length char"
##	set cur [$w index "$cur + $length char"]
##    }
##}
string = Frame(w)
label = Label(string, text="Search string:", width=13, anchor='w')
searchString = StringVar()
entry2 = Entry(string, width=40, textvariable=searchString)
button = Button(string, text='Highlight',
                command=lambda t=text, f=textSearch:
                    f(t, '$searchString', 'search'))
label.pack(side='left')
entry2.pack(side='left')
button.pack(side='left', pady=5, padx=10)
entry2.bind('<Return>',
           lambda e, t=text, f=textSearch: f(t, '$searchString', 'search'))
entry1.bind('<Return>',
           lambda e, t=text, var=fileName, entry=entry2, f=textLoadFile:
               f(t, var.get()) and entry.focus())

##text $w.text -yscrollcommand "$w.scroll set" -setgrid true
##scrollbar $w.scroll -command "$w.text yview"
##pack $w.file $w.string -side top -fill x
##pack $w.scroll -side right -fill y
##pack $w.text -expand yes -fill both
#text = Text(w, setgrid=True)
scroll = Scrollbar(w, command=text.yview)
text['yscrollcommand'] = scroll.set
file.pack(side='top', fill='x')
string.pack(side='top', fill='x')
scroll.pack(side='right', fill='y')
text.pack(expand='yes', fill='both')

# Set up display styles for text highlighting.

##if {[winfo depth $w] > 1} {
##    textToggle "$w.text tag configure search -background \
##	    #ce5555 -foreground white" 800 "$w.text tag configure \
##	    search -background {} -foreground {}" 200
##} else {
##    textToggle "$w.text tag configure search -background \
##	    black -foreground white" 800 "$w.text tag configure \
##	    search -background {} -foreground {}" 200
##}
##$w.text insert 1.0 \
##{This window demonstrates how to use the tagging facilities in text
##widgets to implement a searching mechanism.  First, type a file name
##in the top entry, then type <Return> or click on "Load File".  Then
##type a string in the lower entry and type <Return> or click on
##"Load File".  This will cause all of the instances of the string to
##be tagged with the tag "search", and it will arrange for the tag's
##display attributes to change to make all of the strings blink.}
##$w.text mark set insert 0.0
##
##set fileName ""
##set searchString ""
def textToggle(cmd1, sleep1, cmd2, sleep2):
    global w
    cmd1()
    w.after(sleep1, lambda: textToggle(cmd2, sleep2, cmd1, sleep1))
##proc textToggle {cmd1 sleep1 cmd2 sleep2} {
##    catch {
##	eval $cmd1
##	after $sleep1 [list textToggle $cmd2 $sleep2 $cmd1 $sleep1]
##    }
##}
if w.winfo_depth() > 1:
##    textToggle(lambda: text.tag_configure('search', background='#ce5555',
##                                          foreground='white'),
##               800,
##               lambda: text.tag_configure('search', background='',
##                                          foreground='')
##               200)
    pass
else:
##    textToggle(lambda: text.tag_configure('search', background='black',
##                                          foreground='white'),
##               800,
##               lambda: text.tag_configure('search', background='',
##                                          foreground='')
##               200)
    pass
text.insert(1.0,
"""This window demonstrates how to use the tagging facilities in text
widgets to implement a searching mechanism.  First, type a file name
in the top entry, then type <Return> or click on "Load File".  Then
type a string in the lower entry and type <Return> or click on
"Load File".  This will cause all of the instances of the string to
be tagged with the tag "search", and it will arrange for the tag's
display attributes to change to make all of the strings blink.""")
text.mark_set('insert', 0.0)
fileName.set('')
searchString.set('')
