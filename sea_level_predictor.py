import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Read data from CSV
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(12, 6))

    ax.scatter(
        df["Year"],
        df["CSIRO Adjusted Sea Level"]
    )

    # Calculate line of best fit using all data
    slope, intercept, r_value, p_value, std_err = linregress(
        df["Year"],
        df["CSIRO Adjusted Sea Level"]
    )

    # Create years from the first year through 2050
    years = pd.Series(
        range(df["Year"].min(), 2051)
    )

    # Calculate predicted sea level
    predicted_sea_level = slope * years + intercept

    # Plot first line of best fit
    ax.plot(
        years,
        predicted_sea_level
    )

    # Filter data from 2000 onward
    df_recent = df[df["Year"] >= 2000]

    # Calculate second line of best fit
    slope_recent, intercept_recent, r_value_recent, p_value_recent, std_err_recent = linregress(
        df_recent["Year"],
        df_recent["CSIRO Adjusted Sea Level"]
    )

    # Create years from 2000 through 2050
    years_recent = pd.Series(
        range(2000, 2051)
    )

    # Calculate predicted sea level
    predicted_recent = (
        slope_recent * years_recent +
        intercept_recent
    )

    # Plot second line of best fit
    ax.plot(
        years_recent,
        predicted_recent
    )

    # Labels and title
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    ax.set_title("Rise in Sea Level")

    # Save and return figure
    fig.savefig("sea_level_plot.png")

    return ax