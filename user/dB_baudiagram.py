import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# nyquist frekansı
#b, a = scipy.signal.butter(1, cut_freq/(fs/2), 'high')

b, a = signal.butter(4, 100, 'low', analog=True)
w, h = signal.freqs(b, a)




plt.semilogx(w, 20 * np.log10(abs(h)))





plt.title('Butterworth filter frequency response')
plt.xlabel('Frequency [radians / second]')
plt.ylabel('Amplitude [dB]')
plt.margins(0, 0.1)
plt.grid(which='both', axis='both')
plt.axvline(100, color='green') # cutoff frequency
plt.show()
