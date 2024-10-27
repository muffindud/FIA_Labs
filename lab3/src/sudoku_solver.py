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
        for row in range(9):
            for col in range(9):
                if grid[row][col] == 0:
                    for num in range(1, 10):
                        grid[row][col] = num

                        if print_delay != 0.0:
                            print("\033[H\033[J")
                            print(format_grid(grid))
                            sleep(print_delay)

                        if check_grid(grid):
                            if solve(grid):
                                return True

                        grid[row][col] = 0

                    return False

        return True

    solve(grid)

    if print_delay != 0.0:
        print("\033[H\033[J")

    return grid


# Task 3
def solve_backtracking_optimzed(grid: GridType, print_delay: float = 0.0) -> GridType:
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
            # Task 2
            rc = find_empty_cell(grid)

            if rc is None:
                break

            row, col = rc

            # Task 2
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


def single_cell_complete(grid: GridType, print_delay: float = 0.0) -> GridType:
    """Solve a Sudoku grid using a heuristic approach

    :param grid: The grid to solve
    :return: The solved grid
    """

    changed = True
    while changed:
        changed = False
        for (row, column), num in get_single_possibilities(grid).items():
            changed = True
            grid[row][column] = num

            if print_delay != 0.0:
                print("\033[H\033[J")
                print(format_grid(grid))
                sleep(print_delay)

    if print_delay != 0.0:
        print("\033[H\033[J")

    return grid
