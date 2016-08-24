
import os.path


filein = 'plot.tcl'


fileout = os.path.splitext(filein)[0] + '.py'

breplaces = {
r"""if {![info exists widgetDemo]} {
    error "This script should be run from the \"widget\" demo."
}
""":
r"""assert 'widgetDemo' in globals(), \
'This script should be run from the "widget" demo.'
""",

"""package require Tk
""":
"""from tkinter import *
"""
}

demo_name = ''

block = []

with open(filein) as fi, open(fileout, 'w') as fo:
    for line in fi:
        if line.strip() == '':
            if block:
                if all([ln.startswith('#') for ln in block]):
                    for ln in block:
                        fo.write(ln)
                else:
                    for ln in block:
                        fo.write('##' + ln)
                        
                    blockstr = ''.join(block)
                    if blockstr in breplaces:
                        fo.write(breplaces[blockstr])
                    else:
                        for ln in block:
                            if ln.startswith('set w .'):
                                
                block = []
            fo.write(line)
        else:
            block.append(line)
        
        


    
