#coding: utf-8
__author__ = 'gold'
__date__ = '2019/1/5'
__time__ = '17:09'
__filename__ = 'common.py'

import random
import os
from pygame.locals import KEYDOWN,K_ESCAPE
import pygame

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

def getNumList():

    '''
    this function is used to get a num list with random integer between 0 and 100
    :return: [int]
    '''

    a = [random.randint(0,100) for i in range(100)]
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
            pygame.quit()
            exit()
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

