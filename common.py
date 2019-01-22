#coding: utf-8
__author__ = 'gold'
__date__ = '2019/1/5'
__time__ = '17:09'
__filename__ = 'common.py'

import threading
import random
import os
import time
from pygame.locals import KEYDOWN,K_ESCAPE,K_SPACE
import pygame
from locals import colScale,height,width,yDis,startX,endX,startY,base,columnMostHeight,\
    font,numLargestFontSize,\
    exitTextRectObj,exitTextSurfaceObj,\
    pauseTextRectObj,pauseTextSurfaceObj,\
    runTextRectObj,runTextSurfaceObj,\
    defaultArrayLen,\
    green,black,white,blue,red

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


def getDistance(left,right,steps):
    '''
    this function is used to get the distance between 2 contiguous columns
    :param left:int,the left position
    :param right:int,the right position
    :param steps:int,the count of the columns
    :return:int,the width of the 2 contiguous columns
    '''
    return (right - left) // steps

def getScale(low,high):
    '''
    calculate the column's scale in the height
    :param low: number,the smallest element
    :param high: number,the largest element
    :return: float,the colum's scale in the height
    '''
    if low == high: # when the smallest and largest num are same,all the columns have the same height.
        scale = 1
    else:
        scale = 1 / (high - low)
    return scale

def drawNum(text,x,y,color,fontsize,font):
    '''
    this function is used to draw the num rect object
    :param text: str,the characters to draw
    :param x: int, the rect object's x position
    :param y: int, the rect object's y position
    :param color: (int,int,int),the rect object's color
    :param fontsize: int,the characters' size
    :param font: font,the characters' font
    :return: the rect's surface and itself.
    '''
    fontObj = pygame.font.SysFont(font, fontsize)
    textSurfaceObj = fontObj.render(text, False, color)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (x, y)
    return textSurfaceObj,textRectObj


def exitGame():
    '''
    exit the program
    :return:
    '''
    pygame.quit()
    exit()


class ArraySet:
    '''
    this class is used to store all the relvant information about the array.
    the attributes are listed：
        numList:[number,],the array to sort;
        columnWidth:int,every column's width(not include the space between 2 columns);
        columnPosList:[int],all the columns' x position;
        columnHeightList:[int],all the columns' height;
        numColorList:[(int,int,int)],all the numbers' color;
        columnColorList:[(int,int,int)],all the columns' height;
        numRectList:[(,)],all the numbers' rect surface,the surface is the 1th element;
        orderly:bool,if the sort has finished,True if finshed else False;
        runstate:int,the program is running or paused or exit,0:paused or not started,1:running,-1:exit.
        distance:int,the column between 2 columns(please differ the columnWidth).
    '''

    def __init__(self,numarray = None):
        '''
        :param numarray: [number],the array to sort,if None or empty,the class will generate a random array.z
        '''
        if numarray is None or len(numarray) == 0:
            self.numList = getNumList(count=defaultArrayLen) #默认造出一个100个[0,100]之间的整数出来
        else:
            self.numList = numarray

        low = min(self.numList)
        high = max(self.numList)
        self.distance = getDistance(startX, endX, len(self.numList))
        self.columnWidth = int(self.distance * colScale)
        self.columnPosList = []
        for i in range(len(self.numList)):
            self.columnPosList.append(startX + self.distance * i)
        self.columnHeightList = []
        if low == high:
            for i in range(len(self.numList)):
                self.columnHeightList.append(columnMostHeight)
        else:
            for num in self.numList:
                self.columnHeightList.append(int(columnMostHeight * (num - low) / (high - low)) + base)
        self.columnColorList = [green] * len(self.numList)  # get the origin color for all the columns
        self.numColorList = [black] * len(self.numList)
        self.numRectList = []
        numfontsize = min(numLargestFontSize, int(self.columnWidth * 1.5))
        for index in range(len(self.numList)):
            numSurfaceObj, numRectObj = drawNum(str(self.numList[index]),
                    self.columnPosList[index] + self.columnWidth // 2,
                    startY - self.columnHeightList[index] - yDis,
                    self.numColorList[index],
                    numfontsize, font
                    )
            self.numRectList.append((numSurfaceObj,numRectObj))
        self.orderly = False
        self.runstate = 0

    def getState(self):
        '''
        the the pro's running state
        :return: int
        '''
        return self.runstate

    def setState(self,state):
        '''
        set the pro's running state
        :param state: int,0,-1,1
        :return:
        '''
        self.runstate = state

    def setOrderly(self):
        '''
        update the orderly attri to indicate the pro has finished sorting work.
        :return:
        '''
        self.orderly = True

    def isOrderly(self):
        '''
        judge if the pro has finished sorting or not
        :return: bool
        '''
        return self.orderly

    def swapNumRect(self,leftind,rightind):
        '''
        when 2 numbers in an array swaped,their relevant columns have to be swaped,
        the function is used to finish the work;
        we need to swap the 2 nums' rect object and set their new centers.
        :param leftind: int,index,the index of the first element to swap
        :param rightind: int,index,the index of the second element to swap
        :return:
        '''
        pos1 = (self.numRectList[rightind][1].center[0],self.numRectList[leftind][1].center[1])
        pos2 = (self.numRectList[leftind][1].center[0],self.numRectList[rightind][1].center[1])
        self.numRectList[leftind][1].center = pos1
        self.numRectList[rightind][1].center = pos2
        self.numRectList[leftind],self.numRectList[rightind] = self.numRectList[rightind],self.numRectList[leftind]

    def fixColumnColor(self,index):
        try:
            self.columnColorList[index] = blue
        except IndexError as e:
            pass

    def curColumnColor(self,index):
        try:
            self.columnColorList[index] = red
        except IndexError as e:
            pass

    def resetColumnColor(self,index):
        try:
            self.columnColorList[index] = green
        except IndexError as e:
            pass

    def setColumnHeight(self,index,columnHeight):
        self.columnHeightList[index] = columnHeight

    def getColumnHeight(self,index):
        return self.columnHeightList[index]

    def setRectCenter(self,index,x,y):
        try:
            self.numRectList[index].center = (x,y)
        except IndexError as e:
            pass

    def getRectCenter(self,index):
        try:
            return self.numRectList[index].center
        except IndexError as e:
            return (-1,-1)

    def getDistance(self):
        return self.distance


