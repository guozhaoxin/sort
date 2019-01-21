#coding: utf-8
__author__ = 'gold'
__date__ = '2019/1/15'
__time__ = '0:39'
__filename__ = 'insert.py'

from common import SortThread,showSort,ArraySet
from locals import red,blue
import time,threading

class InsertSortThread(SortThread):

    def __init__(self, arraySet:ArraySet, lock:threading.Lock):
        super(InsertSortThread, self).__init__(arraySet, lock)

    def run(self):
        pause = 0.01

        self.checkpause()

        for index in range(len(self.arrayset.numList)):
            self.checkpause()
            self.arrayset.curColumnColor(index)
            curindex = index - 1
            tempIndex = index
            while curindex >= 0:
                self.lock.acquire()
                self.arrayset.curColumnColor(curindex)
                self.arrayset.curColumnColor(tempIndex)
                self.lock.release()
                self.checkpause()
                time.sleep(pause)
                if self.arrayset.numList[tempIndex] < self.arrayset.numList[curindex]:
                    self.lock.acquire()
                    self.arrayset.numList[tempIndex],self.arrayset.numList[curindex] = \
                    self.arrayset.numList[curindex],self.arrayset.numList[tempIndex]
                    height1 = self.arrayset.getColumnHeight(curindex)
                    height2 = self.arrayset.getColumnHeight(tempIndex)
                    self.arrayset.setColumnHeight(tempIndex,height1)
                    self.arrayset.setColumnHeight(curindex,height2)
                    self.arrayset.swapNumRect(curindex,tempIndex)
                    self.lock.release()
                else:
                    self.lock.acquire()
                    self.arrayset.resetColumnColor(tempIndex)
                    self.arrayset.resetColumnColor(curindex)
                    self.lock.release()
                    self.checkpause()
                    time.sleep(pause)
                    break
                self.arrayset.curColumnColor(index)
                self.checkpause()
                time.sleep(pause)
                self.lock.acquire()
                self.arrayset.resetColumnColor(tempIndex)
                self.lock.release()
                self.checkpause()
                time.sleep(pause)
                curindex -= 1
                tempIndex -= 1
            self.lock.acquire()
            self.arrayset.resetColumnColor(tempIndex)
            self.lock.release()
            self.checkpause()
            time.sleep(pause)

        for index in range(len(self.arrayset.columnColorList)):
            self.arrayset.fixColumnColor(index)
        self.arrayset.setOrderly()


if __name__ == '__main__':
    # arrayset = ArraySet([3,2,1,0,0,1,7,2,3])
    # showSort([3,2,1,0,0,1,7,2,3],InsertSortThread)
    showSort(None,InsertSortThread,'insert')
