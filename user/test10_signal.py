from scipy import signal
import matplotlib.pyplot as plt
import numpy as np
t = np.linspace(-1, 1, 201)
x = (0.3*np.sin(2*np.pi*0.75*t*(1-t) + 2.1) +0.5*np.sin(2*np.pi*2*t + 1) +2*np.cos(2*np.pi*1*t))


xn = x + np.random.randn(len(t)) * 0.5

b, a = signal.butter(5, 0.17)

zi = signal.lfilter_zi(b, a)
z, _ = signal.lfilter(b, a, xn, zi=zi*xn[0])

z2, _ = signal.lfilter(b, a, z, zi=zi*z[0])

y = signal.filtfilt(b, a, xn)

plt.figure
plt.plot(t, xn, 'r', alpha=0.75)
plt.plot( t, y, 'b')
plt.legend(('noisy signal', 'lfilter, once', 'lfilter, twice',
            'filtfilt'), loc='best')
plt.grid(True)
plt.show()