#!/usr/bin/env python
"""
Module contaning the functions to visualize the 
wines distribution using a subset data
"""

import sys
import datetime

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def create_plots(filename):
    """
    Create plots for the analysis
    Args:
    -----
    filename: str
        Path to the filename containing the wine data
   
    """
    wine = pd.read_csv(filename)

    # Calls the function that plots the distribution
    print(plot_distribution(wine))

    # Calls the function that plots the scatter plot
    print(plot_scatter(wine))


def plot_distribution(wine):
    num_bins = 20

    mu = 88 # mean of distribution
    sigma = 3 # standard deviation of distribution

    # Histogram of the data
    fig, ax =  plt.subplots(figsize = (10,8))
    n, bins, patches = plt.hist(wine['points'], num_bins, density=1, facecolor='blue', alpha=0.5)


    # Add a 'best fit' line
    y = ((1 / (np.sqrt(2 * np.pi) * sigma)) *
         np.exp(-0.5 * (1 / sigma * (bins - mu))**2))

    ax.plot(bins, y, '--')

    ax.set_title('Distribution of Wine scores:  $\mu=88$, $\sigma=3$')
    ax.set_ylabel('Probability density')
    ax.set_xlabel('Points');

    fname = f'figures/fig01_distribution-wine-scores.png'

    fig.savefig(fname, bbox_inches = 'tight')
    return (fname)


def plot_scatter(wine):

    fig, ax =  plt.subplots(figsize = (10,8))

    plt.scatter(wine['points'], wine['price'])
    ax.set_title('Scatter wine points vs price')
    ax.set_ylabel('Price USD')
    ax.set_xlabel('Points')

    fname = f'figures/fig02_scatter-points-vs-price.png'
    fig.savefig(fname, bbox_inches = 'tight')
    return (fname)


if __name__ == '__main__':
    # Filename is passed by the user 
    filename = sys.argv[1]
    
    create_plots(filename)
