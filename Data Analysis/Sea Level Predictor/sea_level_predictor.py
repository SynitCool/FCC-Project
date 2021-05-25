import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    fig, ax = plt.subplots()
    fig.set_figheight(6)
    fig.set_figwidth(11)

    ax.scatter(df["Year"], df["CSIRO Adjusted Sea Level"])

    # Create first line of best fit
    regression_line1 = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])

    ax.plot(np.arange(1880, 2050), regression_line1.intercept + regression_line1.slope * np.arange(1880, 2050), c='r')
    # Create second line of best fit
    regression_line2 = linregress(df[df["Year"] >= 2000]["Year"], df[df["Year"] >= 2000]["CSIRO Adjusted Sea Level"])

    ax.plot(np.arange(2000, 2050), regression_line2.intercept + regression_line2.slope * np.arange(2000, 2050), c='g')
    # Add labels and title
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    ax.set_title("Rise in Sea Level")
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()