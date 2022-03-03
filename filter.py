# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 16:24:52 2022

@author: emreo
"""
from scipy import signal
import matplotlib.pyplot as plt
import numpy as np 

t = np.linspace(-1, 1, 201)

f1 = 0.75
w1 = 2*np.pi*f1

f2 = 1.25
w2 = 2*np.pi*f2

f3 = 3.85
w3 = 2*np.pi*f3

s1=      np.sin(w1 * t *(1.5-t))
s2=  0.1*np.sin(w2 * t + 1)
s3= 0.18*np.cos(w3 * t)
s4_noise = 0.08*np.random.randn(len(t))

"""---------------------------------------------
"""

x = (s1+s2+s3)
xn = x + s4_noise

"""---------------------------------------------
"""
b, a = signal.butter(3, 0.6)

zi = signal.lfilter_zi(b, a)

z1, _ = signal.lfilter(b, a, xn, zi=zi*xn[0])
z2, _ = signal.lfilter(b, a, z1, zi=zi*xn[0])


y = signal.filtfilt(b, a, xn)


"""---------------------------------------------
"""
plt.figure
plt.plot(t, xn, 'b',    alpha =0.75)
plt.plot(t, z1, 'r--',  alpha =0.75)
plt.plot(t, z2, 'r',    alpha =0.75)
plt.plot(t, y,  'k',    alpha =0.75)

#plt.plot(t, z1, 'g', t, z2, 'r', t, y, 'k')

plt.legend(('noisy signal', 'lfilter, once','lfilter, twice', 'filtfilt'), loc='best')

plt.grid(True)
plt.show()

"""---------------------------------------------
"""