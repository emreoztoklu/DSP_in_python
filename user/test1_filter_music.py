# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 16:41:37 2022

@author: arge12
"""

import numpy as np
from scipy.io.wavfile import read 
from scipy.io.wavfile import write
import matplotlib.pyplot as plt



def filter_lowpass(sig_input): 
    A = float()
    B = float()

    E = sig_input + 1.1429 * A - 0.4127 * B
    sig_output = 0.0670 * E + 0.1350 * A + 0.0670 * B
    
    B = A
    A = E
    
    return sig_output


path = read("Africa.wav")


raw_wav_datas   = np.array((path[1]), dtype=float)
Sampling_Rate   = path[0]
Frames_count    = np.size(raw_wav_datas)

wav_datas       = np.array(filter_lowpass(path[1]), dtype=int)



write("em.wav", Sampling_Rate, wav_datas)


