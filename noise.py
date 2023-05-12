'''
Topic:          Noise samples
Description:    Creating a stationary mean free random process, where you can determine
                the sampling distribution and power spectral density (psd)
Function:       Creating white noise with sampling distribution, fitting the 
                desired psd to the noise
Autor:          Leon Schmidt
E-Mail:         leonjohannesschmidt@gmail.com
'''

import numpy as np

'''
n_samples       --> number of sampels 
psd             --> psd of noise with maximal frequency the nyquist frequency
                --> sampled frequencies: freq = np.fft.fftfreq(n_samples, 1 /f_s)
                    f_s -> samling frequency
distribution    --> choose how to sample white noise
                --> possible "uniform" distribution (0 till 1), 
                    "binominial" distribution (x_1 = 1, x_2 = -1),
                    "gauss" distribution, default "gauss" distribution                
'''

def noise(n_samples, psd, distribution):
    #creating of white noise
    match distribution:
        case "uniform":
            noise_white = np.random.uniform(0, 1, n_samples)

        case "binominal":
            noise_white = np.random.randint(0, 2, n_samples) *2 -1

        case _:
            mean = 0
            std_dev = 1
            noise_white = np.random.normal(mean, std_dev, n_samples)

    #fitting of the psd
    noise_white_fourier = np.fft.fft(noise_white)
    noise_white_fourier = noise_white_fourier.reshape(noise_white_fourier.size, )

    psd_abs = np.absolute(psd)
    noise_x_fourier = noise_white_fourier * np.sqrt(psd_abs)
    noise_x_fourier[0] = 0

    #normalizing the energy
    noise_x_fourier_abs = np.absolute(noise_x_fourier)
    factor = np.sqrt(np.sum(psd_abs) / np.sum(np.square(noise_x_fourier_abs)))

    noise_x_fourier = noise_x_fourier * factor

    #calculating the time series
    noise_x = np.fft.ifft(noise_x_fourier)
    noise_x = np.real(noise_x)

    return noise_x
