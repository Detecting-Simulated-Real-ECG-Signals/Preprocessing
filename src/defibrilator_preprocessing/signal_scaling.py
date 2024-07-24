"""
Module used to scale time series signals.
"""

import numpy as np


def threshold_scale(
    data: np.ndarray, lower_threshold: float, upper_threshold: float
) -> np.ndarray:
    """
    Scale the signal using the thresholds into the range 0 to 1.
    """

    positive_data = data - lower_threshold
    return positive_data / (upper_threshold - lower_threshold)


def clip_signal(
    data: np.ndarray, lower_threshold: float = 0, upper_threshold: float = 1
) -> np.ndarray:
    """
    Clip the signals at the defined threshold.
    """
    return np.clip(data, lower_threshold, upper_threshold)
