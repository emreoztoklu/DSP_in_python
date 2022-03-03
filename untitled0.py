import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt
import soundfile as sf

fs = 44100
sn = 2
time = np.arange(0,sn,1/fs)
rate = 20.0

def sound_lenght(second=0):
    x=int(44100*second)
    return x

def DFT(x): # To calculate DFT of a 1D real-valued signal x
    
    N = len(x)
    n = np.arange(N)
    k = n.reshape((N, 1))
    e = np.exp(-2j * np.pi * k * n / N)
    X = np.dot(e, x)
    return X

amp=[0,1,0.1,0.01,0.001,0.0001]
freq=[2544,5087,7632,10176,12719,15264]

sound1=[]
for i in range (0,sound_lenght(0.4)):
    sound1.append((amp[2]   *np.sin( 2*np.pi*(freq[0])*  i/fs))
                 +(amp[4]   *np.sin( 2*np.pi*(freq[1])*  i/fs))
                 +(amp[3]   *np.sin( 2*np.pi*(freq[2])*  i/fs))
                 +(amp[3]   *np.sin( 2*np.pi*(freq[3])*  i/fs))
                 +(amp[3]   *np.sin( 2*np.pi*(freq[4])*  i/fs))
                 +(amp[4]   *np.sin( 2*np.pi*(freq[5])*  i/fs)))
     
sound2=[]
for i in range (0,sound_lenght(0.2)):     
    sound2.append(0)

sound3=[]
for i in range (0,sound_lenght(1)):
    sound3.append((amp[1]   *np.sin( 2*np.pi*(50*i/(1*fs))*  i/fs)))
    
sound4=[]
for i in range (0,sound_lenght(1)):
    sound4.append((amp[1]  *np.sin( 2*np.pi*(1000)*  i/fs)))
   
sound=np.concatenate((sound2,sound1,sound2))    
sound5=np.concatenate((sound3,sound4))
#p = 10*np.log10(np.abs(np.fft.rfft(sound)))
#f = np.linspace(0, rate/2, len(p))
#plt.plot(f, p)
    
#sound2=[]
#for i in range (1*fs,0,-1):
#   sound2.append(-1*np.sin(2*np.pi*(300+200*i/(1*fs))*i/(1*fs)))
   
#sound3=[]
#for i in range (0,1*fs):
#    sound1.append(np.cos(2*np.pi*300*i/fs*0.01)*np.sin(2*np.pi*(600+200*i/(1*fs))))
    
#sound=np.concatenate((sound1,sound2,sound3))

#sound5=np.fft.fft(sound)

#plt.plot(time[44000:44200],sound5[44000:44200])

sd.play(sound1, 44100)
sf.write("reverse2.wav",sound,fs)
sf.write("reverse3.wav",sound5,fs)

X = DFT(sound1[0:4096])

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
plt.subplot(121)
plt.stem(f_oneside, abs(X_oneside), 'b', \
         markerfmt=" ", basefmt="-b")
plt.xlabel('Freq (Hz)')
plt.ylabel('DFT Amplitude |X(freq)|')

plt.subplot(122)
plt.stem(f_oneside, abs(X_oneside), 'b', \
         markerfmt=" ", basefmt="-b")
plt.xlabel('Freq (Hz)')
plt.xlim(0, 5000)
plt.tight_layout()
plt.show()

