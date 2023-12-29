# Noise generator

## Description
Creating a stationary mean free random process, where you can choose the inital sampling distribution and power spectral density (psd).

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
Here are two examples shown, where 1/f noise is generated.

**1. Example:** 

In the first example the 1/f noise is generated based on white gaussian noise (WGN). One realizaition of the noise is shown in the following graph. 

![gauss_1](images/gauss_1_f_real.png)

After that the desired power spectral density (psd) and the psd of the noise siganl are compared.

![gauss_2](images/gauss_1_f.png)

**2. Example:**

In the second example 1/f noise is generated based on a binominal distribution. The random variables are x<sub>1</sub> = 1 and x<sub>2</sub> = -1 with the same probability. The generated 1/f noise is shown in the following graph.

![binominal_1](images/binominal_1_f_real.png)

And finally both psd are compared.

![binominal_1](images/binominal_1_f.png)
