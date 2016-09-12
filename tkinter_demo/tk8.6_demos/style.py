# style.tcl --
#
# This demonstration script creates a text widget that illustrates the
# various display styles that may be set for tags.

##if {![info exists widgetDemo]} {
##    error "This script should be run from the \"widget\" demo."
##}
assert 'widgetDemo' in globals(), \
'This script should be run from the "widget" demo.'

##package require Tk
from tkinter import *

##set w .style
##catch {destroy $w}
##toplevel $w
##wm title $w "Text Demonstration - Display Styles"
##wm iconname $w "style"
##positionWindow $w
demo_name = 'style'
if demo_name in globals()['demo_name']:
    globals()['demo_name'][demo_name].destroy()
w = globals()['demo_name'][demo_name] = Toplevel(root)
w.wm_title('Text Demonstration - Display Styles')
w.wm_iconname('style')
positionWindow(w)

## See Code / Dismiss buttons
##set btns [addSeeDismiss $w.buttons $w]
##pack $btns -side bottom -fill x
btns = addSeeDismiss(ttk.Frame(w), demo_name)
btns.pack(side='bottom', fill='x')

# Only set the font family in one place for simplicity and consistency

##set family Courier
##
##text $w.text -yscrollcommand "$w.scroll set" -setgrid true \
##	-width 70 -height 32 -wrap word -font "$family 12"
##scrollbar $w.scroll -command "$w.text yview"
##pack $w.scroll -side right -fill y
##pack $w.text -expand yes -fill both
family = 'Courier'
text = Text(w, setgrid=True, width=70, height=32, wrap='word',
            font='%s 12' % family)
scroll = Scrollbar(w, command=text.yview)
text['yscrollcommand'] = scroll.set
scroll.pack(side='right', fill='y')
text.pack(expand='yes', fill='both')

# Set up display styles

##$w.text tag configure bold -font "$family 12 bold italic"
##$w.text tag configure big -font "$family 14 bold"
##$w.text tag configure verybig -font "Helvetica 24 bold"
##$w.text tag configure tiny -font "Times 8 bold"
##if {[winfo depth $w] > 1} {
##    $w.text tag configure color1 -background #a0b7ce
##    $w.text tag configure color2 -foreground red
##    $w.text tag configure raised -relief raised -borderwidth 1
##    $w.text tag configure sunken -relief sunken -borderwidth 1
##} else {
##    $w.text tag configure color1 -background black -foreground white
##    $w.text tag configure color2 -background black -foreground white
##    $w.text tag configure raised -background white -relief raised \
##	    -borderwidth 1
##    $w.text tag configure sunken -background white -relief sunken \
##	    -borderwidth 1
##}
##$w.text tag configure bgstipple -background black -borderwidth 0 \
##	-bgstipple gray12
##$w.text tag configure fgstipple -fgstipple gray50
##$w.text tag configure underline -underline on
##$w.text tag configure overstrike -overstrike on
##$w.text tag configure right -justify right
##$w.text tag configure center -justify center
##$w.text tag configure super -offset 4p -font "$family 10"
##$w.text tag configure sub -offset -2p -font "$family 10"
##$w.text tag configure margins -lmargin1 12m -lmargin2 6m -rmargin 10m
##$w.text tag configure spacing -spacing1 10p -spacing2 2p \
##	-lmargin1 12m -lmargin2 6m -rmargin 10m
text.tag_configure('bold', font='%s 12 bold italic' % family)
text.tag_configure('big', font='%s 14 bold' % family)
text.tag_configure('verybig',
                   font=text.tk.call('font', 'actual', 'Helvetica 24 bold'))
text.tag_configure('tiny',
                   font=text.tk.call('font', 'actual', 'Times 8 bold'))
if w.winfo_depth() > 1:
    text.tag_configure('color1', background='#a0b7ce')
    text.tag_configure('color2', foreground='red')
    text.tag_configure('raised', relief='raised', borderwidth=1)
    text.tag_configure('sunken', relief='sunken', borderwidth=1)
else:
    text.tag_configure('color1', background='black', foreground='white')
    text.tag_configure('color2', background='black', foreground='white')
    text.tag_configure('raised', background='white', relief='raised',
                       borderwidth=1)
    text.tag_configure('sunken', background='white', relief='sunken',
                       borderwidth=1)
text.tag_configure('bgstipple', background='black', borderwidth=0,
                   bgstipple='gray12')
text.tag_configure('fgstipple', fgstipple='gray50')
text.tag_configure('underline', underline='on')
text.tag_configure('overstrike', overstrike='on')
text.tag_configure('right', justify='right')
text.tag_configure('center', justify='center')
text.tag_configure('super', offset='4p', font='%s  10' % family)
text.tag_configure('sub', offset='2p', font='%s  10' % family)
text.tag_configure('margins', lmargin1='12m', lmargin2='6m', rmargin='10m')
text.tag_configure('spacing', spacing1='10p', spacing2='2p',
                   lmargin1='12m', lmargin2='6m', rmargin='10m')

