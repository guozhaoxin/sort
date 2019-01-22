#coding: utf-8
__author__ = 'gold'
__date__ = '2019/1/22'
__time__ = '23:25'
__filename__ = 'quick.py'

from common import showSort,SortThread
import time
import threading

class QuickThread(SortThread):
    def __init__(self,arrayset,lock):
        super(QuickThread,self).__init__(arrayset,lock)
        self.pause = 0.005

    def run(self):
        self.checkpause(self.pause)
        self.quick(0,len(self.arrayset.numList) - 1)
        self.arrayset.setOrderly()

    def quick(self,left,right):
        partion = self.partion(left,right)
        self.lock.acquire()
        self.arrayset.fixColumnColor(partion)
        self.lock.release()
        self.checkpause(self.pause)
        time.sleep(self.pause)
        if partion > left:
            self.quick(left,partion - 1)
        self.checkpause(self.pause)
        if partion < right:
            self.quick(partion + 1,right)
        self.checkpause(self.pause)

    def partion(self,left,right):
        base = self.arrayset.numList[left]
        self.lock.acquire()
        self.arrayset.curColumnColor(left)
        self.lock.release()
        self.checkpause(self.pause)
        time.sleep(self.pause)
        while left < right:
            self.checkpause(self.pause)
            while left < right:
                self.lock.acquire()
                self.arrayset.curColumnColor(right)
                self.lock.release()
                self.checkpause(self.pause)
                time.sleep(self.pause)
                if self.arrayset.numList[right] >= base:
                    right -= 1
                else:
                    break
            self.swapNum(left,right)
            self.arrayset.swapNumRect(left,right)
            height1,height2 = self.arrayset.getColumnHeight(left),self.arrayset.getColumnHeight(right)
            self.arrayset.setColumnHeight(left,height2)
            self.arrayset.setColumnHeight(right,height1)
            if left != right:
                self.lock.acquire()
                self.arrayset.resetColumnColor(left)
                self.lock.release()
                self.checkpause(self.pause)
                time.sleep(self.pause)
            while left < right:
                self.checkpause(self.pause)
                self.lock.acquire()
                self.arrayset.curColumnColor(left)
                self.lock.release()
                self.checkpause(self.pause)
                time.sleep(self.pause)
                if self.arrayset.numList[left] <= base:
                    left += 1
                else:
                    break
            self.swapNum(left,right)

            self.arrayset.swapNumRect(left, right)
            height1, height2 = self.arrayset.getColumnHeight(left), self.arrayset.getColumnHeight(right)
            self.arrayset.setColumnHeight(left, height2)
            self.arrayset.setColumnHeight(right, height1)

        return left

if __name__ == '__main__':
    showSort(None,QuickThread,'quick')