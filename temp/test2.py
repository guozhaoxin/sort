#coding: utf-8
__author__ = 'gold'
__date__ = '2019/1/5'
__time__ = '13:12'
__filename__ = 'test2.py'

from pylab import *

from numpy import *
x = linspace(0, 5, 10)
y = x ** 2

figure()
plot(x, y, 'r')
xlabel('x')
ylabel('y')
title('title')
show()