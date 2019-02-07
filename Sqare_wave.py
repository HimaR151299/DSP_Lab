#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 17:16:26 2019

@author: rgukt
"""

#/*Square waveform genaration*/
from scipy import signal as sg
import numpy as np
from matplotlib import pyplot as plt
t=np.linspace(0,1,1000,endpoint=True)
x=sg.square(2*np.pi*10*t,0.33)
plt.plot(t,x)
plt.show()
