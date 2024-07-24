"""
Code inspired by Anton Roth 
"""

from typing import Sequence

import numpy as np
from scipy import signal
from scipy.optimize import curve_fit


def butterworth_filtering(
    ecg_signal: np.ndarray,
    low_cut_off_Hz: float,
    high_cut_off_Hz: float,
    order: int,
    samplerate: float,
) -> np.ndarray:
    """
    Filter out baseline wandering and high pass noise by a simple high pass filter combined with a low pass filter (Butterworth filter).
    """
    # Design HP Butterworth-Filter
    nyq = samplerate / 2

    highpass_cut_off = high_cut_off_Hz / nyq
    lowpass_cut_off = low_cut_off_Hz / nyq

    # NOTE: See https://scipy-cookbook.readthedocs.io/items/ButterworthBandpass.html how to implement this kind of filter
    # Design bandpass butterworth filter
    b, a = signal.butter(
        order, [highpass_cut_off, lowpass_cut_off], btype="band", analog=False
    )

    # Execute bandpass butterwoth filter
    hp_filtered_signal = []
    for offset_removed_signal in ecg_signal:
        hp_filtered_signal.append(
            signal.filtfilt(b, a, offset_removed_signal, method="gust", axis=0)
        )

    return np.array(hp_filtered_signal)


def polynomial_remove_offset_and_baseline_wandering(
    raw_data: np.array, samplerate: float
) -> np.array:
    """
    Method that removes offset and baseline wandering in a polynomial fitting manner

    The fit function that should fit for our given samples (`fit function`).
    The coefficients (c, c0...) are determine by a least squares optimizing function to
    fit the function best through the given samples.
    At the last step, the y values of the fitting curve are determined.

    See: https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.curve_fit.html as example where `fit_function`
    is `func`, `x_data` ar our `x_values` and `ydata` is our lead wise ecg signal
    For the plot showed in the docs they apply x_data to the funct and get the values of y for the plot
    """
    # Determine x-Values from number of samples and samplerate of the sample
    time = len(raw_data) / samplerate
    x_values = np.linspace(0, time, len(raw_data))

    # General equation of the function to be used as a baseline
    def fit_function(x, c0, c1, c):
        return c0 * x + c1 * x**2 + c

    calculated_baseline = []
    # Calculate baseline
    # Optimize in `fit_function` defined equation with least squares to fit best for the given samples
    coefficents, _ = curve_fit(fit_function, x_values, raw_data)
    # Calculate y values of baseline by inserting the coefficients determined by curve fitting to the defined equation
    calculated_baseline.append(
        [fit_function(x_value, *coefficents) for x_value in x_values]
    )

    return raw_data - calculated_baseline


def remove_mains_noise(
    ecg_signal: np.ndarray,
    original_sample_rate: int,
    QUALITY_FACTOR: float,
    REMOVE_FREQUENCIES: Sequence,
) -> np.array:
    """
    Method that removes frequencies defined in `params.py` with a notch filter
    """
    nyq = original_sample_rate / 2
    for frequency in REMOVE_FREQUENCIES:
        w0 = frequency / nyq
        numerator, denumerator = signal.iirnotch(w0, QUALITY_FACTOR)
        ecg_signal = signal.filtfilt(numerator, denumerator, ecg_signal)

    return ecg_signal
