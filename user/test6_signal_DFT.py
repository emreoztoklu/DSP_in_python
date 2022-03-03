import matplotlib.pyplot as plt
import numpy as np

def DFT(signal):
    ''' 
    This function calculate the discrete fourier Transform of a 1D real-valued
    signal (parameter) 
    '''
    N = len(signal)
    n = np.arange(N)
    k = n.reshape((N, 1))       #reshape 1 tek colonlu sutun index'e dönüştürür
    e = np.exp( -2j*np.pi*k*n/ N)
    
    dft_signal = np.dot(e, signal)  #euler açısı hesabı. e^signal
    
    return dft_signal
#------------------------------------------------------------------------------ 



sr = 8          #sampling rate
ts = 1.0/sr     #sampling İnterval
t  = np.arange(0, 1, ts)

freq = 1.
signal = [1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4]   
# 16 adet sampling rate değeri 
# 16 adet de 4Hz, 8 adet de 2Hz, 4 adet de 1 hz, 2 adet 0.5Hz  
 


#------------------------------------------------------------------------------ 
DFT_solution = DFT(signal)

#frequence Calculation of Signal
N = len(DFT_solution)
n = np.arange(N)
T = N/sr          #period
freq = n/T        #frequency of signal


n_oneside = N//2   # positif yükselen kenarın analizi için Tam sinyalin yarısı

#get the one side of frequency
f_oneside = freq[:n_oneside]

#normalize the amplitude
DFT_signal_oneside = DFT_solution[:n_oneside]/n_oneside
#------------------------------------------------------------------------------ 



plt.figure(figsize=(12,6))
plt.stem(f_oneside, abs(DFT_signal_oneside), 'b', markerfmt=' ', basefmt='-b')
plt.xlabel('Freq (Hz)')
plt.ylabel('DFT Amplitude |DFT_signal_oneside(freq/2)|')
plt.show()