from src.utils import *
from src.sudoku_solver import *
from copy import deepcopy
from time import time


PRINT_DELAY = 0.0


def main():
    with open("grids/grid3.txt", "r") as f:
        grid_str = f.read()
    grid = parse_grid(grid_str)

    start_time = time()
    solved_grid = solve_backtracking(deepcopy(grid), PRINT_DELAY)
    end_time = time()

    print("Original Grid:")
    print(format_grid(grid))

    print("Solved Grid:")
    print(format_grid(solved_grid))

    print(f"Time taken: {end_time - start_time:.2f}s")


if __name__ == "__main__":
    main()
