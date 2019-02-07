#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 13:50:22 2019

@author: sri
"""

import scipy.io.wavfile as wav
import numpy as np
from matplotlib import pyplot as plt
#/home/rgukt/.config/spyder/e.wav
fs,data=wav.read('e.wav')
print(fs,len(data),data)
plt.subplot(221)
plt.plot(data)
plt.show()
t=np.arange(0,len(data)/fs,1.0/fs)
plt.subplot(222)
plt.plot(t,data)
plt.show()
#wav.write('e_fast.wav',2*fs,data)
wav.write('e_slow-s.wav',0.5*fs,data)
fs1,data1=wav.read('e_slow-s.wav')
print(fs1,len(data1),data1)
plt.subplot(223)
plt.plot(data1)
plt.show()
t=np.arange(0,len(data1)/fs1,1.0/fs1)
plt.subplot(224)
plt.plot(t,data1)
plt.show()
#/home/rgukt/.config/spyder/e_slow-s.wav