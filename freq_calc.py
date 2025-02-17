import numpy as np
import scipy.signal as signal
import pandas as pd

def fft(x):
    N = len(x)
    if N <= 1: return x
    elif N % 2 == 1:         # N is odd, lemma does not apply
        print ('N is ' + str(N) + ', fall back to discrete transform')
        return discrete_transform(x)
    even = fft(x[0::2])
    odd =  fft(x[1::2])
    return np.array( [even[k] + np.exp(-2j*np.pi*k/N)*odd[k] for k in range(N//2)] + \
                     [even[k] - np.exp(-2j*np.pi*k/N)*odd[k] for k in range(N//2)] )

def discrete_transform(data):
    """Return Discrete Fourier Transform (DFT) of a complex data vector"""
    N = len(data)
    transform = np.zeros(N)
    for k in range(N):
        for j in range(N):
            angle = 2 * np.pi * k * j / N
            transform[k] += data[j] * np.exp(1j * angle)
    return transform

def find_peak_frequency(X):
    Y = fft(X)
    # Get the length of the signal
    N = len(Y)
    # Divide by two to get the positive half of the FFT
    half = N // 2
    # Get the absolute value of the FFT
    abs_Y = np.abs(Y[:half])
    # Find the indices of the local maxima of the FFT
    peak_indices = signal.argrelextrema(abs_Y, np.greater)[0]
    # Count the number of peaks
    number_of_peaks = len(peak_indices)
    return number_of_peaks
