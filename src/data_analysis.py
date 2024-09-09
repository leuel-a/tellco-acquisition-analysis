#!/usr/bin/env python3
"""Defines functions for calculating different quantitative
analysis on data frames"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def calculate_dispersion(column: pd.Series) -> pd.Series:
    """Computes dispersion parameters for a given column od data

    :param column: The column for which to compute the dispersion parameters.
    :type column: pd.Series

    :returns pd.Series: A Series containing the following dispersion parameters:
        - Range: The difference between the maximum and minimum values.
        - Variance: The average of squared deviations from the mean.
        - Standard Deviation: The square root of the variance.
        - Inter-quartile Range: The difference between the 75th and 25th percentiles.
        - Coefficient of Variation: The standard deviation divided by the mean.
    """
    return pd.Series({
        'Range': column.max() - column.min(),
        'Variance': column.var(),
        'Standard Deviation': column.std(),
        'Inter-quartile Range': column.quantile(0.75) - column.quantile(0.25),
        'Coefficient of Variation': column.std() / column.mean()
    })


def plot_scatter(df: pd.DataFrame, var1: str, var2: str) -> None:
    """
    Create a scatter plot with a regression line.

    :param df: pandas DataFrame
    :param var1: First Variable (independent).
    :param var2: Second Variable (dependent)
    :return: None
    """
    plt.figure(figsize=(20, 10))
    sns.scatterplot(x=var1, y=var2, data=df, label='Data Points')

    # Fit and plot the regression line
    sns.regplot(x=var1, y=var2, data=df, scatter=False, color='red', label='Regression Line')

    plt.title(f"Scatter Plot of {var1} vs {var2}")
    plt.xlabel(var1)
    plt.ylabel(var2)
    plt.legend()
    plt.show()
