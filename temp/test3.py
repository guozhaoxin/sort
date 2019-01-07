#coding: utf-8
__author__ = 'gold'
__date__ = '2019/1/5'
__time__ = '13:18'
__filename__ = 'test3.py'

import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

fig = plt.figure()
data = np.random.random((255, 255))
im = plt.imshow(data, cmap='gray')


# animation function.  This is called sequentially
def animate(i):
    data = np.random.random((255, 255))
    im.set_array(data)
    return [im]


anim = animation.FuncAnimation(fig, animate, frames=200, interval=60, blit=True)
plt.show()