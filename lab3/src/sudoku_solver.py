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
                        if is_vaild(grid, row, col, num):
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
