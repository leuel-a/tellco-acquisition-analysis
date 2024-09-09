#!/usr/bin/env python3
from typing import List

import numpy as np
import pandas as pd
import scipy.stats as stats
from scipy.stats import zscore
import matplotlib.pyplot as plt


def missing_values(df: pd.DataFrame) -> pd.DataFrame:
    """Prints the number of missing values in the DataFrame

    :param df: DataFrame to check for missing values
    :type df: pd.DataFrame

    :return: A dataframe containing the missing values
    :rtype: pd.DataFrame
    """
    # total missing values
    missing = df.isnull().sum()

    # percentage of missing values
    missing_percent = 100 * df.isnull().sum() / len(df)

    # dtype of missing values
    missing_dtypes = df.dtypes

    missing_table = pd.concat([missing, missing_percent, missing_dtypes], axis=1)

    # rename the columns
    missing_table = missing_table.rename(
        columns={0: 'Missing Values', 1: '% of Total Values', 2: 'Data Type'}
    )

    missing_table = missing_table[missing_table.iloc[:, 1] != 0].sort_values(
        "% of Total Values", ascending=False).round(4)

    print(
        f"Your selected DataFrame has {str(df.shape[1])} columns.\n",
        f"There are {missing_table.shape[0]} columns that have missing values."
    )

    return missing_table


def convert_bytes_to_megabytes(df: pd.DataFrame, bytes_data: List[str]) -> pd.DataFrame:
    """Converts specified columns from bytes to megabytes in a DataFrame

    :param df: DataFrame containing the data to be converted
    :type df: pd.DataFrame

    :param bytes_data: List of column names to be converted from bytes to megabytes
    :type bytes_data: List[str]

    :return: DataFrame with the specified columns to be converted to megabytes
    :rtype: pd.DataFrame
    """

    megabyte = 1 * 10e+5
    df[bytes_data] = df[bytes_data] / megabyte
    return df[bytes_data]


def convert_milliseconds_to_seconds(df: pd.DataFrame, columns: List[str]) -> pd.DataFrame:
    """Converts specified columns from bytes to megabytes in a DataFrame

    :param df: DataFrame containing the data to be converted
    :type df: pd.DataFrame

    :param columns: List of column names to be converted from bytes to megabytes
    :type columns: List[str]

    :return: DataFrame with the specified columns to be converted to megabytes
    :rtype: pd.DataFrame
    """
    second = 1000
    df[columns] = df[columns] / second
    return df[columns]


def convert_milliseconds_to_minute(df: pd.DataFrame, columns: List[str]) -> pd.DataFrame:
    """Converts specified columns from bytes to megabytes in a DataFrame

    :param df: DataFrame containing the data to be converted
    :type df: pd.DataFrame

    :param columns: List of column names to be converted from bytes to megabytes
    :type columns: List[str]

    :return: DataFrame with the specified columns to be converted to megabytes
    :rtype: pd.DataFrame
    """
    minute = 60 * 1000
    df[columns] = df[columns] / minute
    return df[columns]


def convert_megabytes_to_gigabytes(df: pd.DataFrame, columns: List[str]) -> pd.DataFrame:
    """Converts specified columns from bytes to megabytes in a DataFrame

    :param df: DataFrame containing the data to be converted
    :type df: pd.DataFrame

    :param columns: List of column names to be converted from bytes to megabytes
    :type columns: List[str]

    :return: DataFrame with the specified columns to be converted to megabytes
    :rtype: pd.DataFrame
    """
    gigabyte = 1 * 10e+3
    df[columns] = df[columns] / gigabyte
    return df[columns]

def convert_bytes_to_giga_bytes(df: pd.DataFrame, columns: List[str]) -> pd.DataFrame:
    """Converts specified columns from bytes to gigabytes in a DataFrame

    :param df: Dataframe containing the data to be converted
    :type df: pd.DataFrame

    :param columns: List of column names to be converted from byte to gigabytes
    :type columns: List[str]

    :return: DataFrame with the specified columns to be converted to gigabytes
    :rtype: pd.DataFrame
    """
    giga_byte = 1 * 10**9
    df[columns] = df[columns] / giga_byte

    return df[columns]

def plot_user_application_data(df: pd.DataFrame, columns: List[str], user: str) -> None:
    plt.figure(figsize=(20, 10))

    plt.title(f"User for user with IMSI {user}")

    plt.bar(columns, df.loc[user, columns].values)

    plt.show()
