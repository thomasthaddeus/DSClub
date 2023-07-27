"""
_summary_

_extended_summary_
"""

import pandas as pd
from scipy.stats import trim_mean, zscore
import matplotlib.pyplot as plt


def calculate_budget_statistics(filename, column_name, proportiontocut=0.2):
    """
    Calculate and return the mean, median, mode, and trimmed mean of a specified column from a CSV file.

    Args:
        filename (str): The path to the CSV file.
        column_name (str): The name of the column to analyze.
        proportiontocut (float, optional): The proportion of values to remove from each end of the data before calculating the trimmed mean. Default is 0.2.

    Returns:
        dict: A dictionary mapping the names of the measures to their calculated values.
    """
    try:
        df = pd.read_csv(filename)
        if column_name not in df.columns:
            raise ValueError(f"'{column_name}' not found in the dataframe.")
    except FileNotFoundError:
        raise ValueError(f"No such file or directory: '{filename}'")

    mean_value = df[column_name].mean()
    median_value = df[column_name].median()
    mode_value = df[column_name].mode()[0]
    trmean_value = trim_mean(df[column_name], proportiontocut=proportiontocut)

    return {
        'mean': mean_value,
        'median': median_value,
        'mode': mode_value,
        'trimmed_mean': trmean_value
    }


def load_data(filename):
    """
    Load data from a CSV file into a DataFrame.

    Args:
        filename (str): The path to the CSV file.

    Returns:
        DataFrame: The loaded data.
    """
    try:
        df = pd.read_csv(filename)
    except FileNotFoundError:
        raise ValueError(f"No such file or directory: '{filename}'")
    return df

def get_summary_statistics(df):
    """
    Get summary statistics for a DataFrame.

    Args:
        df (DataFrame): The DataFrame to analyze.

    Returns:
        DataFrame: A DataFrame with the summary statistics.
    """
    return df.describe()

def detect_outliers(df, column_name, method='zscore', threshold=3):
    """
    Detect outliers in a DataFrame using the specified method.

    Args:
        df (DataFrame): The DataFrame to analyze.
        column_name (str): The column to check for outliers.
        method (str, optional): The method to use for outlier detection. Default is 'zscore'.
        threshold (float, optional): The threshold to use for outlier detection. Default is 3.

    Returns:
        Series: A boolean Series where True indicates an outlier.
    """
    if method == 'zscore':
        z_scores = zscore(df[column_name])
        return abs(z_scores) > threshold
    else:
        raise ValueError(f"Unknown method: '{method}'")

def plot_data(df, column_name, plot_type='histogram'):
    """
    Plot data from a DataFrame.

    Args:
        df (DataFrame): The DataFrame to analyze.
        column_name (str): The column to plot.
        plot_type (str, optional): The type of plot to create. Default is 'histogram'.

    Returns:
        None
    """
    if plot_type == 'histogram':
        df[column_name].plot(kind='hist')
        plt.title(f"Histogram of {column_name}")
        plt.xlabel(column_name)
        plt.ylabel("Frequency")
        plt.show()
    else:
        raise ValueError(f"Unknown plot type: '{plot_type}'")
