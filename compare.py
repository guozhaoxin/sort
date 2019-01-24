#coding: utf-8
__author__ = 'gold'
__date__ = '2019/1/23'
__time__ = '20:04'
__filename__ = 'compare.py'

'''
this code is used to compare different sort methods.
'''
from common import getNumList,getDistance,getScale,drawNum,exitGame
from locals import width,height,\
                    green,blue,red,black,white

import pygame
from pygame.locals import K_ESCAPE,K_SPACE,KEYDOWN
import threading
import time
import copy
import os

sortThreadCount = 0

fontsize = int(height * 0.03)
font = 'freesansbold.ttf'
fontObj = pygame.font.SysFont(font,fontsize,bold = True)
# below is the tips when the sort is paused or have not started.
tips = 'press space to run or escape to exit'
pauseTextSurfaceObj = fontObj.render(tips,False,black)
pauseTextRectObj = pauseTextSurfaceObj.get_rect()
pauseTextRectObj.center = (width // 2, height * 0.015)
# below is the tips when sort is paused
tips = 'press space to pause or escape to exit'
runTextSurfaceObj = fontObj.render(tips,False,black)
runTextRectObj = runTextSurfaceObj.get_rect()
runTextRectObj.center = (width // 2, height * 0.015)
#below is the tips when sort has finished
tips = 'sort complete,press esc to exit'
exitTextSurfaceObj = fontObj.render(tips,False,black)
exitTextRectObj = exitTextSurfaceObj.get_rect()
exitTextRectObj.center = (width // 2, height * 0.015)

statusShow = [(pauseTextSurfaceObj,pauseTextRectObj),(runTextSurfaceObj,runTextRectObj),(exitTextSurfaceObj,exitTextRectObj)]
status = 0
title = statusShow[0]
pausetime = 0.001

def larger(x,y):
    if x < y:
        return -1
    elif x == y:
        return 0
    return 1

def smaller(x,y):
    if x > y:
        return -1
    elif x == y:
        return 0
    return 1


def exitGame():
    '''
    exit the program
    :return:
    '''
    pygame.quit()
    exit()

def getStrRect_Surface(s,x,y):
    '''
    get the str surface object and rect object,set the rect's center
    :param s:str,the str to show
    :param x:int,the str's center x axis
    :param y:int,the str's center y axis
    :return:surface,rect
    '''
    strTextSurfaceObj = fontObj.render(s,False,black)
    strTextRectObj = strTextSurfaceObj.get_rect()
    strTextRectObj.center = (x,y)
    return strTextSurfaceObj,strTextRectObj

class ArraySet:
    def __init__(self,array,name,xbeginScale,xendScale,ybeginScale,yendScale,colScale,columnHeightList):
        self.numList = copy.deepcopy(array)
        self.name = name
        startX = int(width * xbeginScale)
        endX = int(width * (xendScale - 0.05))
        self.distance = getDistance(startX, endX, len(self.numList))
        self.columnWidth = int(self.distance * colScale)
        self.columnPosList = []
        for i in range(len(self.numList)):
            self.columnPosList.append(startX + self.distance * i)
        self.columnHeightList = copy.deepcopy(columnHeightList)
        self.yPos = int(yendScale * height)
        self.columnColorList = []
        for i in range(len(self.numList)):
            self.columnColorList.append(green)
        self.titleCenX,self.titleCenY = int(width * ((xendScale - 0.05 - xbeginScale) / 2 + xbeginScale)),int(height * ((ybeginScale - 0.025)))
        self.nameSurface,self.nameRect = getStrRect_Surface(self.name,self.titleCenX,self.titleCenY)

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

    def setOrderly(self,duration):
        s = self.name + ', %.2fs' % duration
        self.nameSurface,self.nameRect = getStrRect_Surface(s,self.titleCenX,self.titleCenY)

    def swapNum(self,left,right):
        self.numList[left],self.numList[right] = \
        self.numList[right],self.numList[left]
        self.columnHeightList[left],self.columnHeightList[right] = \
        self.columnHeightList[right],self.columnHeightList[left]


class DrawPanelThread(threading.Thread):
    def __init__(self,arraySetList,displaysurf):
        super(DrawPanelThread,self).__init__()
        self.displaysurf = displaysurf
        self.arraySetList = arraySetList

    def run(self):
        clock = pygame.time.Clock()
        global sortThreadCount,status,title
        while True:
            self.displaysurf.fill(white)
            for arraySet in self.arraySetList:
                for index in range(len(arraySet.numList)):
                    pygame.draw.rect(self.displaysurf, arraySet.columnColorList[index],
                                     (arraySet.columnPosList[index], arraySet.yPos, arraySet.columnWidth,
                                      -arraySet.columnHeightList[index])
                                     )
                self.displaysurf.blit(arraySet.nameSurface,arraySet.nameRect)
            self.displaysurf.blit(title[0],title[1])
            pygame.display.update()
            clock.tick(60)

def eventhandl(events):
    '''
    the function is used to handle all mouse and keyboard events.
    :param events: list,all captured events.
    :param arrayset: ArraySet instance, as all changes will take effect in this variable.
    :param tipsarry: list,the tips list
    :return:
    '''
    global status,statusShow,title,sortThreadCount
    for event in events:
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                status = (status + 1) % 2
                if sortThreadCount != 0:
                    title = statusShow[status]
            elif event.key == K_ESCAPE:
                status = -1
        if sortThreadCount == 0:
            title = statusShow[-1]


class SortThread(threading.Thread):
    def __init__(self,arraySet:ArraySet,lock,method):
        super(SortThread,self).__init__()
        self.arrayset = arraySet
        self.lock = lock
        global sortThreadCount
        self.lock.acquire()
        sortThreadCount += 1
        self.lock.release()
        self.method = method
    def run(self):
        pass

    def checkpause(self,pause = 0.01):
        '''
        thif function is used to juede if the pro has been paused.
        :return:
        '''
        global status
        while status == 0:
            time.sleep(pause)

    def swapNum(self,left,right):
        self.arrayset.numList[left],self.arrayset.numList[right] = \
        self.arrayset.numList[right],self.arrayset.numList[left]
        self.arrayset.columnHeightList[left],self.arrayset.columnHeightList[right] = \
        self.arrayset.columnHeightList[right],self.arrayset.columnHeightList[left]


class BubbleSortThread(SortThread):
    '''
    the bubble thread
    '''

    def run(self):
        # here is used to juede if the user has decided to sort.
        global pausetime,sortThreadCount
        self.checkpause(pausetime)
        lastIndex = len(self.arrayset.numList) - 1
        start = time.time()
        while lastIndex > -1:
            for index in range(0,lastIndex):
                self.checkpause()
                self.arrayset.curColumnColor(index)
                if self.method(self.arrayset.numList[index],self.arrayset.numList[index + 1]) > 0:
                    self.arrayset.swapNum(index,index + 1)
                    self.arrayset.curColumnColor(index + 1)
                time.sleep(pausetime)
                self.checkpause()
                self.arrayset.resetColumnColor(index)
                self.arrayset.resetColumnColor(index +1)
                time.sleep(pausetime)
            self.checkpause()
            self.arrayset.fixColumnColor(lastIndex)
            lastIndex -= 1
        self.checkpause()
        self.arrayset.fixColumnColor(0)
        self.arrayset.setOrderly(time.time() - start)
        self.lock.acquire()
        sortThreadCount -= 1
        self.lock.release()
        return

class InsertSortThread(SortThread):
    def run(self):
        global pausetime,sortThreadCount
        self.checkpause(pausetime)
        start = time.time()
        for index in range(len(self.arrayset.numList)):
            self.checkpause()
            self.arrayset.curColumnColor(index)
            curindex = index - 1
            tempIndex = index
            while curindex >= 0:
                self.arrayset.curColumnColor(curindex)
                self.arrayset.curColumnColor(tempIndex)
                self.checkpause()
                time.sleep(pausetime)
                if self.method(self.arrayset.numList[tempIndex],self.arrayset.numList[curindex]) < 0:
                # if self.arrayset.numList[tempIndex] < self.arrayset.numList[curindex]:
                    self.arrayset.swapNum(tempIndex,curindex)
                else:
                    self.arrayset.resetColumnColor(tempIndex)
                    self.arrayset.resetColumnColor(curindex)
                    self.checkpause(pausetime)
                    time.sleep(pausetime)
                    break
                self.arrayset.curColumnColor(index)
                self.checkpause(pausetime)
                time.sleep(pausetime)
                self.arrayset.resetColumnColor(tempIndex)
                self.checkpause(pausetime)
                time.sleep(pausetime)
                curindex -= 1
                tempIndex -= 1
            self.arrayset.resetColumnColor(tempIndex)
            self.checkpause()
            time.sleep(pausetime)

        for index in range(len(self.arrayset.columnColorList)):
            self.arrayset.fixColumnColor(index)
        self.arrayset.setOrderly(time.time() - start)
        self.lock.acquire()
        sortThreadCount -= 1
        self.lock.release()

class SelectionSortThread(SortThread):
    def run(self):
        global pausetime,sortThreadCount
        self.checkpause(pausetime)
        start = time.time()
        for index in range(len(self.arrayset.numList)):
            self.arrayset.curColumnColor(index)
            self.checkpause(pausetime)
            time.sleep(pausetime)
            smallIndex = index
            smallNum = self.arrayset.numList[index]
            for curIndex in range(index + 1,len(self.arrayset.numList)):
                self.arrayset.curColumnColor(curIndex)
                self.checkpause(pausetime)
                time.sleep(pausetime)
                if self.method(smallNum,self.arrayset.numList[curIndex]) > 0:
                # if smallNum > self.arrayset.numList[curIndex]:
                    if smallIndex != index:
                        self.arrayset.resetColumnColor(smallIndex)
                    smallNum = self.arrayset.numList[curIndex]
                    smallIndex = curIndex
                    self.arrayset.curColumnColor(curIndex)
                    self.checkpause(pausetime)
                    time.sleep(pausetime)
                if curIndex == smallIndex:
                    self.arrayset.curColumnColor(curIndex)
                else:
                    self.arrayset.resetColumnColor(curIndex)
                self.checkpause(pausetime)
                time.sleep(pausetime)
            if smallIndex != index:
                self.arrayset.swapNum(smallIndex,index)
                self.arrayset.resetColumnColor(smallIndex)
                self.checkpause(pausetime)
                time.sleep(pausetime)
            self.checkpause(pausetime)
            time.sleep(pausetime)
            self.arrayset.fixColumnColor(index)
            self.checkpause(pausetime)
            time.sleep(pausetime)
        self.arrayset.setOrderly(time.time() - start)
        self.lock.acquire()
        sortThreadCount -= 1
        self.lock.release()

class ShellSortThread(SortThread):
    def run(self):
        global pausetime,sortThreadCount
        self.checkpause(pausetime)
        steps = [8,5,3,2,1] # the shell steps list
        start = time.time()
        for step in steps:
            for index in range(len(self.arrayset.numList)):
                curIndex = index - step
                latterIndex = index
                self.arrayset.curColumnColor(index)
                self.checkpause(pausetime)
                time.sleep(pausetime)
                while curIndex >= 0:
                    self.arrayset.curColumnColor(curIndex)
                    self.arrayset.curColumnColor(latterIndex)
                    self.checkpause(pausetime)
                    time.sleep(pausetime)
                    if self.method(self.arrayset.numList[curIndex],self.arrayset.numList[latterIndex]) < 0:
                    # if self.arrayset.numList[curIndex] <= self.arrayset.numList[latterIndex]:
                        self.arrayset.resetColumnColor(latterIndex)
                        self.arrayset.resetColumnColor(curIndex)
                        self.checkpause(pausetime)
                        time.sleep(pausetime)
                        break
                    self.arrayset.swapNum(curIndex,latterIndex)
                    self.checkpause(pausetime)
                    time.sleep(pausetime)
                    if latterIndex != index:
                        self.arrayset.resetColumnColor(latterIndex)
                    self.checkpause(pausetime)
                    time.sleep(pausetime)
                    latterIndex = curIndex
                    curIndex -= step
                self.arrayset.resetColumnColor(index)
                self.arrayset.resetColumnColor(latterIndex)
                self.checkpause(pausetime)
                time.sleep(pausetime)
                if curIndex >= 0:
                    self.arrayset.resetColumnColor(curIndex)
                    self.checkpause(pausetime)
                    time.sleep(pausetime)
        for index in range(len(self.arrayset.numList)):
            self.arrayset.fixColumnColor(index)
        self.arrayset.setOrderly(time.time() - start)
        self.lock.acquire()
        sortThreadCount -= 1
        self.lock.release()

class HeapSortThread(SortThread):

    def run(self):
        global pausetime,sortThreadCount
        self.checkpause(pausetime)
        start = time.time()
        self.buildHeap()
        last = len(self.arrayset.numList) - 1
        for index in range(last,-1,-1):
            self.arrayset.swapNum(0,index)
            self.arrayset.fixColumnColor(index)
            self.checkpause(pausetime)
            time.sleep(pausetime)
            self.dfs(0,index)
        self.arrayset.fixColumnColor(0)
        self.arrayset.setOrderly(time.time() - start)
        self.lock.acquire()
        sortThreadCount -= 1
        self.lock.release()


    def dfs(self,index,last):
        global pausetime
        leftInd = index * 2 + 1
        rightInd = leftInd + 1
        maxInd = index
        maxNum = self.arrayset.numList[index]
        self.arrayset.curColumnColor(index)
        self.checkpause(pausetime)
        time.sleep(pausetime)
        if leftInd < last:
            self.arrayset.curColumnColor(leftInd)
            if self.method(maxNum,self.arrayset.numList[leftInd]) < 0:
            # if maxNum < self.arrayset.numList[leftInd]:
                maxInd = leftInd
                maxNum = self.arrayset.numList[leftInd]
            self.checkpause(pausetime)
            time.sleep(pausetime)
            if maxInd != leftInd:
                self.arrayset.resetColumnColor(leftInd)
                self.checkpause(pausetime)
                time.sleep(pausetime)
        if rightInd < last:
            self.arrayset.curColumnColor(rightInd)
            if self.method(maxNum,self.arrayset.numList[rightInd]) < 0:
            # if maxNum < self.arrayset.numList[rightInd]:
                self.arrayset.resetColumnColor(leftInd)
                maxInd = rightInd
            self.checkpause(pausetime)
            time.sleep(pausetime)
            if rightInd != maxInd:
                self.arrayset.resetColumnColor(rightInd)
                self.checkpause(pausetime)
                time.sleep(pausetime)
        if index != maxInd:
            self.arrayset.swapNum(index,maxInd)
            self.arrayset.resetColumnColor(index)
            if leftInd < last:
                self.arrayset.resetColumnColor(leftInd)
            if rightInd < last:
                self.arrayset.resetColumnColor(rightInd)
            self.dfs(maxInd,last)
        self.arrayset.resetColumnColor(index)

    def buildHeap(self):
        global pausetime
        middle = len(self.arrayset.numList) // 2
        self.checkpause(pausetime)
        for index in range(middle,-1,-1):
            self.dfs(index,len(self.arrayset.numList))

class QuickSortThread(SortThread):
    def run(self):
        global pausetime,sortThreadCount
        self.checkpause(pausetime)
        start = time.time()
        self.quick(0,len(self.arrayset.numList) - 1)
        self.arrayset.setOrderly(time.time() - start)
        self.lock.acquire()
        sortThreadCount -= 1
        self.lock.release()

    def quick(self,left,right):
        global pausetime
        partion = self.partion(left,right)
        self.arrayset.fixColumnColor(partion)
        self.checkpause(pausetime)
        time.sleep(pausetime)
        if partion > left:
            self.quick(left,partion - 1)
        self.checkpause(pausetime)
        if partion < right:
            self.quick(partion + 1,right)
        self.checkpause(pausetime)

    def partion(self,left,right):
        global pausetime
        base = self.arrayset.numList[left]
        self.arrayset.curColumnColor(left)
        self.checkpause(pausetime)
        time.sleep(pausetime)
        while left < right:
            self.checkpause(pausetime)
            while left < right:
                self.arrayset.curColumnColor(right)
                self.checkpause(pausetime)
                time.sleep(pausetime)
                if self.method(self.arrayset.numList[right],base) >= 0:
                # if self.arrayset.numList[right] >= base:
                    self.arrayset.resetColumnColor(right)
                    self.checkpause(pausetime)
                    time.sleep(pausetime)
                    right -= 1
                else:
                    break
            self.arrayset.swapNum(left,right)
            if left != right:
                self.arrayset.resetColumnColor(left)
                self.checkpause(pausetime)
                time.sleep(pausetime)
            while left < right:
                self.checkpause(pausetime)
                self.arrayset.curColumnColor(left)
                self.checkpause(pausetime)
                time.sleep(pausetime)
                if self.method(self.arrayset.numList[left],base) <= 0:
                # if self.arrayset.numList[left] <= base:
                    self.arrayset.resetColumnColor(left)
                    self.checkpause(pausetime)
                    time.sleep(pausetime)
                    left += 1
                else:
                    break
            self.arrayset.swapNum(left,right)
            if left != right:
                self.arrayset.resetColumnColor(right)
                self.checkpause(pausetime)
                time.sleep(pausetime)

        return left

def getColumnHeight(array):
    heightList = []
    minValue = min(array)
    maxValue = max(array)
    columnMostHeight = int(0.35 * height)
    if minValue == maxValue:
        for i in range(len(array)):
            heightList.append(columnMostHeight)
    else:
        base = int(height * (0.05))
        for i in range(len(array)):
            heightList.append(base + columnMostHeight * (array[i] - minValue) / (maxValue - minValue))
    return heightList



if __name__ == '__main__':
    threadList = []
    arraySetList = []
    method = larger
    pygame.init()
    os.environ['SDL_VIDEO_WINDOW_POS'] = '%d,%d' % (10,30) # set the main panel's position on the screen.
    displaysurf = pygame.display.set_mode((width,height))
    displaysurf.fill(white)
    array = getNumList(count = 300)
    heightList = getColumnHeight(array)

    bubbleArraySet = ArraySet(array,'bubble',0.05,0.35,0.08,0.48,0.8,heightList)
    arraySetList.append(bubbleArraySet)
    bubbleThread = BubbleSortThread(bubbleArraySet,threading.Lock(),method)
    threadList.append(bubbleThread)

    insertArraySet = ArraySet(array, 'insert', 0.35, 0.65, 0.08, 0.48, 0.8, heightList)
    arraySetList.append(insertArraySet)
    insertThread = InsertSortThread(insertArraySet, threading.Lock(), method)
    threadList.append(insertThread)

    selectionArraySet = ArraySet(array, 'selection', 0.65, 0.95, 0.08, 0.48, 0.8, heightList)
    arraySetList.append(selectionArraySet)
    selectionThread = SelectionSortThread(selectionArraySet, threading.Lock(), method)
    threadList.append(selectionThread)

    shellArraySet = ArraySet(array, 'shell', 0.05, 0.35, 0.53, 0.93, 0.8, heightList)
    arraySetList.append(shellArraySet)
    shellThread = ShellSortThread(shellArraySet, threading.Lock(), method)
    threadList.append(shellThread)

    heapArraySet = ArraySet(array, 'heap', 0.35, 0.65, 0.53, 0.93, 0.8, heightList)
    arraySetList.append(heapArraySet)
    heapThread = HeapSortThread(heapArraySet, threading.Lock(), method)
    threadList.append(heapThread)

    quickArraySet = ArraySet(array, 'quick', 0.65, 0.95, 0.53, 0.93, 0.8, heightList)
    arraySetList.append(quickArraySet)
    quickThread = QuickSortThread(quickArraySet, threading.Lock(), method)
    threadList.append(quickThread)

    for thread in threadList:
        thread.setDaemon(True)
        thread.start()
    drawThread = DrawPanelThread(arraySetList,displaysurf=displaysurf)
    drawThread.setDaemon(True)
    drawThread.start()
    while True:
        eventhandl(pygame.event.get())
        if status == -1:
            exitGame()