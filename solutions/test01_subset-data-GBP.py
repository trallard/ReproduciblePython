#!/usr/bin/env python

import sys
import datetime

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def process_data_GBP(filename):
    """
    Get only the needed subset from the data.
    Args:
    filename: str
        Path to the filename containing the wine data

    Returns:

    data_path: st
        Path to the created data set
    """

    # Load table
    try:
        wine = pd.read_csv(filename)
    except IOError:
        print('That file does not seem to exist')

    # Subset of data to keep
    wine_keep = wine.loc[:,['country', 'designation', 'points', 'price']]

    # Add column with prices in GBP
    wine_keep['price_GBP'] = wine_keep['price'].apply(lambda x : x * 1.2)

    # Constructing the fname
    today = datetime.datetime.today().strftime('%Y-%m-%d')
    fname = f'data/interim/{today}-winemag_priceGBP.csv'

    # Saving the csv
    wine_keep.to_csv(fname)

    return(fname)


if __name__ == '__main__':
    filename = sys.argv[1]
    print(filename)
    print(process_data_GBP(filename))
