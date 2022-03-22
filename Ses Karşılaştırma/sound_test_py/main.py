import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["figure.figsize"] = [16, 12]
plt.rcParams.update({"font.size": 18})

dt = 0.001
time =np.arange(0, 0.5, dt)

f1 = 50     #Hz
f2 = 120    #Hz

w1 = 2*np.pi*f1
w2 = 2*np.pi*f2


f = 1.2*np.sin(w1*time) + np.sin(w2*time)
fnoise = 3*np.random.random(len(time))
                              
                              
f_clean = f
f = f + fnoise


fig, axs = plt.subplots(4, 1)

plt.sca(axs[0])
plt.plot(time, f_clean, color="r", LineWidth = 1.5, Label ="Signal")
plt.legend()
plt.xlim(time[0], time[-1])

plt.sca(axs[1])
plt.plot(time, fnoise, color="g", LineWidth = 1.5, Label ="Noise")
plt.legend()
plt.xlim(time[0], time[-1])

plt.sca(axs[2])
plt.plot(time, f, color="b", LineWidth=1.8, Label ="Signal+Noise")
plt.legend()
plt.xlim(time[0], time[-1])

plt.sca(axs[3])
plt.plot(time, f, color="b", LineWidth=1.8, Label ="Signal+Noise")
plt.plot(time, f_clean, color="r", LineWidth = 1.5, Label ="Signal")
plt.legend()
plt.xlim(time[0], time[-1])

plt.legend()
plt.show()

#----------------------------------------------


n = len(time)       #1000 adet zaman noktası

fhat = np.fft.fft(f , n )
PSD  = fhat * np.conj(fhat) / n
freq = (1/(dt*n)) * np.arange(n)
L    = np.arange(1,np.floor(n/2),dtype="int")

fig, axs = plt.subplots(2, 1)
plt.sca(axs[0])
plt.plot(time, f, color="c", LineWidth=1.5, Label="Signal+Noise")
plt.plot(time, f_clean, color="k", LineWidth=2, Label="Signal")
plt.xlim(time[0], time[-1])
plt.legend()

plt.sca(axs[1])
plt.plot(freq[L], PSD[L], color="c", LineWidth=1.5, Label="Signal+Noise")
plt.xlim(freq[L[0]], freq[L[-1]])
plt.legend()

plt.show()

#----------------------------------------------

indices = PSD > 100
PSDclean = PSD * indices 
fhat = fhat * indices
ffilt = np.fft.ifft(fhat)



fig, axs = plt.subplots(3, 1)
plt.sca(axs[0])
plt.plot(time, f, color="c", LineWidth=1.5, Label="Signal+Noise")
plt.plot(time, f_clean, color="k", LineWidth=2, Label="Signal")
plt.xlim(time[0], time[-1])
plt.legend()

plt.sca(axs[1])
plt.plot(time, ffilt, color="k", LineWidth=1.5, Label="Filtered")
plt.xlim(time[0], time[-1])
plt.legend()

plt.sca(axs[2])
plt.plot(freq[L], PSD[L], color="c", LineWidth=1.5, Label="Signal+Noise")
plt.plot(freq[L], PSDclean[L], color="k", LineWidth=1.5, Label="Filtered")
plt.xlim(freq[L[0]], freq[L[-1]])
plt.legend()

plt.show()








