#coding: utf-8
__author__ = 'gold'
__date__ = '2019/1/5'
__time__ = '17:09'
__filename__ = 'common.py'

import random
import os
from pygame.locals import KEYDOWN,K_ESCAPE,K_SPACE
import pygame
from locals import colScale,height,width,colMostScale,numFontScale,numHeiScale,numWidScale,startX,endX,\
    startY,green,blue,black,fontsize,font,fontObj,white,base

def validNumList(numList):
    '''
    this func is used to check if a list only contains vaild num element
    :param numList:
    :return:bool
    '''

    if not numList:
        return False

    try:
        for i in range(len(numList)):
            if isinstance(numList[i],(float,int)):
                continue
            if numList[i].find('.'):
                numList[i] = float(numList[i])
            else:
                numList[i] = int(numList[i])
    except:
        return False

    return True

def getNumList(start = 0,end = 100,count = 100):

    '''
    this function is used to get a num list with random integer between 0 and 100
    :return: [int]
    '''
    if start >= end:
        raise ValueError('the start num must less than end num: start = %s,end = %s' % (start,end))
    if count < 1:
        raise ValueError('you must specify a negative integer:count = %s' % count)
    a = [random.randint(start,end) for i in range(count)]
    return a

def check_package(packName = 'pygame'):
    '''
    this function is used to check if the host has installed named package or not
    :param packName: str,the named package name
    :return: int,0 if the package has been installed or has been installed in this function;
                 -1 if the environment has no such a package or fail to install in this function.
    '''
    res = os.popen('pip show ' + packName)
    if not res.read():
        for i in range(3):
            res = os.popen('pip install ' + packName)
            if res.read().find(' Could not'):
                continue
            else:
                return 0
        return -1

    else:
        return 0

def getMax(numList):
    '''
    this func is used to get the max num in the given num list
    :param numList: []
    :return: num
    '''
    return max(numList)


def getMin(numList):
    '''
    this func is used to get the min num in the given num list
    :param numList: []
    :return: num
    '''
    return min(numList)

def eventHandle(events):
    '''
    this method is used to handle keyboard event
    if the user press esc,then the pro is finished;else return the key
    :param events: [],a serious of keyboard event
    :return: event.key
    '''
    for event in events:
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            exitGame()
        if event.type == KEYDOWN:
            return event.key

def getDistance(left,right,steps):
    return (right - left) // steps

def getScale(low,high):
    if low == high:
        scale = 1
    else:
        scale = 1 / (high - low)
    return scale

def drawNum(text,x,y,color,fontsize,font):
    fontObj = pygame.font.SysFont(font, fontsize)
    textSurfaceObj = fontObj.render(text, False, color)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (x, y)
    return textSurfaceObj,textRectObj


def draw(displaysurf,numList,numPosList,columnColorList,numColorList,colHeightList,colWidth,middlex,ydis,tipsSurfaceObj,tipsRectObj,font,fontsize,bg = white):
    '''
    draw infor on the main display
    :param displaysurf:
    :param numList: [],all the elements in the list to sort
    :param numPosList: [],all the columns' x position
    :param numColor: [],every column's corresponding color
    :param colHeightList: [],every column's height.
    :param colWidth: int,the column's width
    :param middlex: int,the num away from its column's x position,positive.
    :param ydis: the y away from the height of its column position.
    :param tipsSurfaceObj:the tips surface obj to draw on the display.
    :param tipsRectObj:the tips rect to draw on the display.
    :param font:str,the font used to draw the nums on top of every column.
    :param fontsize:int,the size of the num on the top of every column.
    :return:
    '''

    displaysurf.fill(white)
    for index in range(len(numList)):
        pygame.draw.rect(displaysurf,columnColorList[index],(numPosList[index],startY,colWidth,-colHeightList[index]))
        numSurfaceObj, numRectObj = drawNum(str(numList[index]), numPosList[index] + middlex, startY - colHeightList[index] - ydis, numColorList[index],
                                            fontsize, font)
        displaysurf.blit(numSurfaceObj,numRectObj)
    displaysurf.blit(tipsSurfaceObj,tipsRectObj)
    pygame.display.update()

def exitGame():
    pygame.quit()
    exit()

def start(displaysurf,numList,numPosList,columnColorList,numColorList,coloHeightList,colWidth,middle,ydis,tipsSurfaceObj,tipsRectObj,font,fontsize):
    while True:
        draw(displaysurf,numList,numPosList,columnColorList,numColorList,coloHeightList,colWidth,middle,ydis,tipsSurfaceObj,tipsRectObj,font,fontsize)
        key = eventHandle(pygame.event.get())
        if key == K_SPACE:
            return

end = start

class Prepare:
    def __init__(self):
        pygame.init()
        self.numArray = getNumList(count= 100)
        low = getMin(self.numArray)
        high = getMax(self.numArray)
        distance = getDistance(startX,endX,len(self.numArray))
        self.columnWidth = int(distance * colScale)
        self.columnPosList = []
        for i in range(len(self.numArray)):
            self.columnPosList.append(startX + distance * i)
        self.columnHeightList = []
        mostColumnHeight = int(startY * colMostScale)
        if low == high:
            for i in range(len(self.numArray)):
                self.colHeightList.append(mostColumnHeight)
        else:
            for num in self.numArray:
                self.columnHeightList.append(int(mostColumnHeight * (num - low) / (high - low)) + base)
        self.columnColor = [green] * len(self.numArray)  # get the origin color for all the columns
        self.numColor = [black] * len(self.numArray)
        pygame.display.set_caption('bubble')
        self.displaysurf = pygame.display.set_mode((width, height))
        self.displaysurf.fill(white)

prepare = Prepare()