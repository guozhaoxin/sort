#coding: utf-8
__author__ = 'gold'
__date__ = '2019/1/21'
__time__ = '17:06'
__filename__ = 'selection.py'

from common import showSort,SortThread,ArraySet
import threading
import time

class SelectionThread(SortThread):
    def __init__(self,arrayset:ArraySet,lock:threading.Lock):
        super(SelectionThread,self).__init__(arrayset,lock)

    def run(self):
        pause = 0.01
        self.checkpause(pause)

        for index in range(len(self.arrayset.numList)):
            self.lock.acquire()
            self.arrayset.curColumnColor(index)
            self.lock.release()
            self.checkpause(pause)
            time.sleep(pause)
            smallIndex = index
            smallNum = self.arrayset.numList[index]
            for curIndex in range(index + 1,len(self.arrayset.numList)):
                self.lock.acquire()
                self.arrayset.curColumnColor(curIndex)
                self.lock.release()
                self.checkpause()
                time.sleep(pause)
                if smallNum > self.arrayset.numList[curIndex]:
                    self.lock.acquire()
                    if smallIndex != index:
                        self.arrayset.resetColumnColor(smallIndex)
                    smallNum = self.arrayset.numList[curIndex]
                    smallIndex = curIndex
                    self.arrayset.curColumnColor(curIndex)
                    self.lock.release()
                    self.checkpause()
                    time.sleep(pause)
                self.lock.acquire()
                if curIndex == smallIndex:
                    self.arrayset.curColumnColor(curIndex)
                else:
                    self.arrayset.resetColumnColor(curIndex)
                self.lock.release()
                self.checkpause(pause)
                time.sleep(pause)
            if smallIndex != index:
                self.lock.acquire()
                self.arrayset.numList[index],self.arrayset.numList[smallIndex] = \
                self.arrayset.numList[smallIndex],self.arrayset.numList[index]
                height1,height2 = self.arrayset.getColumnHeight(index),self.arrayset.getColumnHeight(smallIndex)
                self.arrayset.setColumnHeight(index,height2)
                self.arrayset.setColumnHeight(smallIndex,height1)
                self.arrayset.swapNumRect(index,smallIndex)
                self.lock.release()
                self.checkpause(pause)
                time.sleep(pause)
                self.lock.acquire()
                self.arrayset.resetColumnColor(smallIndex)
                self.lock.release()
                self.checkpause(pause)
                time.sleep(pause)
            self.checkpause(pause)
            time.sleep(pause)
            self.lock.acquire()
            self.arrayset.fixColumnColor(index)
            self.lock.release()
            self.checkpause()
            time.sleep(pause)
        self.arrayset.setOrderly()
        print(self.arrayset.numList)

if __name__ == '__main__':
    array = [3,2,1,0,0,1,2,3]
    showSort([],SelectionThread,'selection')
