import librosa, librosa.display
import matplotlib.pyplot as plt
import numpy as np

file_path = "cello.wav"

signal , sr = librosa.load(file_path, sr = 22050, mono = True, offset=0.0, duration=None)

librosa.display.waveplot(signal, sr = sr)
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.show()


fft = np.fft.fft(signal)

samplerate = sr 

magnitude = np.abs(fft)   # imajinerden kurtul
frequency = np.linspace(0, samplerate, len(magnitude))

left_freq = frequency[:int(len(frequency)/2)]
right_freq =magnitude[:int(len(frequency)/2)]


plt.plot(left_freq, right_freq)
plt.xlabel("frequency")
plt.ylabel("Magnitude")
plt.show()


#stft  spectogram
n_fft = 2048            #number of samples fft 
hop_length = 512       

stft = librosa.core.stft(signal, hop_length=hop_length, n_fft=n_fft)

spectrogram = np.abs(stft)

librosa.display.specshow(spectrogram, sr = sr, hop_length=hop_length)
plt.plot(left_freq, right_freq)
plt.xlabel("Time")
plt.ylabel("frequency")
plt.colorbar()
plt.show()

