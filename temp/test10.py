#coding: utf-8
__author__ = 'gold'
__date__ = '2019/1/5'
__time__ = '22:22'
__filename__ = 'test10.py'

import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((600, 500))
pygame.display.set_caption("drawing a rectangle")
pos_x = 300
pos_y = 250
vel_x = 2                            # 设置速度变量
vel_y = 1
while True:
    for event in pygame.event.get():
        if event.type in (QUIT, KEYDOWN):
            exit()
    screen.fill((0, 0, 200))
    pos_x += vel_x
    pos_y += vel_y

    if pos_x > 500 or pos_x < 0:
        vel_x = -vel_x                       # 让矩形在窗口范围内移动
    if pos_y > 400 or pos_y < 0:
        vel_y = -vel_y
    color = 255, 255, 0
    width = 0
    pos = pos_x, pos_y, 100, 100             # 矩形长和宽都为100
    pygame.draw.rect(screen, color, pos, width)
    pygame.display.update()