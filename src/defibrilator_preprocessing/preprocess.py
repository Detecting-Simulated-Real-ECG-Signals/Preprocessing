"""
Created by Anton Roth 
Adapted by Markus Brücklmayr
"""

import numpy as np

from .data_cleaning import (
    butterworth_filtering,
    polynomial_remove_offset_and_baseline_wandering,
    remove_mains_noise,
)


def preprocess_sample(
    raw_signal: np.ndarray, samplerate: int, preprocess_params
) -> np.ndarray:
    raw_signal -= raw_signal.mean()
    if "BASELINE_FILTER" in preprocess_params.ACTIVE_FILTER:
        offset_removed_ecg = polynomial_remove_offset_and_baseline_wandering(
            raw_signal, samplerate=samplerate
        )
    else:
        offset_removed_ecg = raw_signal

    QUALITY_FACTOR = preprocess_params.QUALITY_FACTOR
    REMOVE_FREQUENCIES = preprocess_params.REMOVE_FREQUENCIES

    if "NOTCH_FILTER" in preprocess_params.ACTIVE_FILTER:
        noise_removed_data = remove_mains_noise(
            offset_removed_ecg, samplerate, QUALITY_FACTOR, REMOVE_FREQUENCIES
        )
    else:
        noise_removed_data = offset_removed_ecg

    if "BANDPASS_FILTER" in preprocess_params.ACTIVE_FILTER:
        butterworth_filtered_data = butterworth_filtering(
            noise_removed_data,
            preprocess_params.LOWPASS_FILTER_CUT_OFF_FREQUENCY,
            preprocess_params.HIGHPASS_FILTER_CUT_OFF_FREQUENCY,
            preprocess_params.FILTER_ORDER,
            samplerate,
        )
    else:
        butterworth_filtered_data = noise_removed_data

    return butterworth_filtered_data
