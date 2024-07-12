# Preprocessing of ECG signals

Package to preprocess ECG signals. Adapted from [corpuls](https://corpuls.world/) preprocessing methodology.

## Build package

This package is not yet available via a pip repository server. Therefor you have to clone this repository and build it yourself.

To build the repository you can use the pip package 'build'
```console
pip install build
```
and build the package with `python -m build`. The results of the build process are within the folder /dist. You can install this local package with pip:
```console
pip install /path/to/repository/dist/defibrillator_preprocessing-X.X.X-py3-none-any.whl
```

## Use it

data_cleaning contains methods to remove baseline wandering by a simple highpass filter (`def butterworth_filtering`), baseline and offset wandering by a polynomial fitter manner (`def polynomial_remove_offset_and_baseline_wandering`) and a method to remove mains noise (`def remove_mains_noise`)

preprocessing combines the data_cleaning methods into a single function. You have to define which filters and filter parameters you want to use. 

signal_scaling can be used to scale the mission recordings by percentile, max and threshold. 
