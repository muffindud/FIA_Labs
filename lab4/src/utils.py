import pandas as pd
import numpy as np


def get_unique_years(data: pd.DataFrame) -> list:
    return list(set(data["Year"]))


def get_unique_job_titles(data: pd.DataFrame) -> list:
    jobs: list[str] = list(data["JobTitle"])
    for i in range(len(jobs)):
        jobs[i] = jobs[i].upper()
    return list(set(jobs))


def get_correlation_matrix(data: pd.DataFrame) -> pd.DataFrame:
    """Get the level of correlation between the columns of the data.

    :param data: The data to analyze.
    :return: A list of lists, where each list represents the correlation between the columns of the data.
    """

    data = data.apply(pd.to_numeric, errors="coerce")

    correlation_matrix = data.corr()
    correlation_matrix = correlation_matrix.dropna(axis=0, how="all")
    correlation_matrix = correlation_matrix.dropna(axis=1, how="all")
    correlation_matrix = correlation_matrix.round(2)
    correlation_matrix = correlation_matrix.iloc[1:, 1:]

    return correlation_matrix


def clean_data(data: pd.DataFrame) -> pd.DataFrame:
    for i in range(len(data)):
        data.loc[i, "JobTitle"] = data.loc[i, "JobTitle"].upper()

    data = data[data["EmployeeName"] != "Not provided"]

    return data