class DrawPanelThread(threading.Thread):
    '''
    the draw panel thread,but it doesn't listen to the panel's events.
    it has some attributes:
        arraySet:ArraySet instance;
        tipsarray:[()],the tips needed to draw on the main panel.
        displaysurf:the pygame.display instance to draw all informations.
        lock:threading.Lock instance,to lock 1 or more elements when needed.
    '''
    def __init__(self,arraySet:ArraySet,tipsarray,displaysurf,lock:threading.Lock):
        super(DrawPanelThread,self).__init__()
        self.arraySet = arraySet
        self.tipsarray = tipsarray
        self.displaysurf = displaysurf
        self.lock = lock

    def run(self):
        clock = pygame.time.Clock()
        while self.arraySet.getState() != -1:
            self.displaysurf.fill(white)
            self.lock.acquire() # here we have to acquire the lock firsly,as the sort thread is running to fast.

            # below is used to draw all the columns.
            for index in range(len(self.arraySet.numList)):
                pygame.draw.rect(self.displaysurf,self.arraySet.columnColorList[index],
                                 (self.arraySet.columnPosList[index],startY,self.arraySet.columnWidth,-self.arraySet.columnHeightList[index])
                                 )

            # below is used to drawl all the numbers objects.
            for numSurfaceObj,numRectObj in self.arraySet.numRectList:
                self.displaysurf.blit(numSurfaceObj,numRectObj)
            self.lock.release()

            # below is used to draw all the tips
            for tips in self.tipsarray:
                self.displaysurf.blit(tips[0],tips[1])

            pygame.display.update()
            clock.tick(60)


class SortThread(threading.Thread):
    '''
    the sort thread,you must sub this class.
    the attributes are listed:
        arrayset:ArraySet instance;
        lock:threading.Lock,
    '''
    def __init__(self,arraySet,lock):
        super(SortThread,self).__init__()
        self.arrayset = arraySet
        self.lock = lock

    def run(self):
        pass

    def checkpause(self,pause = 0.01):
        '''
        thif function is used to juede if the pro has been paused.
        :return:
        '''
        while self.arrayset.getState() == 0:
            time.sleep(pause)


# below is a list with all the possible tips on the mpanel
# the 1th is pause tip, the 2th is run tip,the 3th is exit tip.
# the list is mainly used in the eventhandl function.
statusShow = [(pauseTextSurfaceObj,pauseTextRectObj),(runTextSurfaceObj,runTextRectObj),(exitTextSurfaceObj,exitTextRectObj)]
def eventhandl(events,arrayset,tipsarry):
    '''
    the function is used to handle all mouse and keyboard events.
    :param events: list,all captured events.
    :param arrayset: ArraySet instance, as all changes will take effect in this variable.
    :param tipsarry: list,the tips list
    :return:
    '''
    for event in events:
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                arrayset.setState((arrayset.getState() + 1) % 2)
                tipsarry[0] = statusShow[arrayset.getState()]
            elif event.key == K_ESCAPE:
                arrayset.setState(-1)

def showSort(numarray,SortThread,name):
    '''
    the only api used by all the sort functions,you only needed to pass one valid number and the
    sort thread,and the function will finished all work to sort.
    :param numarray:[number],the array you want to sort.
    :param SortThread: SortThread sub class.
    :return:
    '''
    pygame.init()
    os.environ['SDL_VIDEO_WINDOW_POS'] = '%d,%d' % (10,30) # set the main panel's position on the screen.
    pygame.display.set_caption(name)
    displaysurf = pygame.display.set_mode((width, height)) # the main displaysurf
    displaysurf.fill(white)
    arraySet = ArraySet(numarray) # get the ArraySet instance
    tipsArray = [statusShow[0],] #the tips array
    lock = threading.Lock()
    drawThread = DrawPanelThread(arraySet, tipsArray, displaysurf, lock)
    sortedThread = SortThread(arraySet,lock)
    drawThread.setDaemon(True) # set the draw thread daemon thread
    sortedThread.setDaemon(True) # set the sort thread daemon thread
    drawThread.start()
    sortedThread.start()
    while True:
        events = pygame.event.get()
        eventhandl(events,arraySet,tipsArray)
        if arraySet.getState() == -1: # the user pressed exit on the main panel.
            exitGame()
        if arraySet.isOrderly(): # the array is ordered.
            tipsArray[0] = statusShow[2]

def checkOrder(numList):
    '''
    this function is used to check if an array is ordered
    :param numList: [],the array to judge
    :return: bool,True if order else False.
    '''
    if len(numList) <= 1:
        return True
    for index in range(len(numList) - 1):
        if numList[index] > numList[index + 1]:
            return False
    return True