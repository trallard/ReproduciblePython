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
subset = importlib.import_module('.data.01_subset-data-GBP', 'src')
plotwines = importlib.import_module('.visualization.02_visualize-wines', 'src')
country_sub = importlib.import_module('.data.03_country-subset', 'src')

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
    # create the subset of the initial dataframe
    subset_file = subset.process_data_GBP(raw_data)
    # prints out the name of the new file created
    print(subset_file)
    # generate the plots
    plotwines.create_plots(subset_file)
    # subset the data for the country given 
    country_file = country_sub.get_country(subset_file, country)
    print(country_file)
    
    
