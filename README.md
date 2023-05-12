# Noise generator

## Description
Creating a stationary mean free random process, where you can determine the sampling distribution and power spectral density (psd).

## Function
Creating white noise with desired sampling distribution. Then fitting the desired psd to the noise.

## Usage
```python
noise(n_samples, psd, distribution)
```

  **Parameters:** <br />
  
* n_samples:   number of sampels
* psd:         psd of noise with maximal frequency the nyquist frequency
  ```python 
  freq_s = np.fft.fftfreq(n_samples, 1 /f_s) 
  ```
* distribution: choose how to sample white noise ("uniform", "binominal", "gauss")


**Retruns:** <br />
* noise samples
                  
## Example


![gauss_1](images/gauss_1_f_real.png)

![gauss_2](images/gauss_1_f.png)

![binominal_1](images/binominal_1_f_real.png)


![binominal_1](images/binominal_1_f.png)
