'''
DFT analizi klasik tanımı 
(district Fourier Translatıon) ( Ayrık Fourier Dönüşümü)
https://web.itu.edu.tr/~baykut/lab/pdf/Deney_3.pdf

'''
import matplotlib.pyplot as plt
import numpy as np

#sampling rate   // 100 adet örnek noktası 
sr = 300         # burayı oynayarak ayrık sinyali aç-kapa

#sampling interval
ts = 1.0/sr
t  = np.arange(0, 1, ts)



#Theta Açısı(O) --> O= W * t    (Theta açısının Hızı W)  (t ise zaman )
#W=2pif  Açısal Hız             (W=metre/saniye)
def radialvelocity(freqq):
    return 2*np.pi*freqq


#----------------------------------------------

frequency = 10             # 1hz
W = radialvelocity(frequency)    

signal = 3*np.sin( W * t)

#----------------------------------------------

frequency = 4             # 3hz
W = radialvelocity(frequency)     

signal += 2*np.sin( W * t)

#----------------------------------------------

frequency = 7             # 5hz
W = radialvelocity(frequency)

signal += 1.5*np.sin( W * t)
#----------------------------------------------

plt.figure(figsize = (8,6))
plt.plot(t, signal, 'r--')
plt.plot(t, signal, 'g.')
plt.ylabel('Amplitude')

plt.show()

#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------ 

def DFT(signal):
    ''' 
    This function calculate the discrete fourier Transform of a 1D real-valued
    signal (parameter) 
    '''
    N = len(signal)
    n = np.arange(N)
    k = n.reshape((N, 1))       #reshape 1 tek colonlu sutun index'e dönüştürür
    e = np.exp( -2j * np.pi * k * n / N)
    
    dft_signal = np.dot(e, signal)  #euler açısı hesabı. e^signal
    
    return dft_signal

#------------------------------------------------------------------------------ 

DFT_solution = DFT(signal)

#frequence Calculation of Signal
N = len(DFT_solution)
n = np.arange(N)
T = N/sr          #period
freq = n/T        #frequency of signal


plt.figure(figsize=(8,6))
plt.stem(freq, abs(DFT_solution), 'b', markerfmt=' ', basefmt='-b')
plt.xlabel('Freq (Hz)')
plt.ylabel('DFT Amplitude |DFT_solution(freq)|')
plt.show()




