from src.utils import *
from src.sudoku_solver import *
from copy import deepcopy
from time import time


PRINT_DELAY = 0.0


def main():
    with open("grids/grid4.txt", "r") as f:
        grid_str = f.read()
    grid = parse_grid(grid_str)

    start_time_ub = time()
    backtracking_unoptimized = solve_backtracking(
        deepcopy(grid),
        PRINT_DELAY
    )
    end_time_ub = time()

    start_time_ob = time()
    backtracking_optimized = solve_backtracking_optimzed(
        deepcopy(grid),
        PRINT_DELAY
    )
    end_time_ob = time()

    if backtracking_optimized != backtracking_unoptimized:
        print("The optimized and unoptimized backtracking algorithms did not produce the same result")

    print("Original grid:")
    print(format_grid(grid))

    print("Solved grid:")
    print(format_grid(backtracking_optimized))

    print(f"Unoptimized backtracking: {end_time_ub - start_time_ub:.2f} seconds")
    print(f"Optimized backtracking: {end_time_ob - start_time_ob:.2f} seconds")

if __name__ == "__main__":
    main()
