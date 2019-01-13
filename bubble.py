#coding: utf-8
__author__ = 'gold'
__date__ = '2019/1/5'
__time__ = '17:07'
__filename__ = 'bubble.py'

import pygame,time
from pygame.locals import K_SPACE,K_ESCAPE
from common import getNumList,getMax,getMin,validNumList,eventHandle,getDistance,getScale,drawNum,\
                    draw,exitGame
from locals import width,height,yellow,red,blue,white,green,black,startX,startY,endX,endY,base,font,\
    colScale,colMostScale,numHeiScale,numWidScale,numFontScale,yDisScale,columnMostHeight,yDis,numFontSize,numFont,\
    exitTextRectObj,exitTextSurfaceObj,\
    pauseTextRectObj,pauseTextSurfaceObj,\
    contTextRectObj,contTextSurfaceObj,\
    startTextRectObj,startTextSurfaceObj


def beginSort(numList,displaysurf,distance,scale,low):
    colwidth = int(distance * 0.8)
    colMostHeight = int(height * 0.8)
    numWid = distance // 2
    numHei = height // 20
    fontsize = (numHei + numWid) // 2 * 4 // 5
    sameNumPos = 0.08 * height
    last = len(numList) - 1
    while last >= 0:
        largest = numList[0]
        for index in range(last + 1):
            if largest < numList[index]:
                pass
        last -= 1

def start(displaysurf,numList,numPosList,columnColorList,numColorList,coloHeightList,colWidth,middle,ydis,tipsSurfaceObj,tipsRectObj,font,fontsize):
    while True:
        draw(displaysurf,numList,numPosList,columnColorList,numColorList,coloHeightList,colWidth,middle,ydis,tipsSurfaceObj,tipsRectObj,font,fontsize)
        key = eventHandle(pygame.event.get())
        if key == K_SPACE:
            return

def sort(displaysurf,numList,numPosList,columnColorList,numColorList,coloHeightList,colWidth,middle,ydis,tipsSurfaceObj,tipsRectObj,font,fontsize,bg = white,contSur = contTextSurfaceObj,contRect = contTextRectObj):
    lastIndex = len(numList) - 1
    clock = pygame.time.Clock()
    while lastIndex >= -1:
        for index in range(lastIndex):
            colorTemp = columnColorList[index]
            columnColorList[index] = red
            if numList[index] > numList[index + 1]:
                numList[index],numList[index + 1] = numList[index + 1],numList[index]
                coloHeightList[index],coloHeightList[index + 1] = coloHeightList[index + 1],coloHeightList[index]
            draw(displaysurf,numList,numPosList,columnColorList,numColorList,coloHeightList,colWidth,middle,ydis,tipsSurfaceObj,tipsRectObj,font,fontsize,bg)
            columnColorList[index] = colorTemp
            key = eventHandle(pygame.event.get())
            if key == K_ESCAPE:
                exitGame()
            elif key == K_SPACE:
                while True:
                    draw(displaysurf, numList, numPosList, columnColorList, numColorList, coloHeightList, colWidth,
                         middle, ydis, contSur, contRect, font, fontsize)
                    key = eventHandle(pygame.event.get())
                    if key == K_SPACE:
                        break
                    elif key == K_ESCAPE:
                        exitGame()
            pygame.display.update()
            clock.tick(3)
        columnColorList[lastIndex] = blue
        lastIndex -= 1
    columnColorList[0] = blue
    draw(displaysurf, numList, numPosList, columnColorList, numColorList, coloHeightList, colWidth, middle, ydis,
         tipsSurfaceObj, tipsRectObj, font, fontsize)

end = start # 两者逻辑参数都一样，只是要显示的内容不同而已。

def main():
    a = getNumList()[:10]
    print(a)
    res = validNumList(a)
    if not res:
        print('error:the list is invalid,please check')
        exitGame()
    low = getMin(a) # get the smallest num in the list
    high = getMax(a) # get the largest num in the list
    distance = getDistance(startX,endX,len(a)) # get the distance from column to column
    colWidth = int(distance * colScale) # get the column's real width
    numPosList = []
    for i in range(len(a)):
        numPosList.append(startX + distance * i)
    colHeightList = []
    colHeight = int(startY * colMostScale)
    if low == high:
        for i in range(len(a)):
            colHeightList.append(colHeight)
    else:
        for num in a:
            colHeightList.append(int(colHeight * (num - low) / (high - low)) + base)
    columnColor = [green] * len(a) # get the origin color for all the columns
    numColor = [black] * len(a)
    pygame.display.set_caption('bubble')
    DISPLAYSURF = pygame.display.set_mode((width, height))
    DISPLAYSURF.fill(white)
    print(dir(DISPLAYSURF))
    start(DISPLAYSURF,a,numPosList,columnColor,numColor,colHeightList,colWidth,colWidth // 2,yDis,startTextSurfaceObj,startTextRectObj,numFont,numFontSize)
    sort(DISPLAYSURF,a,numPosList,columnColor,numColor,colHeightList,colWidth,colWidth // 2,yDis,pauseTextSurfaceObj,pauseTextRectObj,numFont,numFontSize)
    end(DISPLAYSURF,a,numPosList,columnColor,numColor,colHeightList,colWidth,colWidth // 2,yDis,exitTextSurfaceObj,exitTextRectObj,numFont,numFontSize)


if __name__ == '__main__':
    main()