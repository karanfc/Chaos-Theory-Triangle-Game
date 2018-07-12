# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import matplotlib.pyplot as plt
import random
global Ux, Uy

fig = plt.figure()

Ax = 30
Ay = 40

Bx = 70
By = 40

Cx = 50
Cy = 50

plt.plot(Ax, Ay, 'ro')
plt.plot(Bx, By, 'ro')
plt.plot(Cx, Cy, 'ro')
plt.grid()
plt.show()

def onclick(event):
    ix, iy = event.xdata, event.ydata
    Ux = ix;
    Uy = iy;
    plt.plot(Ux, Uy, 'ro')

    
    for i in range(0,100000):
        rand = random.randint(1,7)
        if rand == 1 or rand == 2:
            cx = (ix + Ax)/2
            cy = (iy + Ay)/2
            plt.plot(cx,cy,'ro')
        elif rand == 3 or rand == 4:
            cx = (ix + Bx)/2
            cy = (iy + By)/2
            plt.plot(cx,cy,'ro')
        else:
            cx = (ix + Cx)/2
            cy = (iy + Cy)/2
            plt.plot(cx,cy,'ro')
        ix = cx
        iy = cy

    
for i in xrange(0,1):
    cid = fig.canvas.mpl_connect('button_press_event', onclick)
    