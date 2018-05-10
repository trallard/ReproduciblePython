#!/usr/bin/env python

import sys
import datetime

import pandas as pd


def get_country(filename, country):
    """
    Do a simple analysis per country
    Args:
    -----
    filename: str
        Path to the filename containing the wine data
    country: str
        Country to be used to subset

    Returns:
    -----
    data_path: dataframe
        Dataframe containing the subset of the data
    """

    # Load table
    wine = pd.read_csv(filename)

    # Use the country name to subset data
    subset_country = wine[wine['country'] == country ].copy()
    
    # important for testing!!!!
    subset_country.reset_index(drop=True, inplace=True)

    # Constructing the fname
    today = datetime.datetime.today().strftime('%Y-%m-%d')
    fname = f'data/processed/{today}-winemag_{country}.csv'

    # Saving the csv
    # also note the addition of the index = False!!!
    subset_country.to_csv(fname, index=False)
    print(fname)  # print the fname from here

    return(subset_country)  #returns the data frame

def get_mean_price(filename):
    """Compute the mean price of wines
    Args:
    -----
    filename: str
        Path to the filename containing the wine data
    
    Returns:
    -----
    mean_price: float
        Mean price computed from the subset data
    
    """
    wine = pd.read_csv(filename)
    mean_price = wine['price'].mean()
    return round(mean_price, 4)

if __name__ == '__main__':
    # by using sys.arg the user can provide input from
    # the command line
    filename = sys.argv[1]
    country = sys.argv[2]
    
    # adding some prints to get feedback in the command
    # line
    print(f'Subsetting: {filename}')
    print(f'Country searched: {country}')

    print(get_country(filename, country))
