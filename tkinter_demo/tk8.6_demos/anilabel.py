# anilabel.tcl --
#
# This demonstration script creates a toplevel window containing
# several animated label widgets.

##if {![info exists widgetDemo]} {
##    error "This script should be run from the \"widget\" demo."
##}
assert 'widgetDemo' in globals(), \
'This script should be run from the "widget" demo.'

##package require Tk

##set w .anilabel
##catch {destroy $w}
##toplevel $w
##wm title $w "Animated Label Demonstration"
##wm iconname $w "anilabel"
##positionWindow $w
demo_name = 'anilabel'
if demo_name in globals():
    globals()[demo_name].destroy()
w = globals()[demo_name] = Toplevel(root)
w.wm_title('Animated Label Demonstration')
w.wm_iconname('anilabel')
positionWindow(w)

##label $w.msg -font $font -wraplength 4i -justify left -text "Four animated labels are displayed below; each of the labels on the left is animated by making the text message inside it appear to scroll, and the label on the right is animated by animating the image that it displays."
##pack $w.msg -side top
msg=Label(w, font=font, wraplength='4i', justify=LEFT, text="Four animated labels are displayed below; each of the labels on the left is animated by making the text message inside it appear to scroll, and the label on the right is animated by animating the image that it displays.")
msg.pack(side=TOP)

#### See Code / Dismiss buttons
##set btns [addSeeDismiss $w.buttons $w]
##pack $btns -side bottom -fill x
btns = addSeeDismiss(ttk.Frame(w), demo_name)
btns.pack(side=BOTTOM, fill=X)

# Ensure that this this is an array
##array set animationCallbacks {}
animationCallbacks = {}

## This callback is the core of how to do animation in Tcl/Tk; all
## animations work in basically the same way, with a procedure that
## uses the [after] command to reschedule itself at some point in the
## future. Of course, the details of how to update the state will vary
## according to what is being animated.
##proc RotateLabelText {w interval} {
##    global animationCallbacks
##
##    # Schedule the calling of this procedure again in the future
##    set animationCallbacks($w) [after $interval RotateLabelText $w $interval]
##
##    # We do marquee-like scrolling text by chopping characters off the
##    # front of the text and sticking them on the end.
##    set text [$w cget -text]
##    set newText [string range $text 1 end][string index $text 0]
##    $w configure -text $newText
##}
def RotateLabelText(w, interval):
    global animationCallbacks
    animationCallbacks[w] = \
        w.after(interval, lambda: RotateLabelText(w, interval))
    text = w.cget('text')
    newText = text[1:] + text[0]
    w.configure(text=newText)

## A helper procedure to start the animation happening.
##proc animateLabelText {w text interval} {
##    global animationCallbacks
##
##    # Install the text into the widget
##    $w configure -text $text
##
##    # Schedule the start of the animation loop
##    set animationCallbacks($w) [after $interval RotateLabelText $w $interval]
##
##    # Make sure that the animation stops and is cleaned up after itself
##    # when the animated label is destroyed.  Note that at this point we
##    # cannot manipulate the widget itself, as that has already died.
##    bind $w <Destroy> {
##	after cancel $animationCallbacks(%W)
##	unset animationCallbacks(%W)
##    }
##}
def animateLabelText(w, text, interval):
    global animationCallbacks
    w.configure(text=text)
    animationCallbacks[w] = \
        w.after(interval, lambda: RotateLabelText(w, interval))
    def destory_callback(e):
        w.after_cancel(animationCallbacks[e.widget])
        del animationCallbacks[e.widget]
    w.bind('<Destroy>', destory_callback)

