import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt
import soundfile as sf

Ampl=[0, 1, 0.1, 0.01, 0.001, 0.0001]

#sampling interval
fs = 4096        #freq
ts = 1.0/fs         #period
time = np.arange(0, 1, ts)

S1_Amp      = 1
S1_freq     = 100
S1_sig_len  = 1

#---------------------------------------------------------------
def DFT(src_signal): # To calculate DFT of a 1D real-valued signal x 
    N = len(src_signal)
    n = np.arange(N)
    k = n.reshape((N, 1))
    e = np.exp(-2j * np.pi * k * n / N)
    X = np.dot(e, src_signal)
    return X

def low_passfilter(src_sound_arr, sample_number):
    fltsound=[]
    A=0
    B=0
    for i in range (0, sample_number):
        X = src_sound_arr[i]
        E = X + 1.1429 * A - 0.4127 * B
        Y = 0.067 * E + 0.135 * A + 0.067 * B
        fltsound.append(Y)
        B = A
        A = E
    return  fltsound 


def signal_lenght(sample_freq, second):
    return int(sample_freq * second)


#---------------------------------------------------------------

sound=[]

for i in range (0, signal_lenght(fs, S1_sig_len)):
    samp1=  S1_Amp * np.sin(2 * np.pi * (S1_freq) * i/fs)
    samp2=  S1_Amp * np.cos(2 * np.pi * (S1_freq) * i/fs * 0.05)
    noise= 0.25*(np.random.rand()-0.5)
    sound.append ( samp1 * samp2)
    
sd.play(sound, fs)
sf.write('sound.wav', sound, fs)
#---------------------------------------------------------------

X = DFT(sound)

fsound2 = low_passfilter(sound, len(sound))
fsound3 = low_passfilter(fsound2, len(fsound2))

X1 = DFT(fsound3)

#---------------------------------------------------------------
# calculate the frequency

N = len(X)
n = np.arange(N)
T = N/fs
freq = n/T 

n_oneside = N//2

# get the one side frequencies
f_oneside  = freq [:n_oneside]

# normalize the amplitude
X_oneside  =  X[:n_oneside]/n_oneside
X1_oneside = X1[:n_oneside]/n_oneside

fig, axs = plt.subplots(3,2)
axs[0, 0].plot(time[0:512],sound[0:512])
axs[0, 0].set_title('İnput Signal')


axs[0, 1].plot(time[0:200],fsound3[0:200])
axs[0, 1].set_title('Output_Filtered Signal')

axs[1, 0].stem(f_oneside,  abs(X_oneside), 'b', markerfmt=" ", basefmt="-b")
axs[1, 0].set_title('DFT Amplitude |X(freq)|')


axs[2, 0].stem(f_oneside, abs(X_oneside), 'b', markerfmt=" ", basefmt="-b")
axs[2, 0].set_title('DFT Amplitude |X(freq)|')


axs[1, 1].stem(f_oneside,  abs(X1_oneside), 'b', markerfmt=" ", basefmt="-b")

plt.xlim(0, 60)
plt.tight_layout()

axs[2, 1].stem(f_oneside, abs(X1_oneside), 'b', markerfmt=" ", basefmt="-b")

        