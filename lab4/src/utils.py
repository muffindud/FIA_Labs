import pandas as pd


def get_unique_years(data: pd.DataFrame) -> list:
    return list(set(data["Year"]))


def get_unique_job_titles(data: pd.DataFrame) -> list:
    return list(set(data["JobTitle"]))


def get_unique_job_titles(data: pd.DataFrame) -> list:
    jobs: list[str] = list(data["JobTitle"])
    for i in range(len(jobs)):
        jobs[i] = jobs[i].upper()
    return list(set(jobs))


def clean_data(data: pd.DataFrame) -> pd.DataFrame:
    for i in range(len(data)):
        data.loc[i, "JobTitle"] = data.loc[i, "JobTitle"].upper()

    return data
