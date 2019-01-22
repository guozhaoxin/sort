#coding: utf-8
__author__ = 'gold'
__date__ = '2019/1/22'
__time__ = '10:34'
__filename__ = 'heap.py'

from common import SortThread,showSort
import time

class HeapThread(SortThread):
    def __init__(self,arrayset,lock):
        super(HeapThread,self).__init__(arrayset,lock)
        self.pause = 0.005

    def run(self):
        self.checkpause(self.pause)
        self.buildHeap()
        print(self.arrayset.numList)
        last = len(self.arrayset.numList) - 1
        for index in range(last,-1,-1):
            self.swap(0,index)
            self.lock.acquire()
            self.arrayset.fixColumnColor(index)
            self.lock.release()
            self.checkpause(self.pause)
            time.sleep(self.pause)
            self.dfs(0,index)
        self.arrayset.fixColumnColor(0)
        print(self.arrayset.numList)
        self.arrayset.setOrderly()


    def dfs(self,index,last):
        leftInd = index * 2 + 1
        rightInd = leftInd + 1
        maxInd = index
        maxNum = self.arrayset.numList[index]
        self.lock.acquire()
        self.arrayset.curColumnColor(index)
        self.lock.release()
        self.checkpause(self.pause)
        time.sleep(self.pause)
        if leftInd < last:
            self.lock.acquire()
            self.arrayset.curColumnColor(leftInd)
            if maxNum < self.arrayset.numList[leftInd]:
                maxInd = leftInd
                maxNum = self.arrayset.numList[leftInd]
            self.lock.release()
            self.checkpause(self.pause)
            time.sleep(self.pause)
            if maxInd != leftInd:
                self.lock.acquire()
                self.arrayset.resetColumnColor(leftInd)
                self.lock.release()
                self.checkpause(self.pause)
                time.sleep(self.pause)
        if rightInd < last:
            self.lock.acquire()
            self.arrayset.curColumnColor(rightInd)
            if maxNum < self.arrayset.numList[rightInd]:
                self.arrayset.resetColumnColor(leftInd)
                maxInd = rightInd
            self.lock.release()
            self.checkpause(self.pause)
            time.sleep(self.pause)
            if rightInd != maxInd:
                self.lock.acquire()
                self.arrayset.resetColumnColor(rightInd)
                self.lock.release()
                self.checkpause(self.pause)
                time.sleep(self.pause)
        if index != maxInd:
            self.swap(index,maxInd)
            self.lock.acquire()
            self.arrayset.resetColumnColor(index)
            if leftInd < last:
                self.arrayset.resetColumnColor(leftInd)
            if rightInd < last:
                self.arrayset.resetColumnColor(rightInd)
            self.lock.release()
            self.dfs(maxInd,last)
        self.arrayset.resetColumnColor(index)

    def buildHeap(self):
        middle = len(self.arrayset.numList) // 2
        self.checkpause(self.pause)
        for index in range(middle,-1,-1):
            self.dfs(index,len(self.arrayset.numList))


    def swap(self,index1,index2):
        self.arrayset.numList[index1],self.arrayset.numList[index2] = \
        self.arrayset.numList[index2],self.arrayset.numList[index1]
        self.arrayset.swapNumRect(index1,index2)
        height1,height2 = self.arrayset.getColumnHeight(index1),self.arrayset.getColumnHeight(index2)
        self.arrayset.setColumnHeight(index1,height2)
        self.arrayset.setColumnHeight(index2,height1)

if __name__ == '__main__':
    showSort(None,HeapThread,'heap')
