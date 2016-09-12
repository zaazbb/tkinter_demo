
import tkinter
from tkinter import tix



# tkinter Standard Widgets
def Mk_tkinterStd0(nb, name):
    w = nb.page(name)
    button = tkinter.Button(w).grid(column=0, row=0)
    canvas = tkinter.Canvas(w).grid(column=1, row=0)
    checkbutton = tkinter.Checkbutton(w).grid(column=2, row=0)
    entry = tkinter.Entry(w).grid(column=3, row=0)
    frame = tkinter.Frame(w).grid(column=0, row=1)
    label = tkinter.Label(w).grid(column=1, row=1)
    listbox = tkinter.Listbox(w).grid(column=2, row=1)
    menu = tkinter.Menu(w)#.grid(column=3, row=1)
def Mk_tkinterStd1(nb, name):
    w = nb.page(name)
    menubutton = tkinter.Menubutton(w).grid(column=0, row=0)
    message = tkinter.Message(w).grid(column=1, row=0)
    radiobutton = tkinter.Radiobutton(w).grid(column=2, row=0)
    scale = tkinter.Scale(w).grid(column=3, row=0)
    scrollbar = tkinter.Scrollbar(w).grid(column=0, row=1)
    text = tkinter.Text(w).grid(column=1, row=1)
##    optionmenu = tkinter.OptionMenu(w)#.grid(column=2, row=1)
##    photoimage = tkinter.PhotoImage(w)#.grid(column=3, row=1)
def Mk_tkinterStd2(nb, name):
    w = nb.page(name)
##    bitmapimage = tkinter.BitmapImage(w)#.grid(column=0, row=0)
    spinbox = tkinter.Spinbox(w).grid(column=1, row=0)
    labelframe = tkinter.LabelFrame(w)#.grid(column=2, row=0)
    panedwindow = tkinter.PanedWindow(w).grid(column=3, row=0)
##    studbutton = tkinter.Studbutton(w).grid(column=0, row=1)
##    tributton = tkinter.Tributton(w).grid(column=1, row=1)

# Tix Standard Widgets
def Mk_tixStd(nb, name):
    w = nb.page(name)
    tixGrid                 = tix.Grid(w).grid(column=0, row=0)
    tixHList                = tix.HList(w).grid(column=1, row=0)
    # tixInputOnly, Unix only.
##    tixInputOnly            = tix.InputOnly(root).grid(column=2, row=0) 
##    tixNBFrame              = tix.NBFrame(root).grid(column=3, row=0)
    # tixNoteBookFrame, only pass in py33.
##    tixNoteBookFrame        = tix.NoteBookFrame(w)
    tixTList                = tix.TList(w).grid(column=0, row=1)

# Tix Mega Widgets
def Mk_tixMega0(nb, name):
    w = nb.page(name)
    tixBalloon              = tix.Balloon(w)
    tixButtonBox            = tix.ButtonBox(w).grid(column=1, row=0)
    tixCheckList            = tix.CheckList(w).grid(column=2, row=0)
    tixCObjView             = tix.CheckList(w).grid(column=3, row=0)
    tixComboBox             = tix.ComboBox(w).grid(column=0, row=1)
    tixControl              = tix.Control(w).grid(column=1, row=1)
    tixDirList              = tix.DirList(w).grid(column=2, row=1)
    # tixDirSelectBox, not in Tix8.1.4 Reference Manual
    tixDirSelectBox         = tix.DirSelectBox(w).grid(column=3, row=1)
def Mk_tixMega1(nb, name):
    w = nb.page(name)    
    tixDirSelectDialog      = tix.DirSelectDialog(w)
    tixDirTree              = tix.DirTree(w).grid(column=1, row=0)
    tixExFileSelectBox      = tix.ExFileSelectBox(w).grid(column=2, row=0)
    tixExFileSelectDialog   = tix.ExFileSelectDialog(w)
    tixFileEntry            = tix.FileEntry(w).grid(column=0, row=1)
    tixFileSelectBox        = tix.FileSelectBox(w).grid(column=1, row=1)
    tixFileSelectDialog     = tix.FileSelectDialog(w)
    tixLabelEntry           = tix.LabelEntry(w).grid(column=3, row=1)
def Mk_tixMega2(nb, name):
    w = nb.page(name)    
    tixLabelFrame           = tix.LabelFrame(w).grid(column=0, row=0)
    tixListNoteBook         = tix.ListNoteBook(w).grid(column=1, row=0)
    tixMeter                = tix.Meter(w).grid(column=2, row=0)
    tixNoteBook             = tix.NoteBook(w).grid(column=3, row=0)
    tixOptionMenu           = tix.OptionMenu(w).grid(column=0, row=1)
    tixPanedWindow          = tix.PanedWindow(w).grid(column=1, row=1)
    tixPopupMenu            = tix.PopupMenu(w)
    tixResizeHandle         = tix.ResizeHandle(w).grid(column=3, row=1)
def Mk_tixMega3(nb, name):
    w = nb.page(name)  
    tixScrolledGrid         = tix.ScrolledGrid(w).grid(column=0, row=0)
    tixScrolledHList        = tix.ScrolledHList(w).grid(column=1, row=0)
    tixScrolledListBox      = tix.ScrolledListBox(w).grid(column=2, row=0)
    tixScrolledText         = tix.ScrolledText(w).grid(column=3, row=0)
    tixScrolledTList        = tix.ScrolledTList(w).grid(column=0, row=1)
    tixScrolledWindow       = tix.ScrolledWindow(w).grid(column=1, row=1)   
    tixSelect               = tix.Select(w).grid(column=2, row=1)
    tixShell                = tix.Shell(w)#.grid(column=3, row=1)
def Mk_tixMega4(nb, name):
    w = nb.page(name)  
    tixDialogShell          = tix.DialogShell(w)#.grid(column=0, row=0)
    tixStdButtonBox         = tix.StdButtonBox(w).grid(column=1, row=0)
    tixTList                = tix.TList(w).grid(column=2, row=0)
    tixTree                 = tix.Tree(w).grid(column=3, row=0)

root = tix.Tk()

w = tix.NoteBook(root)
w.add('tkinterStd0', label='tkinterStd0',
      createcmd=lambda w=w, name='tkinterStd0': Mk_tkinterStd0(w, name))
w.add('tkinterStd1', label='tkinterStd1',
      createcmd=lambda w=w, name='tkinterStd1': Mk_tkinterStd1(w, name))
w.add('tkinterStd2', label='tkinterStd2',
      createcmd=lambda w=w, name='tkinterStd2': Mk_tkinterStd2(w, name))
w.add('tixStd', label='tixStd',
      createcmd=lambda w=w, name='tixStd': Mk_tixStd(w, name))
w.add('tixMega0', label='tixMega0',
      createcmd=lambda w=w, name='tixMega0': Mk_tixMega0(w, name))
w.add('tixMega1', label='tixMega1',
      createcmd=lambda w=w, name='tixMega1': Mk_tixMega1(w, name))
w.add('tixMega2', label='tixMega2',
      createcmd=lambda w=w, name='tixMega2': Mk_tixMega2(w, name))
w.add('tixMega3', label='tixMega3',
      createcmd=lambda w=w, name='tixMega3': Mk_tixMega3(w, name))
w.add('tixMega4', label='tixMega4',
      createcmd=lambda w=w, name='tixMega4': Mk_tixMega4(w, name))
w.pack()


root.mainloop()
