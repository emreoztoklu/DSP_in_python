'''
DFT analizi klasik tanımı 
(district Fourier Translatıon) ( Ayrık Fourier Dönüşümü)
https://web.itu.edu.tr/~baykut/lab/pdf/Deney_3.pdf

'''
import matplotlib.plot as plt
import numpy as np

#sampling rate   // 100 adet örenek noktası 
sr = 100  

#sampling interval
ts = 1.0/sr
t  = np.arange(0, 1,)