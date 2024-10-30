from pandas import read_csv
from json import dumps


DATA_PATH = "data/data.csv"
data = read_csv(DATA_PATH)


def get_unique_years():
    return list(set(data["Year"]))


def get_unique_job_titles():
    jobs = list(data["JobTitle"])
    for i in range(len(jobs)):
        job = ""
        for w in jobs[i].split(" "):
            if not w in ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", "XI", "XII", "XIII", "XIV", "XV"]:
                job += w.capitalize() + " "
            else:
                job += w + " "
        jobs[i] = job.strip()
    return list(set(jobs))


def main():
    # print job titles sorted by alphabetical order
    jobs = get_unique_job_titles()
    jobs.sort()
    print(dumps(jobs, indent=4))
    print(dumps(get_unique_years(), indent=4))


if __name__ == "__main__":
    main()
