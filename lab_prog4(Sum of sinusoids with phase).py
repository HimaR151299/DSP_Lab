#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  24 15:23:53 2019

@author: rgukt
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(0,0.01,1000)
f1=input("f1:")
f2=input("f2:")
fs=2*max(f1,f2)
print fs
s=np.sin(2*np.pi*f1*x)
plt.subplot(221)
plt.plot(x,s)
plt.xlabel("...>Time")
plt.ylabel("...>Amplitude(f1)")
plt.show()
v=3*(np.sin(2*np.pi*f2*x)+(np.pi))
plt.subplot(222)
plt.plot(x,v)
plt.xlabel("...>Time")
plt.ylabel("...>Amplitude(f2)")
plt.show()
u=5*(np.sin(2*np.pi*fs*x))
plt.subplot(223)
plt.plot(x,u)
plt.xlabel("...>Time")
plt.ylabel("...>Amplitude(fs)")
plt.show()
h=s+v
plt.subplot(224)
plt.plot(x,h)
plt.xlabel("...>Time")
plt.ylabel("...>Amplitude(rst)")
plt.show()

