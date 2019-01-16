#coding: utf-8
__author__ = 'gold'
__date__ = '2019/1/5'
__time__ = '19:56'
__filename__ = 'locals.py'

import tkinter
import pygame
pygame.init()

win = tkinter.Tk()
width = win.winfo_screenwidth() # the width of the screen
height = win.winfo_screenheight() # the height of the screen
del win

yellow = (255,255,0)
red = (255,0,0)
blue = (0,0,255)
white = (255,255,255)
green = (0,255,0)
black = (0,0,0)

startX = int(width * 0.1) # the start position of the first column
startY = int(height * 0.9) # the lowest position of all the columns
endX = int(width * 0.9) # the rightmost position
endY = int(height * 0.1)  # the highest position of the longest column
base = int(0.1 * startY)

colScale = 0.8 # the col width occpying the column
colMostScale = 0.8 # the most height occupying the column
numWidScale = 0.5
numHeiScale = 0.05
# numFontSize = int(numFontScale * min(height,width))
numLargestFontSize = int(numHeiScale * min(height,width))
numFont = 'freesansbold.ttf'
yDisScale = 0.02
columnMostHeight = int(startY * colMostScale)
yDis = int(yDisScale * columnMostHeight) #每个数字距离其柱子顶部的距离e


fontsize = int(height * 0.08)
font = 'freesansbold.ttf'
fontObj = pygame.font.SysFont(font,fontsize,bold = True)

tips = 'press space to run or escape to exit'
pauseTextSurfaceObj = fontObj.render(tips,False,black)
pauseTextRectObj = pauseTextSurfaceObj.get_rect()
pauseTextRectObj.center = (width // 2, height * 0.03)

tips = 'press space to pause or escape to exit'
runTextSurfaceObj = fontObj.render(tips,False,black)
runTextRectObj = runTextSurfaceObj.get_rect()
runTextRectObj.center = (width // 2, height * 0.03)

tips = 'press space to continue or escape to exit'
continueTextSurfaceObj = fontObj.render(tips,False,black)
continueTextRectObj = continueTextSurfaceObj.get_rect()
continueTextRectObj.center = (width // 2, height * 0.03)

tips = 'press space to exit'
exitTextSurfaceObj = fontObj.render(tips,False,black)
exitTextRectObj = exitTextSurfaceObj.get_rect()
exitTextRectObj.center = (width // 2, height * 0.03)

