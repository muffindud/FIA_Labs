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


def ac3_solve(grid: GridType, print_delay: int = 0.0):
    """Solve a Sudoku grid using the AC3 algorithm

    :param grid: The grid to solve
    :param print_delay: The delay between each print
    :return: The solved grid
    """

    g = deepcopy(grid)

    if not check_grid(g):
        raise ValueError("Invalid grid")

    def get_neighbours(cell: tuple[int, int]) -> list[tuple[int, int]]:
        """Get the neighbours of a cell

        :param cell: The cell to get the neighbours of
        :return: A list of neighbours
        """
        row, col = cell
        neighbours = []

        for i in range(9):
            if i != col:
                neighbours.append((row, i))

            if i != row:
                neighbours.append((i, col))

        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if i + start_row != row and j + start_col != col:
                    neighbours.append((i + start_row, j + start_col))

        return neighbours

    domains: dict[tuple[int, int], set[int]] = {(row, col): set(get_valid_numbers(g, row, col)) for row, col in get_empty_cells(g)}

    def get_arcs(row: int, col: int) -> list[tuple[int, int]]:
        """Get the arcs for a cell

        :param row: The row of the cell
        :param col: The column of the cell
        :return: A list of arcs
        """
        arcs = []

        for r, c in domains.keys():
            if (r, c) != (row, col):
                arcs.append((r, c))

        return arcs

    arcs: list[tuple[tuple[int, int], tuple[int, int]]] = []

    for row, col in domains.keys():
        arcs.extend([((row, col), cell) for cell in get_arcs(row, col)])

    def ac3() -> bool:
        """Perform the AC3 algorithm

        :return: True if the grid is solved, False otherwise
        """
        queue = arcs.copy()

        while queue:
            xi, xj = queue.pop(0)

            print(f"Revising {xi} and {xj}")
            if revise(xi, xj):
                for key in domains.keys():
                    print(key, domains[key])
                if len(domains[xi]) == 0:
                    return False

                for xk in get_neighbours(xi):
                    if xk != xj:
                        queue.append((xk, xi))

        return True

    # for key in domains.keys():
    #     print(key, domains[key])

    def revise(xi: tuple[int, int], xj: tuple[int, int]) -> bool:
        """Revise the domains of two cells

        :param xi: The first cell
        :param xj: The second cell
        :return: True if the domains were revised, False otherwise
        """
        revised = False

        for x in domains[xi].copy():
            if not any(y in domains[xj] for y in domains[xi]):
                domains[xi].remove(x)
                revised = True

        return revised

    ac3()

    print("DEBUG")
    print(format_grid(g))

    return g
