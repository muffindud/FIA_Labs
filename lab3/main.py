from src.utils import *
from src.sudoku_solver import *
from copy import deepcopy
from time import time


PRINT_DELAY = 0.0


def main():
    # grid = generate_grid(27)

    with open("grids/grid5.txt") as f:
        grid = parse_grid(f.read())

    if PRINT_DELAY == 0.0:
        print("Original grid:")
        print(format_grid(grid))

    start_bu = time()
    solved_grid_bu = solve_backtracking(deepcopy(grid), PRINT_DELAY)
    end_bu = time()

    if PRINT_DELAY == 0.0:
        print("Unoptimized backtracking:")
        print(format_grid(solved_grid_bu))
        print(f"Backtracking unoptimized took {end_bu - start_bu:.2f} seconds")

    start_bo = time()
    solved_grid_bo = solve_backtracking_optimzed(deepcopy(grid), PRINT_DELAY)
    end_bo = time()

    if PRINT_DELAY == 0.0:
        print("Optimized backtracking:")
        print(format_grid(solved_grid_bo))
        print(f"Backtracking optimized took {end_bo - start_bo:.2f} seconds")

    start_sc = time()
    solved_grid_sc = single_cell_complete(deepcopy(grid), PRINT_DELAY)
    end_sc = time()

    if PRINT_DELAY == 0.0:
        print("Single cell complete:")
        print(format_grid(solved_grid_sc))
        print(f"Single cell complete took {end_sc - start_sc:.2f} seconds")

    start_hs = time()
    solved_grid_hs = heuristic_solve(deepcopy(grid), PRINT_DELAY)
    end_hs = time()

    if PRINT_DELAY == 0.0:
        print("Heuristic solve:")
        print(format_grid(solved_grid_hs))
        print(f"Heuristic solve took {end_hs - start_hs:.2f} seconds")

    if PRINT_DELAY != 0.0:
        print("Original grid:")
        print(format_grid(grid))

        print("Unoptimized backtracking:")
        print(format_grid(solved_grid_bu))
        print(f"Backtracking unoptimized took {end_bu - start_bu:.2f} seconds")

        print("Optimized backtracking:")
        print(format_grid(solved_grid_bo))
        print(f"Backtracking optimized took {end_bo - start_bo:.2f} seconds")

        print("Single cell complete:")
        print(format_grid(solved_grid_sc))
        print(f"Single cell complete took {end_sc - start_sc:.2f} seconds")

        print("Heuristic solve:")
        print(format_grid(solved_grid_hs))
        print(f"Heuristic solve took {end_hs - start_hs:.2f} seconds")


if __name__ == "__main__":
    main()
