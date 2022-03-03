# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 15:28:34 2022

@author: arge12
"""
import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt

fs   = 44100
time = np.arange(0, 4, 1/fs)



#sound1=[]
#for i in range(0, 1*fs):
#    sound1.append(        np.sin(2 * np.pi * (300 + 200*i/(1*fs) * i/(1*fs))))

#sound2=[]                  
#for i in range(1*fs, 0, -1):
#    sound2.append( (-1) * np.sin(2 * np.pi * (300 + 200*i/(1*fs) * i/(1*fs))))

sound3=[]                  
for i in range(0, 3*fs):
    s2=np.sin(2*np.pi*200*i/(2*fs))
    s1=np.sin(2*np.pi*(100 + 300/(2*fs))*i/(2*fs))
    sound3.append(np.cos(2*np.pi*300*i/(fs)*0.02)*np.sin(2*np.pi*(300+100*i/(2*fs))*i/(2*fs))*0.5 + s2*0.3 + s1*0.2)


sound4=[]
#for i in range(0, 4*fs):
   # sound.append(np.sin(2*np.pi*1000*i))
  
    
#sound = np.concatenate((sound1,sound2,sound3))   #sesleri birleştirme.   

plt.plot(time[0:8000], sound3[0:8000])


sd.play(sound3,fs)  




#-----------------------------------------------------
#                    1
#f1  = 697
#f2  = 1336
#time = np.arange(0, 1, 1/fs)
#sound1 = np.sin(2*np.pi*f1*time)           # sinüs dalga
#sound2 = np.sign(np.sin(2*np.pi*f1*time))  # kara dalga
#sound3 = np.sin(2*np.pi*f2*time) 
#sound = 0.5*sound1 + 0.5*sound3
#plt.plot(time[0:200], sound[0:200])
#sd.play(sound,fs)

#-----------------------------------------------------

#                    2
#time = np.arange(0, 2, 1/fs)
#soundx = np.sin(2*np.pi*(697  + time/2 * 400) *time)
#soundy = np.sin(2*np.pi*(1097 - time/2 * 400) *time)

#sound = np.concatenate((soundx, soundy))   #sesi birleştirir

#len_of_sound  = len(time)
#len_of_sound2 = len(sound)


#plt.plot(time[0:6000], sound[0:6000])
#sd.play(sound,fs)
#-----------------------------------------------------





