import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    df.plot(kind='scatter', x='Year', y='CSIRO Adjusted Sea Level', figsize=(12,12))

    # Create first line of best fit
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']
    best_fit_first = linregress(x, y)
    years_first = pd.DataFrame({'col1': [i for i in range(1880,2051)]})

    plt.plot(years_first, best_fit_first.intercept + best_fit_first.slope*years_first, 'r', label='first line')

    # Create second line of best fit
    x = df['Year'][df['Year'] > 1999]
    y = df['CSIRO Adjusted Sea Level'][df['Year'] > 1999]
    best_fit_second = linregress(x,y)
    years_second = pd.DataFrame({'col1': [i for i in range(2000, 2051)]})

    plt.plot(years_second, best_fit_second.intercept + best_fit_second.slope*years_second, 'b', label='second line')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title("Rise in Sea Level")

    plt.legend()

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()