## Next, a similar pair of procedures to animate a GIF loaded into a
## photo image.
##proc SelectNextImageFrame {w interval} {
##    global animationCallbacks
##    set animationCallbacks($w) \
##	    [after $interval SelectNextImageFrame $w $interval]
##    set image [$w cget -image]
##
##    # The easy way to animate a GIF!
##    set idx -1
##    scan [$image cget -format] "GIF -index %d" idx
##    if {[catch {
##	# Note that we get an error if the index is out of range
##	$image configure -format "GIF -index [incr idx]"
##    }]} then {
##	$image configure -format "GIF -index 0"
##    }
##}
##proc animateLabelImage {w imageData interval} {
##    global animationCallbacks
##
##    # Create a multi-frame GIF from base-64-encoded data
##    set image [image create photo -format GIF -data $imageData]
##
##    # Install the image into the widget
##    $w configure -image $image
##
##    # Schedule the start of the animation loop
##    set animationCallbacks($w) \
##	    [after $interval SelectNextImageFrame $w $interval]
##
##    # Make sure that the animation stops and is cleaned up after itself
##    # when the animated label is destroyed.  Note that at this point we
##    # cannot manipulate the widget itself, as that has already died.
##    # Also note that this script is in double-quotes; this is always OK
##    # because image names are chosen automatically to be simple words.
##    bind $w <Destroy> "
##	after cancel \$animationCallbacks(%W)
##	unset animationCallbacks(%W)
##	rename $image {}
##    "
##}
def SelectNextImageFrame(w, interval):
    global animationCallbacks
    animationCallbacks[w] = \
        w.after(interval, lambda: SelectNextImageFrame(w, interval))
    #image = w.cget('image')
    image = w.image
    idx = -1
    # image.cget('format') -> ('GIF',)
    # image.cget('format') -> ('GIF', <index object: '-index'>, 1)
    if len(image.cget('format')) > 1:
        idx = int(image.cget('format')[-1])
    try:
        idx += 1
        image.configure(format='GIF -index '+str(idx))
    except:
        image.configure(format='GIF -index 0')
def animateLabelImage(w, imageData, interval):
    global animationCallbacks
    w.image = image = PhotoImage(format='GIF', data=imageData)
    w.configure(image=image)
    animationCallbacks[w] = \
        w.after(interval, lambda: SelectNextImageFrame(w, interval))
    def destroy_callback(e):
        w.after_cancel(animationCallbacks[e.widget])
        del animationCallbacks[e.widget]
        image = None
    w.bind('<Destroy>', destroy_callback)
globals().update(locals())

# Make some widgets to contain the animations
##labelframe $w.left -text "Scrolling Texts"
##labelframe $w.right -text "GIF Image"
##pack $w.left $w.right -side left -padx 10 -pady 10 -expand yes
left = LabelFrame(w, text='Scrolling Texts')
right = LabelFrame(w, text='GIF Image')
for ww in left, right:
    ww.pack(side=LEFT, padx=10, pady=10, expand=YES)

# This method of scrolling text looks far better with a fixed-width font
##label $w.left.l1 -bd 4 -relief ridge -font fixedFont
##label $w.left.l2 -bd 4 -relief groove -font fixedFont
##label $w.left.l3 -bd 4 -relief flat -font fixedFont -width 18
##pack $w.left.l1 $w.left.l2 $w.left.l3 -side top -expand yes -padx 10 -pady 10 -anchor w
### Don't need to do very much with this label except turn off the border
##label $w.right.l -bd 0
##pack $w.right.l -side top -expand yes -padx 10 -pady 10
l1 = Label(left, bd=4, relief='ridge', font=fixedFont)
l2 = Label(left, bd=4, relief='groove', font=fixedFont)
l3 = Label(left, bd=4, relief='flat', font=fixedFont, width=18)
for ww in l1, l2, l3:
    ww.pack(side=TOP, expand=YES, padx=10, pady=10, anchor=W)
l = Label(right, bd=0)
l.pack(side=TOP, expand=YES, padx=10, pady=10)

