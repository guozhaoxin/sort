#coding: utf-8
__author__ = 'gold'
__date__ = '2019/1/23'
__time__ = '16:10'
__filename__ = 'quick_kth.py'

from common import ArraySet,showSort,statusShow,SortThread,getNumList
import threading
import time

class QuickKthThread(SortThread):
    def __init__(self,arrayset:ArraySet,lock:threading.Lock,kth:int = 0):
        super(QuickKthThread,self).__init__(arrayset,lock)
        self.pause = 0.01
        kth -= 1
        if kth < 0:
            kth = 0
        if kth >= len(self.arrayset.numList):
            kth = len(self.arrayset.numList) - 1
        self.kth = kth

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
        if partion == self.kth:
            print('in quick the ans is',self.arrayset.numList[partion])
            self.arrayset.kthColumnColor(partion)
            return
        elif partion > self.kth:
            self.quick(left,partion - 1)
            self.checkpause(self.pause)
        else:
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
                if self.arrayset.numList[right] <= base:
                    self.lock.acquire()
                    self.arrayset.resetColumnColor(right)
                    self.lock.release()
                    self.checkpause(self.pause)
                    time.sleep(self.pause)
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
                if self.arrayset.numList[left] >= base:
                    self.lock.acquire()
                    self.arrayset.resetColumnColor(left)
                    self.lock.release()
                    self.checkpause(self.pause)
                    time.sleep(self.pause)
                    left += 1
                else:
                    break
            self.swapNum(left,right)
            self.arrayset.swapNumRect(left, right)
            if left != right:
                self.lock.acquire()
                self.arrayset.resetColumnColor(right)
                self.lock.release()
                self.checkpause(self.pause)
                time.sleep(self.pause)
            height1, height2 = self.arrayset.getColumnHeight(left), self.arrayset.getColumnHeight(right)
            self.arrayset.setColumnHeight(left, height2)
            self.arrayset.setColumnHeight(right, height1)

        return left

if __name__ == '__main__':
    count = 30 # how long the array
    numList = getNumList(count = count)
    import copy
    b = copy.deepcopy(numList)
    b.sort(reverse=True)
    import random
    kth = random.randint(0,count)
    if kth < 0:
        kth = 0
    if kth >= len(b):
        kth = len(b) - 1
    print('the whole array sorted :',b)
    print('the %dth ele is %d' % (kth,b[kth - 1]))
    showSort(numList,QuickKthThread,'kth',kth = kth)
