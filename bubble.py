#coding: utf-8
__author__ = 'gold'
__date__ = '2019/1/5'
__time__ = '17:07'
__filename__ = 'bubble.py'

import pygame
from pygame.locals import K_SPACE,K_ESCAPE
from common import eventHandle,draw,exitGame,start,end,SortThread,EventMonitorThread,DrawPanelThread,ArraySet
from locals import red,blue,white,width,height,\
    yDis,numLargestFontSize,numFont,\
    exitTextRectObj,exitTextSurfaceObj,\
    pauseTextRectObj,pauseTextSurfaceObj

import time


# def sort(displaysurf,numList,numPosList,columnColorList,numColorList,coloHeightList,colWidth,middle,ydis,tipsSurfaceObj,tipsRectObj,font,fontsize,bg = white,contSur = contTextSurfaceObj,contRect = contTextRectObj):
#     lastIndex = len(numList) - 1
#     clock = pygame.time.Clock()
#     while lastIndex >= -1:
#         for index in range(lastIndex):
#             colorTemp1 = columnColorList[index]
#             colorTemp2 = columnColorList[index + 1]
#             columnColorList[index] = red
#             if numList[index] > numList[index + 1]:
#                 numList[index],numList[index + 1] = numList[index + 1],numList[index]
#                 coloHeightList[index],coloHeightList[index + 1] = coloHeightList[index + 1],coloHeightList[index]
#                 columnColorList[index + 1] = red
#
#             draw(displaysurf,numList,numPosList,columnColorList,numColorList,coloHeightList,colWidth,middle,ydis,tipsSurfaceObj,tipsRectObj,font,fontsize,bg)
#             columnColorList[index] = colorTemp1
#             columnColorList[index + 1] = colorTemp2
#             key = eventHandle(pygame.event.get())
#             if key == K_SPACE:
#                 while True:
#                     draw(displaysurf, numList, numPosList, columnColorList, numColorList, coloHeightList, colWidth,
#                          middle, ydis, contSur, contRect, font, fontsize)
#                     key = eventHandle(pygame.event.get())
#                     if key == K_SPACE:
#                         break
#                     elif key == K_ESCAPE:
#                         exitGame()
#             pygame.display.update()
#             clock.tick(60)
#         columnColorList[lastIndex] = blue
#         lastIndex -= 1
#     columnColorList[0] = blue
#     draw(displaysurf, numList, numPosList, columnColorList, numColorList, coloHeightList, colWidth, middle, ydis,
#          tipsSurfaceObj, tipsRectObj, font, fontsize)



class BubbleSortThread(SortThread):
    def __init__(self,arraySet,statusarray,sortedarray):
        super(BubbleSortThread,self).__init__(statusarray,sortedarray)
        self.arrayset = arraySet

    def run(self):
        time.sleep(1000)
        lastIndex = len(self.arrayset.numList) - 1
        print(self.runstatusarray)
        while self.runstatusarray[0] != 0:
            print('fuck')
            break
        if self.runstatusarray[0] == -1:
            return
        while lastIndex > -1:
            print(self.arrayset.numList)
            for index in range(0,lastIndex):
                time.sleep(0.01)
                colorTemp1 = self.arrayset.columnColorList[index]
                colorTemp2 = self.arrayset.columnColorList[index + 1]
                self.checkpause()
                self.arrayset.columnColorList[index] = red
                self.checkpause()
                if self.arrayset.numList[index] > self.arrayset.numList[index + 1]:
                    self.arrayset.numList[index], self.arrayset.numList[index + 1] = self.arrayset.numList[index + 1], self.arrayset.numList[index]
                    self.arrayset.columnHeightList[index], self.arrayset.columnHeightList[index + 1] = self.arrayset.columnHeightList[index + 1], self.arrayset.columnHeightList[index]
                    self.arrayset.columnColorList[index + 1] = red
                self.checkpause()
                self.arrayset.columnColorList[index] = colorTemp1
                self.arrayset.columnColorList[index + 1] = colorTemp2
            self.checkpause()
            self.arrayset.columnColorList[lastIndex] = blue
            lastIndex -= 1
        self.checkpause()
        self.arrayset.columnColorList[0] = blue
        self.sortedarray[0] = True
        return


    def checkpause(self):
        while self.runstatusarray[0] != 0:
            break

def main():
    pygame.init()
    pygame.display.set_caption('bubble')
    displaysurf = pygame.display.set_mode((width,height))
    displaysurf.fill(white)
    arraySet = ArraySet()
    sortedarray = [False]
    runstatusarray = [0]
    tipsArray = [(pauseTextSurfaceObj,pauseTextRectObj)]
    eventThread = EventMonitorThread(tipsArray,runstatusarray,sortedarray)
    drawThread = DrawPanelThread(arraySet,tipsArray,displaysurf,runstatusarray)
    sortedThread = BubbleSortThread(arraySet,runstatusarray,sortedarray)
    drawThread.start()
    eventThread.start()
    sortedThread.start()

if __name__ == '__main__':
    main()
