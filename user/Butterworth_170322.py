import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt
import soundfile as sf
from scipy import signal

fs = 1000
time = np.arange(0,1,1/fs)

def sound_lenght(second=0):
    x=int(fs*second)
    return x

def DFT(x): # To calculate DFT of a 1D real-valued signal x
    
    N = len(x)
    n = np.arange(N)
    k = n.reshape((N, 1))
    e = np.exp(-2j * np.pi * k * n / N)
    X = np.dot(e, x)
    return X

amp=[0,1,0.1,0.01,0.001,0.0001]

s3_freq=120
s3_add_freq=100
s3_sound_length=1
s3_amp=amp[1]

sound=[]
for i in range (0,sound_lenght(s3_sound_length)):
    sound.append(
                  0.5*np.sin(2*np.pi*(40)*i/fs)
                 #+0.5*np.sin(2*np.pi*(150)*i/fs)
                 +0.25*(np.random.rand()-0.5)        
                 )

X = DFT(sound)

# calculate the frequency
N = len(X)
n = np.arange(N)
T = N/fs
freq = n/T 

n_oneside = N//2
# get the one side frequency
f_oneside = freq[:n_oneside]

# normalize the amplitude
X_oneside =X[:n_oneside]/n_oneside

plt.figure(figsize = (12, 6))
plt.subplot(323)
plt.stem(f_oneside, abs(X_oneside), 'b', \
         markerfmt=" ", basefmt="-b")
plt.xlabel('Freq (Hz)')
plt.ylabel('DFT Amplitude |X(freq)|')

plt.subplot(324)
plt.stem(f_oneside, abs(X_oneside), 'b', \
         markerfmt=" ", basefmt="-b")
plt.xlabel('Freq (Hz)')
plt.xlim(0, 60)
plt.tight_layout()

plt.subplot(321)
plt.plot(time[0:200],sound[0:200])

A=0
B=0
fsound=[]
for i in range (0,N):
    X=sound[i]
    E=X+1.1429*A-0.4127*B
    Y=0.067*E+0.135*A+0.067*B
    fsound.append(Y)
    B=A
    A=E
    
f2sound=[]
for i in range (0,N):
    X=fsound[i]
    E=X+1.1429*A-0.4127*B
    Y=0.067*E+0.135*A+0.067*B
    f2sound.append(Y)
    B=A
    A=E

plt.subplot(322)
plt.plot(time[0:200],f2sound[0:200])
     
X1 = DFT(f2sound)

# calculate the frequency
N1= len(X1)
n1 = np.arange(N1)
T1 = N1/fs
freq1 = n1/T1 

n_oneside1 = N1//2
# get the one side frequency
f_oneside1 = freq1[:n_oneside1]

# normalize the amplitude
X_oneside1 =X1[:n_oneside1]/n_oneside1

plt.figure(figsize = (12, 6))
plt.subplot(325)
plt.stem(f_oneside1, abs(X_oneside1), 'b', markerfmt=" ", basefmt="-b")
plt.xlabel('Freq (Hz)')
plt.ylabel('DFT Amplitude |X(freq)|')

plt.subplot(326)
plt.stem(f_oneside1, abs(X_oneside1), 'b', markerfmt=" ", basefmt="-b")
plt.xlabel('Freq (Hz)')
plt.xlim(0, 60)
plt.tight_layout()

plt.show() 

        