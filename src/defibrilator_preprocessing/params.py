from typing import List


class FilterProcess:
    # Possible filters:
    # "BASELINE_FILTER": removes a very low frequency trend from the signal
    # "NOTCH_FITLER": removes power line frequencies (defined in REMOVE_FREQUENCIES). Narrowband filter
    # "BANDPASS_FILTER": frequencies outside of the defined bandpass. Uses
    #                    HIGHPASS_FILTER_CUT_OFF_FREQUENCY and LOWPASS_FILTER_CUT_OFF_FREQUENCY
    ACTIVE_FILTER: List[str] = (
        []
    )  # ["BASELINE_FILTER", "BANDPASS_FILTER", "NOTCH_FITLER"]

    SAMPLE_RATE = 300
    DURATION = 10

    # For butterworth filter use:
    FILTER_ORDER = 2

    # Cut off frequencys in Hz
    HIGHPASS_FILTER_CUT_OFF_FREQUENCY = 0.05
    LOWPASS_FILTER_CUT_OFF_FREQUENCY = 120

    # For notch filter use:
    QUALITY_FACTOR = 30.0

    # Frequency to be removed from signal (Hz)
    REMOVE_FREQUENCIES = [50, 60, 100, 120]

    # For scaling parameters calculation
    SAMPLE_PERCENTAGE_FOR_PERCENTILE_SCALING = 0.1
    LOWER_PERCENTILE = 2
    UPPER_PERCENTILE = 98
