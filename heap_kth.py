#coding: utf-8
__author__ = 'gold'
__date__ = '2019/1/23'
__time__ = '19:17'
__filename__ = 'heap_kth.py'

from common import SortThread,ArraySet,showSort,getNumList
import time
import threading

class HeapKthThread(SortThread):
    def __init__(self,arrayset:ArraySet,lock:threading.Lock,kth = 0):
        super(HeapKthThread,self).__init__(arrayset,lock)
        if kth < 0:
            kth = 0
        if kth >= len(self.arrayset.numList):
            kth = len(self.arrayset.numList)
        self.kth = kth
        self.pause = 0.001

    def run(self):
        self.checkpause(self.pause)
        self.buildHeap()
        last = len(self.arrayset.numList) - 1
        for index in range(last,-1,-1):
            self.swap(0,index)
            self.lock.acquire()
            self.arrayset.fixColumnColor(index)
            self.lock.release()
            self.checkpause(self.pause)
            time.sleep(self.pause)
            if (len(self.arrayset.numList) - index) == self.kth:
                self.arrayset.kthColumnColor(index)
                print('in heap the ans is',self.arrayset.numList[index])
                break
            self.dfs(0,index)
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
    count = 30 # how long the array
    array = getNumList(count = count)
    import copy,random
    b = copy.deepcopy(array)
    b.sort(reverse=True)
    kth = random.randint(0,count)
    if kth < 0:
        kth = 0
    if kth >= len(b):
        kth = len(b) - 1
    print('the whole array sorted :',b)
    print('the %dth ele is %d' % (kth,b[kth - 1]))
    showSort(array,HeapKthThread,'heap-kth',kth = kth)