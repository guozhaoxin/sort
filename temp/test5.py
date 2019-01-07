#coding: utf-8
__author__ = 'gold'
__date__ = '2019/1/5'
__time__ = '16:20'
__filename__ = 'test5.py'

import matplotlib.pyplot as plt
fig, ax = plt.subplots()
y1 = []
for i in range(50):
    y1.append(i)  # 每迭代一次，将i放入y1中画出来
    ax.cla()   # 清除键
    ax.bar(y1, label='test', height=y1, width=0.3)
    ax.legend()
    plt.pause(0.1)

plt.show()