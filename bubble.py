#coding: utf-8
__author__ = 'gold'
__date__ = '2019/1/5'
__time__ = '17:07'
__filename__ = 'bubble.py'

from common import SortThread,showSort
from locals import red,blue
import time


class BubbleSortThread(SortThread):
    '''
    the bubble thread
    '''
    def __init__(self,arraySet,lock):
        super(BubbleSortThread,self).__init__(arraySet,lock)

    def run(self):
        pausetime = 0.01 # the pause time as the sort is very quick,the color change may be not captured by
                        # the draw thread,so the thread must stay for a while.
        # here is used to juede if the user has decided to sort.
        flag = True
        while flag:
            time.sleep(pausetime)
            if self.arrayset.getState() != 0:
                flag = False
        # the bubble sort.
        lastIndex = len(self.arrayset.numList) - 1
        while lastIndex > -1:
            for index in range(0,lastIndex):
                colorTemp1 = self.arrayset.columnColorList[index]
                colorTemp2 = self.arrayset.columnColorList[index + 1]
                self.checkpause()
                self.lock.acquire()
                self.arrayset.columnColorList[index] = red
                if self.arrayset.numList[index] > self.arrayset.numList[index + 1]:
                    self.arrayset.numList[index], self.arrayset.numList[index + 1] = self.arrayset.numList[index + 1], self.arrayset.numList[index]
                    self.arrayset.columnHeightList[index], self.arrayset.columnHeightList[index + 1] = self.arrayset.columnHeightList[index + 1], self.arrayset.columnHeightList[index]
                    self.arrayset.columnColorList[index + 1] = red
                    self.arrayset.swapNumRect(index,index + 1) # please remember to swap 2 columns' information.
                self.lock.release()
                time.sleep(pausetime)
                self.checkpause()
                self.lock.acquire()
                self.arrayset.columnColorList[index] = colorTemp1
                self.arrayset.columnColorList[index + 1] = colorTemp2
                self.lock.release()
            self.checkpause()
            self.arrayset.columnColorList[lastIndex] = blue
            lastIndex -= 1
        self.checkpause()
        self.arrayset.columnColorList[0] = blue
        self.arrayset.setOrderly()
        return

if __name__ == '__main__':
    showSort(None,BubbleSortThread)