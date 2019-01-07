#coding: utf-8
__author__ = 'gold'
__date__ = '2019/1/5'
__time__ = '16:39'
__filename__ = 'test6.py'

import numpy as np
import matplotlib.pyplot as plt

N = 5
y1 = [20, 10, 30, 25, 15]
y2 = [15, 14, 34, 10, 5]
index = np.arange(5)

bar_width = 0.3
plt.bar(index, y1, width=0.3, color='r')
plt.bar(index + bar_width, y2, width=.3, color='g')


plt.show()