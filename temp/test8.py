#coding: utf-8
__author__ = 'gold'
__date__ = '2019/1/5'
__time__ = '16:52'
__filename__ = 'test8.py'

from matplotlib import pyplot as plt
import numpy as np

fig=plt.figure(1)
ax1=plt.subplot(111)
data=np.array([15,20,18,25])
width=0.5
x_bar=np.arange(4)
print(help(ax1.bar))
rect=ax1.bar(x_bar,height=data,width=width,color="lightblue")
for rec in rect:
    x=rec.get_x()
    height=rec.get_height()
    ax1.text(x+0.1,1.02*height,str(height))

ax1.set_xticks(x_bar)
ax1.set_xticklabels(("first","second","third","fourth"))
ax1.set_ylabel("sales")
ax1.set_title("The Sales in 2016")
ax1.grid(True)
ax1.set_ylim(0,28)
plt.show()
