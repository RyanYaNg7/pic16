#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 23:33:34 2018

@author: Ryan
"""
import matplotlib.pyplot as plt
import numpy as np
from scipy import fftpack as spft
from scipy.io import wavfile as spwav

rate, data = spwav.read('/Users/Ryan/Desktop/Assignment 7F/wooguy.wav')

t = np.linspace(0, len(data)/float(rate), len(data))
plt.plot(t[0:100],data[0:100])
plt.show()

FFT1 = spft.fft(data[:,0])
FFT2 = spft.fft(data[:,1])

power1 = abs(FFT1)
power2 = abs(FFT2)

plt.plot(power1)
plt.plot(power2)
plt.show()

N = len(power1)
d = 1./rate
spfre = spft.fftfreq(N,d)
plt.plot(spfre, power1)
plt.plot(spfre, power2)
plt.show()

plt.plot(spfre[0:50000], power1[0:50000])
plt.plot(spfre[0:50000], power2[0:50000])
plt.show()


# =============================================================================
# FFT1[int(550*N*d + N/2):int(640*N*d + N/2)] = 0
# FFT2[int(550*N*d + N/2):int(640*N*d + N/2)] = 0
# =============================================================================

FFT1[-int(640*N*d):-int(530*N*d)] = 0
FFT2[-int(640*N*d):-int(530*N*d)] = 0

FFT1[int(530*N*d):int(640*N*d)] = 0
FFT2[int(530*N*d):int(640*N*d)] = 0

power11 = abs(FFT1)
power22 = abs(FFT2)

plt.plot(spfre, power11)
plt.plot(spfre, power22)
plt.show()

plt.plot(spfre[0:15000], power11[0:15000])
plt.plot(spfre[0:15000], power22[0:15000])
plt.show()

plt.plot(spfre[-15000:-1], power11[-15000:-1])
plt.plot(spfre[-15000:-1], power22[-15000:-1])
plt.show()

# =============================================================================
# plt.plot(spfre[N//2:15000+N//2], power11[N//2:15000+N//2])
# plt.plot(spfre[N//2:15000+N//2], power22[N//2:15000+N//2])
# plt.show()
# =============================================================================



cleaned1 = spft.ifft(FFT1)
cleaned2 = spft.ifft(FFT2)

cleaned1 = np.array(cleaned1, dtype = 'int16')
cleaned2 = np.array(cleaned2, dtype = 'int16')

result = np.hstack((cleaned1[:, np.newaxis], cleaned2[:, np.newaxis]))

t = np.linspace(0, len(result)/float(rate), len(result))
plt.plot(t[0:100],result[0:100])
plt.show()

spwav.write('nowooguy.wav', rate, result)