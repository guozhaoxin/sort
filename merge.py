#coding: utf-8
__author__ = 'gold'
__date__ = '2019/1/21'
__time__ = '22:03'
__filename__ = 'merge.py'

from common import ArraySet,showSort,SortThread,getNumList
import time
import threading

class MergeThread(SortThread):
    def __init__(self,arrayset,lock):
        super(MergeThread,self).__init__(arrayset,lock)

    def run(self):
        pause = 0.1
        # self.checkpause(pause)
        self.dfs(0,len(self.arrayset.numList) - 1)
        print('the ans is')
        print(self.arrayset.numList)

    def dfs(self,left,right):
        if left == right:
            return
        middle = (left + right) // 2
        self.dfs(left,middle)
        self.dfs(middle + 1,right)
        self.merge(left,middle,right)


    def merge(self,left,middle,right):
        index1 = left
        index2 = middle + 1
        res = []
        while index1 <= middle and index2 <= right:
            if self.arrayset.numList[index1] <= self.arrayset.numList[index2]:
                res.append(self.arrayset.numList[index1])
                index1 += 1
            else:
                res.append(self.arrayset.numList[index2])
                index2 += 1
        if index1 <= middle:
            while index1 <= middle:
                res.append(self.arrayset.numList[index1])
                index1 += 1
        if index2 <= right:
            while index2 <= right:
                res.append(self.arrayset.numList[index2])
                index2 += 1
        index = left
        for num in res:
            self.arrayset.numList[index] = num
            index += 1


if __name__ == '__main__':
    # array = getNumList(count=10)
    # th = MergeThread(ArraySet(array),None)
    # th.start()
    showSort(None,MergeThread,'merge')