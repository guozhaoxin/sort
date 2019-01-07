#coding: utf-8
__author__ = 'gold'
__date__ = '2019/1/6'
__time__ = '22:24'
__filename__ = 'test11.py'

import pygame
import sys

#             R    G    B
WHITE     = (255, 255, 255)
BLACK     = (  0,   0,   0)
RED       = (255,   0,   0)
GREEN     = (  0, 255,   0)
DARKGREEN = (  0, 155,   0)
DARKGRAY  = ( 40,  40,  40)
OLIVE     = (128, 128,   0)
BLUE      = (  0,   0, 255)
NAVYBLUE  = (  0,   0, 128)

def main():
    pygame.init()
    pygame.display.set_caption("Hello world")

    screen = pygame.display.set_mode((640,480),0,32)
    #background = pygame.image.load("flippyboard.png")

    x = 640//2
    y = 480//2

    move_x,move_y = 0,0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN: #键被按下
                if event.key == pygame.K_LEFT:
                    move_x = -1
                elif event.key == pygame.K_RIGHT:
                    move_x = 1
                elif event.key == pygame.K_UP:
                    move_y = -1
                elif event.key == pygame.K_DOWN:
                    move_y = 1
            elif event.type == pygame.KEYUP:
                move_x = 0
                move_y = 0

        x = x + move_x
        y = y + move_y

        x = (x + 640)%640
        y = (y + 480)%480

        screen.fill(DARKGRAY) #重新填充屏幕背景色
        pygame.draw.circle(screen,BLUE,(x,y),30)  #在新的位置画一个画

        pygame.display.update()  #更新

if __name__ == '__main__':
    main()