from time import sleep
from copy import deepcopy

from src.utils import *


# Task 1
def solve_backtracking(grid: GridType, print_delay: float = 0.0) -> GridType:
    """Solve a Sudoku grid using backtracking

    :param grid: The grid to solve
    :return: The solved grid
    """
    g = deepcopy(grid)

    if not check_grid(g):
        raise ValueError("Invalid grid")

    def solve(g: GridType) -> bool:
        """Solve the grid using backtracking

        :param grid: The grid to solve
        :return: True if the grid is solved, False otherwise
        """
        for row in range(9):
            for col in range(9):
                if g[row][col] == 0:
                    for num in range(1, 10):
                        g[row][col] = num

                        if print_delay != 0.0:
                            print("\033[H\033[J")
                            print(format_grid(g))
                            sleep(print_delay)

                        if check_grid(g):
                            if solve(g):
                                return True

                        g[row][col] = 0

                    return False

        return True

    solve(g)

    if print_delay != 0.0:
        print("\033[H\033[J")

    return g


# Task 3
def solve_backtracking_optimzed(grid: GridType, print_delay: float = 0.0) -> GridType:
    """Solve a Sudoku grid using backtracking

    :param grid: The grid to solve
    :return: The solved grid
    """
    g = deepcopy(grid)

    if not check_grid(g):
        raise ValueError("Invalid grid")

    def solve(g: GridType) -> bool:
        """Solve the grid using backtracking

        :param grid: The grid to solve
        :return: True if the grid is solved, False otherwise
        """
        while True:
            # Task 2
            rc = find_empty_cell(g)

            if rc is None:
                break

            row, col = rc

            # Task 2
            for num in get_valid_numbers(g, row, col):
                g[row][col] = num

                if print_delay != 0.0:
                    print("\033[H\033[J")
                    print(format_grid(g))
                    sleep(print_delay)

                if solve(g):
                    return True

                g[row][col] = 0

            return False

        return True

    solve(g)

    if print_delay != 0.0:
        print("\033[H\033[J")

    return g


def single_cell_complete(grid: GridType, print_delay: float = 0.0) -> GridType:
    """Solve a Sudoku grid using a heuristic approach

    :param grid: The grid to solve
    :return: The solved grid
    """

    g = deepcopy(grid)

    if not check_grid(g):
        raise ValueError("Invalid grid")

    changed = True
    while changed:
        changed = False
        for (row, column), num in get_single_possibilities(g).items():
            changed = True
            g[row][column] = num

            if print_delay != 0.0:
                print("\033[H\033[J")
                print(format_grid(g))
                sleep(print_delay)

    solve_backtracking_optimzed(g, print_delay)

    if print_delay != 0.0:
        print("\033[H\033[J")

    return g


# Task 4
def heuristic_solve(grid: GridType, print_delay: float = 0.0) -> GridType:
    """Solve a Sudoku grid using a heuristic approach

    :param grid: The grid to solve
    :return: The solved grid
    """

    g = deepcopy(grid)

    if not check_grid(g):
        raise ValueError("Invalid grid")

    def solve(g: GridType) -> bool:
        """Solve the grid using a heuristic approach

        :param grid: The grid to solve
        :return: True if the grid is solved, False otherwise
        """
        for (row, column), nums in get_min_possibilities(g).items():
            for num in nums:
                g[row][column] = num

                if print_delay != 0.0:
                    print("\033[H\033[J")
                    print(format_grid(g))
                    sleep(print_delay)

                if solve(g):
                    return True

                g[row][column] = 0

            return False

        return True

    solve(g)

    if print_delay != 0.0:
        print("\033[H\033[J")

    return g
