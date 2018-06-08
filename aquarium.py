#!venv/bin/python

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
    import termcolor
    import random
    import sys
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
        self.top_border = []
        self.bottom_border = []
        self.middle_border =[]
        self.border_all= []
        #-----------
        #Border Creation
        for i in range(screen_width):
            self.top_border.append('\u00af')
            self.bottom_border.append('_')
        #print(''.join(top_border))
        self.middle_border.append('|')
        for i in range(screen_width-2):
            self.middle_border.append(' ')
        self.middle_border.append('|')

        #print(''.join(bottom_border))
        self.border_all.append(self.top_border)
        for i in range(screen_height-3):
            self.border_all.append(self.middle_border)
        self.border_all.append(self.bottom_border)
#----------
#Rocks
#----------
'''Blue is smooth clay()
Pink is Jagged Plagioclase(P)
Yellow is Smoothish Limestone(Y)
Grey is Smoothish  Large Dolomite(D)
Black S is PLanar Shale'''

rocklist = {'clay':'blue','plagioclase':'pink', 'limestone': 'yellow','Shale':'black'}

#----------

class Rock:
    def __init__(self,size,morphology = '*'): 
   
        #Rock Initialization
        self.height = random.randint(1,size)
        self.width = random.randint(1,size)
        self.position_x = random.randint(1,screen_width)

        self.position_y = random.randint(int(screen_height-screen_height/3),screen_height)
        #self.stone = []
        #self.size = size
        self.morphology = morphology
        #background = ['on_']+self.morphology
        '''for i in range(self.height):
            for i in range(self.width):
                self.stone.append(rocklist[morphology])
                cprint(''.join(stone),rocklist[morphology],background)
        '''
    def draw(self, canvas):
        '''canvas is array of strings to be drawn
        '''
        current_x = self.position_x
        current_y = self.position_y
        for h in range(self.height):
            for w in range(self.width):
                canvas[current_y][current_x] = self.morphology
                current_x +=1
            current_y -=1
         






#----------
#Main stuff
#----------


#clay = 'clay'

def main():
    border = Border()
    rock1 = Rock(5)
    rock1.draw(border.border_all)
    for item in border.border_all:
        print(''.join(item))
    

if __name__ == '__main__':
    sys.exit(main())
















