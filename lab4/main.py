from pandas import read_csv
from json import dumps
from matplotlib import pyplot as plt
import seaborn as sns

from src.utils import *


GENERATE_CORRELATION_MATRIX = False
GENERATE_SCATTER_PLOT = False

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

    if GENERATE_CORRELATION_MATRIX:
        plt.title("Correlation Matrix")
        sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0, vmin=-1, vmax=1, square=True)
        plt.savefig("plots/correlation_matrix.png", bbox_inches="tight", dpi=300)

    if GENERATE_SCATTER_PLOT:
        plt.title("Benefits and BasePay")
        sns.scatterplot(data=data, x="BasePay", y="Benefits", alpha=0.5, s=10)
        plt.savefig("plots/benefits_vs_basepay.png", bbox_inches="tight", dpi=300)


if __name__ == "__main__":
    main()
