from pandas import read_csv
from json import dumps
from matplotlib import pyplot as plt
import seaborn as sns

from src.utils import *


DATA_PATH = "data/cleaned_data.csv"
try:
    data = read_csv(DATA_PATH)
except FileNotFoundError:
    DATA_PATH = "data/data.csv"
    data = read_csv(DATA_PATH)
    data = clean_data(data)
    data.to_csv("data/cleaned_data.csv", index=False)


def main():
    correlation_matrix = get_correlation_matrix(data)

    plt.title("Correlation Matrix")
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0, vmin=-1, vmax=1, square=True)
    plt.savefig("plots/correlation_matrix.png", bbox_inches="tight", dpi=300)


if __name__ == "__main__":
    main()
