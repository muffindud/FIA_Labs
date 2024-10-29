from src.utils import *
from src.sudoku_solver import *
from copy import deepcopy
from time import time


PRINT_DELAY = 0.05

SAVE_LAST_GRID = True

UNOPTIMIZED_SOLVE = False
OPTIMIZED_SOLVE = False
HEURISTIC_SOLVE = True
AC3_SOLVE = False


def main():
    grid = generate_grid(27)

    # with open("grids/grid5.txt") as f:
    #     grid = parse_grid(f.read())

    if SAVE_LAST_GRID:
        with open("grids/gridLast.txt", "w") as f:
            for row in grid:
                f.write("".join(str(cell) if cell != 0 else "*" for cell in row) + "\n")

    if PRINT_DELAY == 0.0:
        print("Original grid:")
        print(format_grid(grid))

    if UNOPTIMIZED_SOLVE:
        start_bu = time()
        solved_grid_bu = solve_backtracking(grid, PRINT_DELAY)
        end_bu = time()

        if PRINT_DELAY == 0.0:
            print("Unoptimized backtracking:")
            print(format_grid(solved_grid_bu))
            print(f"Backtracking unoptimized took {end_bu - start_bu:.2f} seconds")

    if OPTIMIZED_SOLVE:
        start_bo = time()
        solved_grid_bo = solve_backtracking_optimzed(grid, PRINT_DELAY)
        end_bo = time()

        if PRINT_DELAY == 0.0:
            print("Optimized backtracking:")
            print(format_grid(solved_grid_bo))
            print(f"Backtracking optimized took {end_bo - start_bo:.2f} seconds")

    if HEURISTIC_SOLVE:
        start_hs = time()
        solved_grid_hs = heuristic_solve(grid, PRINT_DELAY)
        end_hs = time()

        if PRINT_DELAY == 0.0:
            print("Heuristic solve:")
            print(format_grid(solved_grid_hs))
            print(f"Heuristic solve took {end_hs - start_hs:.2f} seconds")

    if AC3_SOLVE:
        start_ac3 = time()
        solved_grid_ac3 = ac3_solve(grid, PRINT_DELAY)
        end_ac3 = time()

        if PRINT_DELAY == 0.0:
            print("AC3 solve:")
            print(format_grid(solved_grid_ac3))
            print(f"AC3 solve took {end_ac3 - start_ac3:.2f} seconds")

    if PRINT_DELAY != 0.0:
        print("Original grid:")
        print(format_grid(grid))

        if UNOPTIMIZED_SOLVE:
            print("Unoptimized backtracking:")
            print(format_grid(solved_grid_bu))
            print(f"Backtracking unoptimized took {end_bu - start_bu:.2f} seconds")

        if OPTIMIZED_SOLVE:
            print("Optimized backtracking:")
            print(format_grid(solved_grid_bo))
            print(f"Backtracking optimized took {end_bo - start_bo:.2f} seconds")

        if HEURISTIC_SOLVE:
            print("Heuristic solve:")
            print(format_grid(solved_grid_hs))
            print(f"Heuristic solve took {end_hs - start_hs:.2f} seconds")

        if AC3_SOLVE:
            print("AC3 solve:")
            print(format_grid(solved_grid_ac3))
            print(f"AC3 solve took {end_ac3 - start_ac3:.2f} seconds")


if __name__ == "__main__":
    main()
