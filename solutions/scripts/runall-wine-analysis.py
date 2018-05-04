#!/usr/bin/env python

"""
Script to create all the results from our
amazing wine study
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import importlib

# imports from our package
# Since we have digits at the start of the modules we
# will use dynamic imports
subset = importlib.import_module('.data.01_subset-data-GBP', 'scripts')
plotwines = importlib.import_module('.visualization.02_visualize-wines', 'scripts')
country_sub = importlib.import_module('.data.03_country-subset', 'scripts')

# ------------------------------------------------------------------------
# Declare variables
# ------------------------------------------------------------------------

# Set raw data path
raw_data = "data/raw/winemag-data-130k-v2.csv"

# Set country
country = "Chile"

# ------------------------------------------------------------------------
# Perform analysis
# ------------------------------------------------------------------------

if __name__ == '__main__':
    subset_file = subset.process_data_GBP(raw_data)
    print(subset_file)
    plotwines.create_plots(interim_data)
    country_file = country_sub.get_country(subset_file, country)
    print(country_file)