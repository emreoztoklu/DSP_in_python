import librosa, librosa.display
import matplotlib.pyplot as plt

file_path = "cello.wav"

signal, sr = librosa.load(file_path, sr = 22050)
librosa.display.waveplot(signal, sr = sr)
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.show()

