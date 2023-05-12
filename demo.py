'''
Topic:          Demonstration: Noise
Description:    Demonstrating how to create noise
Autor:          Leon Schmidt
E-Mail:         leonjohannesschmidt@gmail.com
'''

import numpy as np
import matplotlib.pyplot as plt
from noise import *

'''
1/f - noise from gauss distribution, sampling frequency = 1 Hz,  
number of samples 500
'''
#Creating of the psd
n_samples = int(500)
freq = np.fft.fftfreq(n_samples)
freq[0] = 1

psd = 1 / freq
psd[0] = 0 
freq[0] = 0

#Creating the noise
samples_noise = noise(n_samples, psd, "gauss")

#Visualizing the psd
samples_noise_fourier = np.fft.fft(samples_noise)
samples_noise_fourier = samples_noise_fourier.reshape(samples_noise_fourier.size, )
samples_noise_fourier_abs = np.absolute(samples_noise_fourier)

psd_abs = np.absolute(psd)

plt.plot(freq, np.square(samples_noise_fourier_abs), freq, psd_abs)
plt.xlabel("Frequency [Hz]")
plt.ylabel("Power")
plt.title("Power spectral density")
plt.legend(['$PSD_{noise}$', '$PSD_{given}$'])
plt.show()

#Visualizing the noise
t = np.arange(n_samples)

plt.plot(t, samples_noise)
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.title("Noise realization")
plt.show()


'''
1/f - noise from binominal distribution, sampling frequency = 1 Hz,
number of samples 500
'''
#Creating of the psd
n_samples = int(500)
freq = np.fft.fftfreq(n_samples)
freq[0] = 1

psd = 1 / freq
psd[0] = 0 
freq[0] = 0

#Creating the noise
samples_noise = noise(n_samples, psd, "binominal")

#Visualizing the psd
samples_noise_fourier = np.fft.fft(samples_noise)
samples_noise_fourier = samples_noise_fourier.reshape(samples_noise_fourier.size, )
samples_noise_fourier_abs = np.absolute(samples_noise_fourier)

psd_abs = np.absolute(psd)

plt.plot(freq, np.square(samples_noise_fourier_abs), freq, psd_abs)
plt.xlabel("Frequency [Hz]")
plt.ylabel("Power")
plt.title("Power spectral density")
plt.legend(['$PSD_{noise}$', '$PSD_{given}$'])
plt.show()

#Visualizing the noise
t = np.arange(n_samples)

plt.plot(t, samples_noise)
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.title("Noise realization")
plt.show()


'''
specific noise from gauss distribution, sampling frequency = 1 Hz, 
number of samples 500
'''
#Creating of the psd
n_samples = int(500)
psd = np.zeros(n_samples)
freq = np.fft.fftfreq(n_samples)
psd = 500 - np.abs(1000 * freq)
psd[0] = 0 

#Creating the noise
samples_noise = noise(n_samples, psd, "gauss")

#Visualizing the psd
samples_noise_fourier = np.fft.fft(samples_noise)
samples_noise_fourier = samples_noise_fourier.reshape(samples_noise_fourier.size, )
samples_noise_fourier_abs = np.absolute(samples_noise_fourier)

psd_abs = np.absolute(psd)

plt.plot(freq, np.square(samples_noise_fourier_abs), freq, psd_abs)
plt.xlabel("Frequency [Hz]")
plt.ylabel("Power")
plt.title("Power spectral density")
plt.legend(['$PSD_{noise}$', '$PSD_{given}$'])
plt.show()

#Visualizing the noise
t = np.arange(n_samples)

plt.plot(t, samples_noise)
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.title("Noise realization")
plt.show()


'''
specific noise from uniform disribution, sampling frequency = 1 Hz,
number of samples 500
'''
#Creating of the psd
n_samples = int(500)
psd = np.zeros(n_samples)
freq = np.fft.fftfreq(n_samples)
psd = 500 - np.abs(1000 * freq)
psd[0] = 0 

#Creating the noise
samples_noise = noise(n_samples, psd, "uniform")

#Visualizing the psd
samples_noise_fourier = np.fft.fft(samples_noise)
samples_noise_fourier = samples_noise_fourier.reshape(samples_noise_fourier.size, )
samples_noise_fourier_abs = np.absolute(samples_noise_fourier)

psd_abs = np.absolute(psd)

plt.plot(freq, np.square(samples_noise_fourier_abs), freq, psd_abs)
plt.xlabel("Frequency [Hz]")
plt.ylabel("Power")
plt.title("Power spectral density")
plt.legend(['$PSD_{noise}$', '$PSD_{given}$'])
plt.show()

#Visualizing the noise
t = np.arange(n_samples)

plt.plot(t, samples_noise)
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.title("Noise realization")
plt.show()