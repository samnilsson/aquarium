#-----------
#Sam's Aquarium - May contain bears
#Use Python 3 probbo
#Done: Border Creation - using a list of list, borders are created on the screen
#
#
#
#
#
#
#-----------
"""
Git Commands to push/pull
git push origin master
git log
git status
git commit -m  'String here'
git add
git add -a
git pull
"""
#-----------
#imports
#-----------
try:
    #import tkinter
    import curses
    import os
    import shutil
except ImportError as e:
    print(e)
    exit()
#import numpy
#import scipy
#-----------
size = shutil.get_terminal_size()
screen_height = size.lines
screen_width = size.columns

#-----------
class Border:
   def __init__(self): 
    
        #Border initialization
        top_border = []
        bottom_border = []
        middle_border =[]
        border_all= []
        #-----------
        #Border Creation
        for i in range(screen_width):
            top_border.append('\u00af')
            bottom_border.append('_')
        #print(''.join(top_border))
        middle_border.append('|')
        for i in range(screen_width-2):
            middle_border.append(' ')
        middle_border.append('|')

        #print(''.join(bottom_border))
        border_all.append(top_border)
        for i in range(screen_height-3):
            border_all.append(middle_border)
        border_all.append(bottom_border)
#----------
#Rocks
#----------
#class rock:























