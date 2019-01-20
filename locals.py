#coding: utf-8
__author__ = 'gold'
__date__ = '2019/1/5'
__time__ = '19:56'
__filename__ = 'locals.py'

import tkinter
import pygame
pygame.init()

# below is the part to get the size of the screen
win = tkinter.Tk()
width = win.winfo_screenwidth() # the width of the screen
height = win.winfo_screenheight() # the height of the screen

# below are some color variables
yellow = (255,255,0)
red = (255,0,0)
blue = (0,0,255)
white = (255,255,255)
green = (0,255,0)
black = (0,0,0)

# below are some axis's position parameters
startX = int(width * 0.1) # the start position of the first column
startY = int(height * 0.9) # the lowest position of all the columns
endX = int(width * 0.9) # the rightmost position panel including all the columns
endY = int(height * 0.1)  # the highest position of the longest column
base = int(0.1 * startY) # avoiding the smallest num's column may be 0 in height
colScale = 0.8 # the col width occpying the space between one column to its next column.
colMostScale = 0.8 # the most height occupying the column
numWidScale = 0.5 # the number's width scale occupying one column
numHeiScale = 0.05 # the number's height scale occupying the column's height
numLargestFontSize = int(numHeiScale * min(height,width)) # the size of num str
numFont = 'freesansbold.ttf' # nums' font
yDisScale = 0.02 # the space between num and its column in height occupying the height
columnMostHeight = int(startY * colMostScale)
yDis = int(yDisScale * columnMostHeight) # the space between num and its column's top

# below are the tip's position info
fontsize = int(height * 0.08)
font = 'freesansbold.ttf'
fontObj = pygame.font.SysFont(font,fontsize,bold = True)

# below is the tips when the sort is paused or have not started.
tips = 'press space to run or escape to exit'
pauseTextSurfaceObj = fontObj.render(tips,False,black)
pauseTextRectObj = pauseTextSurfaceObj.get_rect()
pauseTextRectObj.center = (width // 2, height * 0.03)

# below is the tips when sort is paused
tips = 'press space to pause or escape to exit'
runTextSurfaceObj = fontObj.render(tips,False,black)
runTextRectObj = runTextSurfaceObj.get_rect()
runTextRectObj.center = (width // 2, height * 0.03)

#below is the tips when sort has finished
tips = 'sort complete,press esc to exit'
exitTextSurfaceObj = fontObj.render(tips,False,black)
exitTextRectObj = exitTextSurfaceObj.get_rect()
exitTextRectObj.center = (width // 2, height * 0.03)

defaultArrayLen = 50 # the default count of the random array's lengthen