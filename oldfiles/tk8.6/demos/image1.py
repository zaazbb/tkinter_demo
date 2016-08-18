# image1.tcl --
#
# This demonstration script displays two image widgets.

##if {![info exists widgetDemo]} {
##    error "This script should be run from the \"widget\" demo."
##}
assert 'widgetDemo' in globals(), \
'This script should be run from the "widget" demo.'

##package require Tk
from tkinter import *

##set w .image1
##catch {destroy $w}
##toplevel $w
##wm title $w "Image Demonstration #1"
##wm iconname $w "Image1"
##positionWindow $w
demo_name = 'image1'
if demo_name in globals()['demo_name']:
    globals()['demo_name'][demo_name].destroy()
w = globals()['demo_name'][demo_name] = Toplevel(root)
w.wm_title('Image Demonstration #1')
w.wm_iconname('Image1')
positionWindow(w)

##label $w.msg -font $font -wraplength 4i -justify left -text "This demonstration displays two images, each in a separate label widget."
##pack $w.msg -side top
msg = Label(w, font=font_, wraplength='4i', justify='left', text="This demonstration displays two images, each in a separate label widget.")
msg.pack(side='top')

## See Code / Dismiss buttons
##set btns [addSeeDismiss $w.buttons $w]
##pack $btns -side bottom -fill x
btns = addSeeDismiss(ttk.Frame(w), demo_name)
btns.pack(side='bottom', fill='x')

# Main widget program sets variable tk_demoDirectory
##catch {image delete image1a}
##image create photo image1a -file [file join $tk_demoDirectory images earth.gif]
##label $w.l1 -image image1a -bd 1 -relief sunken
import os.path
image1a = PhotoImage(file=os.path.join(tk_demoDirectory, 'images', 'earth.gif'))
l1 = Label(w, image=image1a, bd=1, relief='sunken')
# keep a reference
l1.image=image1a

##catch {image delete image1b}
##image create photo image1b \
##	-file [file join $tk_demoDirectory images earthris.gif]
##label $w.l2 -image image1b -bd 1 -relief sunken
image1b = PhotoImage(file=os.path.join(tk_demoDirectory, 'images', 'earthris.gif'))
l2 = Label(w, image=image1b, bd=1, relief='sunken')
# keep a reference
l2.image=image1b

##pack $w.l1 $w.l2 -side top -padx .5m -pady .5m
for w in [l1, l2]: w.pack(side='top', padx='.5m', pady='.5m')
