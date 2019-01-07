#coding: utf-8
__author__ = 'gold'
__date__ = '2019/1/5'
__time__ = '17:07'
__filename__ = 'bubble.py'

import pygame
from pygame.locals import K_SPACE
from common import getNumList,getMax,getMin,validNumList,eventHandle,getDistance,getScale,drawNum
from locals import width,height,yellow,red,blue,white,green,startX,startY,endX,endY,base,font,textRectObj,textSurfaceObj



def draw(numlist):
    global DISPLAYSURF
    DISPLAYSURF = pygame.display.set_mode((width,height))
    DISPLAYSURF.fill(white)
    valid = validNumList(numlist)
    if not valid:
        return

    low = getMin(numlist)
    high = getMax(numlist)
    startX = width * 0.1
    startY = height * 0.9
    endX = width * 0.9
    endY = height * 0.1

    distance = (endX - startX) // len(numlist)

    base = 0.1 * height
    if low == high:
        scale = 1
    else:
        scale = 1 / (high - low)

    while True:
        for index in range(len(numlist)):
            if index == 0:
                if scale == 1:
                    pygame.draw.rect(DISPLAYSURF,red,(distance * index + startX,startY,distance * 0.8,- 0.8 * height))
                else:
                    pygame.draw.rect(DISPLAYSURF,red,(distance * index + startX,startY,distance * 0.8,- base - (numlist[index] - low) * scale * 0.7 * height))
            else:
                if scale == 1:
                    pygame.draw.rect(DISPLAYSURF,blue,(distance * index + startX,startY,distance *0.8,- 0.8 * height))
                else:
                    pygame.draw.rect(DISPLAYSURF,blue,(distance * index + startX,startY,distance * 0.8,- base - (numlist[index] - low) * scale * 0.7 * height))

        pygame.display.update()
        eventHandle(pygame.event.get())

def showStart(numList,displaysurf,distance,scale,low):
    colwidth = int(distance * 0.8)
    colMostHeight = int(height * 0.8)
    numWid = distance // 2
    numHei = height // 20
    fontsize = (numHei + numWid) // 2 * 4 // 5
    sameNumPos = 0.08 * height
    while True:
        for index in range(len(numList)):
            x = distance * index + startX
            if scale == 1:
                pygame.draw.rect(displaysurf,green,(x,startY,colwidth,-colMostHeight))
                numSurfaceObj, numRectObj = drawNum(str(numList[index]),x + numWid, sameNumPos,blue,
                                                      fontsize,font)
                displaysurf.blit(numSurfaceObj,numRectObj)
            else:
                colHei = - base - (numList[index] - low) * scale * 0.7 * height
                pygame.draw.rect(displaysurf, green, (x, startY, colwidth, colHei))
                numSurfaceObj, numRectObj = drawNum(str(numList[index]), x + numWid, 0.9 * height + colHei - 0.01 * height, blue,
                                                      fontsize, font)
                displaysurf.blit(numSurfaceObj, numRectObj)
        displaysurf.blit(textSurfaceObj,textRectObj)
        pygame.display.update()
        key = eventHandle(pygame.event.get())
        if key == K_SPACE:
            return

def beginShow(numList,displaysurf,distance,scale,low):
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

def endShow(numList,displaysurf,distance,scale,low):
    pass

def main():
    a = getNumList()
    # a.append(-100)
    print(a)
    res = validNumList(a)
    if not res:
        print('error:the list is invalid,please check')
        exit()
    # a = [20] * 20
    low = getMin(a)
    high = getMax(a)
    distance = getDistance(startX,endX,len(a))
    scale = getScale(low,high)
    pygame.display.set_caption('bubble')
    DISPLAYSURF = pygame.display.set_mode((width, height))
    DISPLAYSURF.fill(white)
    showStart(a,DISPLAYSURF,distance,scale,low)
    beginShow(a,DISPLAYSURF,distance,scale,low)
    showEnd(a,DISPLAYSURF,distance,scale,low)


if __name__ == '__main__':
    main()