##$w.text insert end {Text widgets like this one allow you to display information in a
##variety of styles.  Display styles are controlled using a mechanism
##called }
##$w.text insert end tags bold
##$w.text insert end {.  Tags are just textual names that you can apply to one
##or more ranges of characters within a text widget.  You can configure
##tags with various display styles.  If you do this, then the tagged
##characters will be displayed with the styles you chose.  The
##available display styles are:
##}
##$w.text insert end "\n1. Font." big
##$w.text insert end "  You can choose any system font, "
##$w.text insert end large verybig
##$w.text insert end " or "
##$w.text insert end "small" tiny ".\n"
##$w.text insert end "\n2. Color." big
##$w.text insert end "  You can change either the "
##$w.text insert end background color1
##$w.text insert end " or "
##$w.text insert end foreground color2
##$w.text insert end "\ncolor, or "
##$w.text insert end both {color1 color2}
##$w.text insert end ".\n"
##$w.text insert end "\n3. Stippling." big
##$w.text insert end "  You can cause either the "
##$w.text insert end background bgstipple
##$w.text insert end " or "
##$w.text insert end foreground fgstipple
##$w.text insert end {
##information to be drawn with a stipple fill instead of a solid fill.
##}
##$w.text insert end "\n4. Underlining." big
##$w.text insert end "  You can "
##$w.text insert end underline underline
##$w.text insert end " ranges of text.\n"
##$w.text insert end "\n5. Overstrikes." big
##$w.text insert end "  You can "
##$w.text insert end "draw lines through" overstrike
##$w.text insert end " ranges of text.\n"
##$w.text insert end "\n6. 3-D effects." big
##$w.text insert end {  You can arrange for the background to be drawn
##with a border that makes characters appear either }
##$w.text insert end raised raised
##$w.text insert end " or "
##$w.text insert end sunken sunken
##$w.text insert end ".\n"
##$w.text insert end "\n7. Justification." big
##$w.text insert end " You can arrange for lines to be displayed\n"
##$w.text insert end "left-justified,\n"
##$w.text insert end "right-justified, or\n" right
##$w.text insert end "centered.\n" center
##$w.text insert end "\n8. Superscripts and subscripts."  big
##$w.text insert end " You can control the vertical\n"
##$w.text insert end "position of text to generate superscript effects like 10"
##$w.text insert end "n" super
##$w.text insert end " or\nsubscript effects like X"
##$w.text insert end "i" sub
##$w.text insert end ".\n"
##$w.text insert end "\n9. Margins." big
##$w.text insert end " You can control the amount of extra space left"
##$w.text insert end " on\neach side of the text:\n"
##$w.text insert end "This paragraph is an example of the use of " margins
##$w.text insert end "margins.  It consists of a single line of text " margins
##$w.text insert end "that wraps around on the screen.  There are two " margins
##$w.text insert end "separate left margin values, one for the first " margins
##$w.text insert end "display line associated with the text line, " margins
##$w.text insert end "and one for the subsequent display lines, which " margins
##$w.text insert end "occur because of wrapping.  There is also a " margins
##$w.text insert end "separate specification for the right margin, " margins
##$w.text insert end "which is used to choose wrap points for lines.\n" margins
##$w.text insert end "\n10. Spacing." big
##$w.text insert end " You can control the spacing of lines with three\n"
##$w.text insert end "separate parameters.  \"Spacing1\" tells how much "
##$w.text insert end "extra space to leave\nabove a line, \"spacing3\" "
##$w.text insert end "tells how much space to leave below a line,\nand "
##$w.text insert end "if a text line wraps, \"spacing2\" tells how much "
##$w.text insert end "space to leave\nbetween the display lines that "
##$w.text insert end "make up the text line.\n"
##$w.text insert end "These indented paragraphs illustrate how spacing " spacing
##$w.text insert end "can be used.  Each paragraph is actually a " spacing
##$w.text insert end "single line in the text widget, which is " spacing
##$w.text insert end "word-wrapped by the widget.\n" spacing
##$w.text insert end "Spacing1 is set to 10 points for this text, " spacing
##$w.text insert end "which results in relatively large gaps between " spacing
##$w.text insert end "the paragraphs.  Spacing2 is set to 2 points, " spacing
##$w.text insert end "which results in just a bit of extra space " spacing
##$w.text insert end "within a pararaph.  Spacing3 isn't used " spacing
##$w.text insert end "in this example.\n" spacing
##$w.text insert end "To see where the space is, select ranges of " spacing
##$w.text insert end "text within these paragraphs.  The selection " spacing
##$w.text insert end "highlight will cover the extra space." spacing
text.insert('end', """Text widgets like this one allow you to display information in a
variety of styles.  Display styles are controlled using a mechanism
called """)
text.insert('end', 'tags', 'bold')
text.insert('end', """.  Tags are just textual names that you can apply to one
or more ranges of characters within a text widget.  You can configure
tags with various display styles.  If you do this, then the tagged
characters will be displayed with the styles you chose.  The
available display styles are:
""")
text.insert('end', "\n1. Font.", 'big')
text.insert('end', "  You can choose any system font, ")
text.insert('end', 'large', 'verybig')
text.insert('end', " or ")
text.insert('end', "small", 'tiny', ".\n")
text.insert('end', "\n2. Color.", 'big')
text.insert('end', "  You can change either the ")
text.insert('end', 'background', 'color1')
text.insert('end', " or ")
text.insert('end', 'foreground', 'color2')
text.insert('end', "\ncolor, or ")
text.insert('end', 'both', 'color1 color2')
text.insert('end', ".\n")
text.insert('end', "\n3. Stippling.", 'big')
text.insert('end', "  You can cause either the ")
text.insert('end', 'background', 'bgstipple')
text.insert('end', " or ")
text.insert('end', 'foreground', 'fgstipple')
text.insert('end', """
information to be drawn with a stipple fill instead of a solid fill.
""")
text.insert('end', "\n4. Underlining.", 'big')
text.insert('end', "  You can ")
text.insert('end', 'underline', 'underline')
text.insert('end', " ranges of text.\n")
text.insert('end', "\n5. Overstrikes.", 'big')
text.insert('end', "  You can ")
text.insert('end', "draw lines through", 'overstrike')
text.insert('end', " ranges of text.\n")
text.insert('end', "\n6. 3-D effects.", 'big')
text.insert('end', """  You can arrange for the background to be drawn
with a border that makes characters appear either """)
text.insert('end', 'raised', 'raised')
text.insert('end', " or ")
text.insert('end', 'sunken', 'sunken')
text.insert('end', ".\n")
text.insert('end', "\n7. Justification.", 'big')
text.insert('end', " You can arrange for lines to be displayed\n")
text.insert('end', "left-justified,\n")
text.insert('end', "right-justified, or\n", 'right')
text.insert('end', "centered.\n", 'center')
text.insert('end', "\n8. Superscripts and subscripts.",  'big')
text.insert('end', " You can control the vertical\n")
text.insert('end', "position of text to generate superscript effects like 10")
text.insert('end', "n" 'super')
text.insert('end', " or\nsubscript effects like X")
text.insert('end', "i", 'sub')
text.insert('end', ".\n")
text.insert('end', "\n9. Margins.", 'big')
text.insert('end', " You can control the amount of extra space left")
text.insert('end', " on\neach side of the text:\n")
text.insert('end', "This paragraph is an example of the use of ", 'margins')
text.insert('end', "margins.  It consists of a single line of text ", 'margins')
text.insert('end', "that wraps around on the screen.  There are two ", 'margins')
text.insert('end', "separate left margin values, one for the first ", 'margins')
text.insert('end', "display line associated with the text line, ", 'margins')
text.insert('end', "and one for the subsequent display lines, which ", 'margins')
text.insert('end', "occur because of wrapping.  There is also a ", 'margins')
text.insert('end', "separate specification for the right margin, ", 'margins')
text.insert('end', "which is used to choose wrap points for lines.\n", 'margins')
text.insert('end', "\n10. Spacing.", 'big')
text.insert('end', " You can control the spacing of lines with three\n")
text.insert('end', "separate parameters.  \"Spacing1\" tells how much ")
text.insert('end', "extra space to leave\nabove a line, \"spacing3\" ")
text.insert('end', "tells how much space to leave below a line,\nand ")
text.insert('end', "if a text line wraps, \"spacing2\" tells how much ")
text.insert('end', "space to leave\nbetween the display lines that ")
text.insert('end', "make up the text line.\n")
text.insert('end', "These indented paragraphs illustrate how spacing ", 'spacing')
text.insert('end', "can be used.  Each paragraph is actually a ", 'spacing')
text.insert('end', "single line in the text widget, which is ", 'spacing')
text.insert('end', "word-wrapped by the widget.\n", 'spacing')
text.insert('end', "Spacing1 is set to 10 points for this text, ", 'spacing')
text.insert('end', "which results in relatively large gaps between ", 'spacing')
text.insert('end', "the paragraphs.  Spacing2 is set to 2 points, ", 'spacing')
text.insert('end', "which results in just a bit of extra space ", 'spacing')
text.insert('end', "within a pararaph.  Spacing3 isn't used ", 'spacing')
text.insert('end', "in this example.\n", 'spacing')
text.insert('end', "To see where the space is, select ranges of ", 'spacing')
text.insert('end', "text within these paragraphs.  The selection ", 'spacing')
text.insert('end', "highlight will cover the extra space.", 'spacing')