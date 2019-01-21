#coding: utf-8
__author__ = 'gold'
__date__ = '2019/1/21'
__time__ = '20:07'
__filename__ = 'shell.py'

from common import SortThread,showSort,ArraySet
import time
import threading

class ShellThread(SortThread):
    def __init__(self,arrayset,lock):
        super().__init__(arrayset,lock)

    def run(self):
        pause = 0.01
        self.checkpause(pause)
        steps = [8,5,3,2,1] # the shell steps list
        for step in steps:
            for index in range(len(self.arrayset.numList)):
                curIndex = index - step
                latterIndex = index
                self.lock.acquire()
                self.arrayset.curColumnColor(index)
                self.lock.release()
                self.checkpause(pause)
                time.sleep(pause)
                while curIndex >= 0:
                    self.lock.acquire()
                    self.arrayset.curColumnColor(curIndex)
                    self.arrayset.curColumnColor(latterIndex)
                    self.lock.release()
                    self.checkpause(pause)
                    time.sleep(pause)
                    if self.arrayset.numList[curIndex] <= self.arrayset.numList[latterIndex]:
                        self.lock.acquire()
                        self.arrayset.resetColumnColor(latterIndex)
                        self.arrayset.resetColumnColor(curIndex)
                        self.lock.release()
                        self.checkpause(pause)
                        time.sleep(pause)
                        break
                    self.lock.acquire()
                    self.arrayset.numList[curIndex],self.arrayset.numList[latterIndex] = \
                    self.arrayset.numList[latterIndex],self.arrayset.numList[curIndex]
                    height1,height2 = self.arrayset.getColumnHeight(curIndex),self.arrayset.getColumnHeight(latterIndex)
                    self.arrayset.setColumnHeight(curIndex,height2)
                    self.arrayset.setColumnHeight(latterIndex,height1)
                    self.arrayset.swapNumRect(curIndex,latterIndex)
                    self.lock.release()
                    self.checkpause()
                    time.sleep(pause)
                    self.lock.acquire()
                    if latterIndex != index:
                        self.arrayset.resetColumnColor(latterIndex)
                    self.lock.release()
                    self.checkpause()
                    time.sleep(pause)
                    latterIndex = curIndex
                    curIndex -= step
                self.lock.acquire()
                # if step == 1:
                #     self.arrayset.fixColumnColor(latterIndex)
                # else:
                self.arrayset.resetColumnColor(index)
                self.arrayset.resetColumnColor(latterIndex)
                if curIndex >= 0:
                    self.arrayset.resetColumnColor(curIndex)
                self.lock.release()
                self.checkpause()
                time.sleep(pause)
        for index in range(len(self.arrayset.numList)):
            self.arrayset.fixColumnColor(index)
        self.arrayset.setOrderly()

if __name__ == '__main__':
    array = [3,2,1,0,0,1,2,3,7,4]
    showSort([],ShellThread,'shell')