#coding: utf-8
__author__ = 'gold'
__date__ = '2019/1/5'
__time__ = '17:07'
__filename__ = 'bubble.py'

import pygame
from pygame.locals import K_SPACE,K_ESCAPE
from common import eventHandle,draw,exitGame,start,end,prepare
from locals import red,blue,white,\
    yDis,numFontSize,numFont,\
    exitTextRectObj,exitTextSurfaceObj,\
    pauseTextRectObj,pauseTextSurfaceObj,\
    contTextRectObj,contTextSurfaceObj,\
    startTextRectObj,startTextSurfaceObj


def sort(displaysurf,numList,numPosList,columnColorList,numColorList,coloHeightList,colWidth,middle,ydis,tipsSurfaceObj,tipsRectObj,font,fontsize,bg = white,contSur = contTextSurfaceObj,contRect = contTextRectObj):
    lastIndex = len(numList) - 1
    clock = pygame.time.Clock()
    while lastIndex >= -1:
        for index in range(lastIndex):
            colorTemp1 = columnColorList[index]
            colorTemp2 = columnColorList[index + 1]
            columnColorList[index] = red
            if numList[index] > numList[index + 1]:
                numList[index],numList[index + 1] = numList[index + 1],numList[index]
                coloHeightList[index],coloHeightList[index + 1] = coloHeightList[index + 1],coloHeightList[index]
                columnColorList[index + 1] = red

            draw(displaysurf,numList,numPosList,columnColorList,numColorList,coloHeightList,colWidth,middle,ydis,tipsSurfaceObj,tipsRectObj,font,fontsize,bg)
            columnColorList[index] = colorTemp1
            columnColorList[index + 1] = colorTemp2
            key = eventHandle(pygame.event.get())
            if key == K_SPACE:
                while True:
                    draw(displaysurf, numList, numPosList, columnColorList, numColorList, coloHeightList, colWidth,
                         middle, ydis, contSur, contRect, font, fontsize)
                    key = eventHandle(pygame.event.get())
                    if key == K_SPACE:
                        break
                    elif key == K_ESCAPE:
                        exitGame()
            pygame.display.update()
            clock.tick(30)
        columnColorList[lastIndex] = blue
        lastIndex -= 1
    columnColorList[0] = blue
    draw(displaysurf, numList, numPosList, columnColorList, numColorList, coloHeightList, colWidth, middle, ydis,
         tipsSurfaceObj, tipsRectObj, font, fontsize)


def main():
    start(prepare.displaysurf,prepare.numArray,prepare.columnPosList,prepare.columnColor,prepare.numColor,
          prepare.columnHeightList,prepare.columnWidth,prepare.columnWidth // 2,yDis,startTextSurfaceObj,startTextRectObj,numFont,numFontSize)
    sort(prepare.displaysurf, prepare.numArray, prepare.columnPosList, prepare.columnColor, prepare.numColor,
          prepare.columnHeightList, prepare.columnWidth, prepare.columnWidth // 2, yDis, pauseTextSurfaceObj, pauseTextRectObj,numFont,numFontSize)
    end(prepare.displaysurf, prepare.numArray, prepare.columnPosList, prepare.columnColor, prepare.numColor,
          prepare.columnHeightList, prepare.columnWidth, prepare.columnWidth // 2, yDis, exitTextSurfaceObj, exitTextRectObj,numFont,numFontSize)


if __name__ == '__main__':
    main()