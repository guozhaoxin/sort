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
base = int(0.1 * height)


tips = 'press space to start or pause'
fontsize = int(height * 0.08)
font = 'freesansbold.ttf'
fontObj = pygame.font.SysFont(font,fontsize,bold = True)
textSurfaceObj = fontObj.render(tips,False,black)
textRectObj = textSurfaceObj.get_rect()
textRectObj.center = (width // 2, height * 0.03)
