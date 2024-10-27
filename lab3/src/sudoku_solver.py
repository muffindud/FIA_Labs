from time import sleep
from src.utils import *


# Task 1
def solve_backtracking(grid: GridType, print_delay: float = 0.0) -> GridType:
    """Solve a Sudoku grid using backtracking

    :param grid: The grid to solve
    :return: The solved grid
    """

    def solve(grid: GridType) -> bool:
        """Solve the grid using backtracking

        :param grid: The grid to solve
        :return: True if the grid is solved, False otherwise
        """
        while True:
            rc = find_empty_cell(grid)

            if rc is None:
                break

            row, col = rc

            for num in get_valid_numbers(grid, row, col):
                grid[row][col] = num

                if print_delay != 0.0:
                    print("\033[H\033[J")
                    print(format_grid(grid))
                    sleep(print_delay)

                if solve(grid):
                    return True

                grid[row][col] = 0

            return False

        return True

    solve(grid)

    if print_delay != 0.0:
        print("\033[H\033[J")

    return grid