# This is a base-64-encoded animated GIF file.
##set tclPoweredData {
##    R0lGODlhKgBAAPQAAP//////zP//AP/MzP/Mmf/MAP+Zmf+ZZv+ZAMz//8zM
##    zMyZmcyZZsxmZsxmAMwzAJnMzJmZzJmZmZlmmZlmZplmM5kzM2aZzGZmzGZm
##    mWZmZmYzZmYzMzNmzDMzZgAzmSH+IE1hZGUgd2l0aCBHSU1QIGJ5IExARGVt
##    YWlsbHkuY29tACH5BAVkAAEALAAAAAAqAEAAAAX+YCCOZEkyTKM2jOm66yPP
##    dF03bx7YcuHIDkGBR7SZeIyhTID4FZ+4Es8nQyCe2EeUNJ0peY2s9mi7PhAM
##    ngEAMGRbUpvzSxskLh1J+Hkg134OdDIDEB+GHxtYMEQMTjMGEYeGFoomezaC
##    DZGSHFmLXTQKkh8eNQVpZ2afmDQGHaOYSoEyhhcklzVmMpuHnaZmDqiGJbg0
##    qFqvh6UNAwB7VA+OwydEjgujkgrPNhbTI8dFvNgEYcHcHx0lB1kX2IYeA2G6
##    NN0YfkXJ2BsAMuAzHB9cZMk3qoEbRzUACsRCUBK5JxsC3iMiKd8GN088SIyT
##    0RAFSROyeEg38caDiB/+JEgqxsODrZJ1BkT0oHKSmI0ceQxo94HDpg0qsuDk
##    UmRAMgu8OgwQ+uIJgUMVeGXA+IQkzEeHGvD8cIGlDXsLiRjQ+EHroQhea7xY
##    8IQBSgYYDi1IS+OFBCgaDMGVS3fGi5BPJpBaENdQ0EomKGD56IHwO39EXiSC
##    Ysgxor5+Xfgq0qByYUpiXmwuoredB2aYH4gWWda0B7SeNENpEJHC1ghi+pS4
##    AJpIAwWvKPBi+8YEht5EriEqpFfMlhEdkBNpx0HUhwypx5T4IB1MBg/Ws2sn
##    wV3MSQOkzI8fUd48Aw3dOZto71x85hHtHijYv18Gf/3GqCdDCXHNoICBobSo
##    IqBqJLyCoH8JPrLgdh88CKCFD0CGmAiGYPgffwceZh6FC2ohIIklnkhehTNY
##    4CIHHGzgwYw01ujBBhvAqKOLLq5AAk9kuSPkkKO40NB+h1gnypJIIvkBf09a
##    N5QIRz5p5ZJXJpmlIVhOGQA2TmIJZZhKKmmll2BqyWSXWUrZpQtpatlmk1c2
##    KaWRHeTZEJF8SqLDn/hhsOeQgBbqAh6DGqronxeARUIIACH5BAUeAAAALAUA
##    LgAFAAUAAAUM4CeKz/OV5YmqaRkCACH5BAUeAAEALAUALgAKAAUAAAUUICCK
##    z/OdJVCaa7p+7aOWcDvTZwgAIfkEBR4AAQAsCwAuAAkABQAABRPgA4zP95zA
##    eZqoWqqpyqLkZ38hACH5BAUKAAEALAcALgANAA4AAAU7ICA+jwiUJEqeKau+
##    r+vGaTmac63v/GP9HM7GQyx+jsgkkoRUHJ3Qx0cK/VQVTKtWwbVKn9suNunc
##    WkMAIfkEBQoAAAAsBwA3AAcABQAABRGgIHzk842j+Yjlt5KuO8JmCAAh+QQF
##    CgAAACwLADcABwAFAAAFEeAnfN9TjqP5oOWziq05lmUIACH5BAUKAAAALA8A
##    NwAHAAUAAAUPoPCJTymS3yiQj4qOcPmEACH5BAUKAAAALBMANwAHAAUAAAUR
##    oCB+z/MJX2o+I2miKimiawgAIfkEBQoAAAAsFwA3AAcABQAABRGgIHzfY47j
##    Q4qk+aHl+pZmCAAh+QQFCgAAACwbADcABwAFAAAFEaAgfs/zCV9qPiNJouo7
##    ll8IACH5BAUKAAAALB8ANwADAAUAAAUIoCB8o0iWZggAOw==
##}
tclPoweredData = """
    R0lGODlhKgBAAPQAAP//////zP//AP/MzP/Mmf/MAP+Zmf+ZZv+ZAMz//8zM
    zMyZmcyZZsxmZsxmAMwzAJnMzJmZzJmZmZlmmZlmZplmM5kzM2aZzGZmzGZm
    mWZmZmYzZmYzMzNmzDMzZgAzmSH+IE1hZGUgd2l0aCBHSU1QIGJ5IExARGVt
    YWlsbHkuY29tACH5BAVkAAEALAAAAAAqAEAAAAX+YCCOZEkyTKM2jOm66yPP
    dF03bx7YcuHIDkGBR7SZeIyhTID4FZ+4Es8nQyCe2EeUNJ0peY2s9mi7PhAM
    ngEAMGRbUpvzSxskLh1J+Hkg134OdDIDEB+GHxtYMEQMTjMGEYeGFoomezaC
    DZGSHFmLXTQKkh8eNQVpZ2afmDQGHaOYSoEyhhcklzVmMpuHnaZmDqiGJbg0
    qFqvh6UNAwB7VA+OwydEjgujkgrPNhbTI8dFvNgEYcHcHx0lB1kX2IYeA2G6
    NN0YfkXJ2BsAMuAzHB9cZMk3qoEbRzUACsRCUBK5JxsC3iMiKd8GN088SIyT
    0RAFSROyeEg38caDiB/+JEgqxsODrZJ1BkT0oHKSmI0ceQxo94HDpg0qsuDk
    UmRAMgu8OgwQ+uIJgUMVeGXA+IQkzEeHGvD8cIGlDXsLiRjQ+EHroQhea7xY
    8IQBSgYYDi1IS+OFBCgaDMGVS3fGi5BPJpBaENdQ0EomKGD56IHwO39EXiSC
    Ysgxor5+Xfgq0qByYUpiXmwuoredB2aYH4gWWda0B7SeNENpEJHC1ghi+pS4
    AJpIAwWvKPBi+8YEht5EriEqpFfMlhEdkBNpx0HUhwypx5T4IB1MBg/Ws2sn
    wV3MSQOkzI8fUd48Aw3dOZto71x85hHtHijYv18Gf/3GqCdDCXHNoICBobSo
    IqBqJLyCoH8JPrLgdh88CKCFD0CGmAiGYPgffwceZh6FC2ohIIklnkhehTNY
    4CIHHGzgwYw01ujBBhvAqKOLLq5AAk9kuSPkkKO40NB+h1gnypJIIvkBf09a
    N5QIRz5p5ZJXJpmlIVhOGQA2TmIJZZhKKmmll2BqyWSXWUrZpQtpatlmk1c2
    KaWRHeTZEJF8SqLDn/hhsOeQgBbqAh6DGqronxeARUIIACH5BAUeAAAALAUA
    LgAFAAUAAAUM4CeKz/OV5YmqaRkCACH5BAUeAAEALAUALgAKAAUAAAUUICCK
    z/OdJVCaa7p+7aOWcDvTZwgAIfkEBR4AAQAsCwAuAAkABQAABRPgA4zP95zA
    eZqoWqqpyqLkZ38hACH5BAUKAAEALAcALgANAA4AAAU7ICA+jwiUJEqeKau+
    r+vGaTmac63v/GP9HM7GQyx+jsgkkoRUHJ3Qx0cK/VQVTKtWwbVKn9suNunc
    WkMAIfkEBQoAAAAsBwA3AAcABQAABRGgIHzk842j+Yjlt5KuO8JmCAAh+QQF
    CgAAACwLADcABwAFAAAFEeAnfN9TjqP5oOWziq05lmUIACH5BAUKAAAALA8A
    NwAHAAUAAAUPoPCJTymS3yiQj4qOcPmEACH5BAUKAAAALBMANwAHAAUAAAUR
    oCB+z/MJX2o+I2miKimiawgAIfkEBQoAAAAsFwA3AAcABQAABRGgIHzfY47j
    Q4qk+aHl+pZmCAAh+QQFCgAAACwbADcABwAFAAAFEaAgfs/zCV9qPiNJouo7
    ll8IACH5BAUKAAAALB8ANwADAAUAAAUIoCB8o0iWZggAOw=="""

# Finally, set up the text scrolling animation
##animateLabelText $w.left.l1 "* Slow Animation *" 300
##animateLabelText $w.left.l2 "* Fast Animation *" 80
##animateLabelText $w.left.l3 "This is a longer scrolling text in a widget that will not show the whole message at once. " 150
##animateLabelImage $w.right.l $tclPoweredData 100
animateLabelText(l1, "* Slow Animation *", 300)
animateLabelText(l2, "* Fast Animation *", 80)
animateLabelText(l3, "This is a longer scrolling text in a widget that will not show the whole message at once. ", 150)
animateLabelImage(l, tclPoweredData, 100)
