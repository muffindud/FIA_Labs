"""Grid type definition"""
GridType = list[list[int]]


def parse_grid(grid_str: str) -> GridType:
    """Parse a string into a grid

    :param grid_str: The string to parse
    :return: The parsed grid
    """
    grid = []

    for row in grid_str.split("\n"):
        row = row.replace("*", "0")
        grid.append([int(cell) for cell in row])

    return grid


def format_grid(grid: GridType) -> str:
    """Format a grid into an ASCII art string

    :param grid: The grid to format
    :return: The formatted grid
    """
    g = [[str(cell) if cell != 0 else " " for cell in row] for row in grid]

    grid_str = f"""
    ╔═══╤═══╤═══╦═══╤═══╤═══╦═══╤═══╤═══╗
    ║ {g[0][0]} │ {g[0][1]} │ {g[0][2]} ║ {g[0][3]} │ {g[0][4]} │ {g[0][5]} ║ {g[0][6]} │ {g[0][7]} │ {g[0][8]} ║
    ╟───┼───┼───╫───┼───┼───╫───┼───┼───╢
    ║ {g[1][0]} │ {g[1][1]} │ {g[1][2]} ║ {g[1][3]} │ {g[1][4]} │ {g[1][5]} ║ {g[1][6]} │ {g[1][7]} │ {g[1][8]} ║
    ╟───┼───┼───╫───┼───┼───╫───┼───┼───╢
    ║ {g[2][0]} │ {g[2][1]} │ {g[2][2]} ║ {g[2][3]} │ {g[2][4]} │ {g[2][5]} ║ {g[2][6]} │ {g[2][7]} │ {g[2][8]} ║
    ╠═══╪═══╪═══╬═══╪═══╪═══╬═══╪═══╪═══╣
    ║ {g[3][0]} │ {g[3][1]} │ {g[3][2]} ║ {g[3][3]} │ {g[3][4]} │ {g[3][5]} ║ {g[3][6]} │ {g[3][7]} │ {g[3][8]} ║
    ╟───┼───┼───╫───┼───┼───╫───┼───┼───╢
    ║ {g[4][0]} │ {g[4][1]} │ {g[4][2]} ║ {g[4][3]} │ {g[4][4]} │ {g[4][5]} ║ {g[4][6]} │ {g[4][7]} │ {g[4][8]} ║
    ╟───┼───┼───╫───┼───┼───╫───┼───┼───╢
    ║ {g[5][0]} │ {g[5][1]} │ {g[5][2]} ║ {g[5][3]} │ {g[5][4]} │ {g[5][5]} ║ {g[5][6]} │ {g[5][7]} │ {g[5][8]} ║
    ╠═══╪═══╪═══╬═══╪═══╪═══╬═══╪═══╪═══╣
    ║ {g[6][0]} │ {g[6][1]} │ {g[6][2]} ║ {g[6][3]} │ {g[6][4]} │ {g[6][5]} ║ {g[6][6]} │ {g[6][7]} │ {g[6][8]} ║
    ╟───┼───┼───╫───┼───┼───╫───┼───┼───╢
    ║ {g[7][0]} │ {g[7][1]} │ {g[7][2]} ║ {g[7][3]} │ {g[7][4]} │ {g[7][5]} ║ {g[7][6]} │ {g[7][7]} │ {g[7][8]} ║
    ╟───┼───┼───╫───┼───┼───╫───┼───┼───╢
    ║ {g[8][0]} │ {g[8][1]} │ {g[8][2]} ║ {g[8][3]} │ {g[8][4]} │ {g[8][5]} ║ {g[8][6]} │ {g[8][7]} │ {g[8][8]} ║
    ╚═══╧═══╧═══╩═══╧═══╧═══╩═══╧═══╧═══╝
    """

    return grid_str



def is_vaild(grid: GridType, row: int, col: int, num: int) -> bool:
    """Check if a number can be placed in a cell

    :param grid: The grid to check
    :param row: The row of the cell
    :param col: The column of the cell
    :param num: The number to check
    :return: True if the number can be placed, False otherwise
    """
    for i in range(9):
        if grid[row][i] == num:
            return False
        if grid[i][col] == num:
            return False

    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if grid[i + start_row][j + start_col] == num:
                return False

    return True


def get_valid_numbers(grid: GridType, row: int, col: int) -> list[int]:
    """Get valid numbers for a cell

    :param grid: The grid to check
    :param row: The row of the cell
    :param col: The column of the cell
    :return: A list of valid numbers
    """
    valid_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(9):
        if grid[row][i] in valid_numbers:
            valid_numbers.remove(grid[row][i])
        if grid[i][col] in valid_numbers:
            valid_numbers.remove(grid[i][col])
        if not valid_numbers:
            return []

    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if grid[i + start_row][j + start_col] in valid_numbers:
                valid_numbers.remove(grid[i + start_row][j + start_col])
            if not valid_numbers:
                return []

    return valid_numbers


def check_grid(grid: GridType) -> bool:
    """Check if a grid is in a valid state

    :param grid: The grid to check
    :return: True if the grid is valid, False otherwise
    """
    for row in grid:
        row_nums = [num for num in row if num != 0]
        if len(row_nums) != len(set(row_nums)):
            return False

    for col in range(9):
        col_nums = [grid[row][col] for row in range(9) if grid[row][col] != 0]
        if len(col_nums) != len(set(col_nums)):
            return False

    for i in range(3):
        for j in range(3):
            square_nums = [grid[row][col] for row in range(3 * i, 3 * i + 3) for col in range(3 * j, 3 * j + 3) if grid[row][col] != 0]
            if len(square_nums) != len(set(square_nums)):
                return False

    return True


def find_empty_cell(grid: GridType) -> tuple[int, int]:
    """Find an empty cell in a grid

    :param grid: The grid to check
    :return: The row and column of the first empty cell found
    """
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return i, j

    return None


def get_empty_cells(grid: GridType) -> list[tuple[int, int]]:
    """Get a list of empty cells in a grid

    :param grid: The grid to check
    :return: A list of empty cells
    """
    empty_cells = []
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                empty_cells.append((i, j))

    return empty_cells


def get_single_possibilities(grid: GridType) -> dict[tuple[int, int], int]:
    """Get cells with only one possible number

    :param grid: The grid to check
    :return: A dictionary of cells with only one possible number
    """
    single_possibilities = {}
    for row, column in get_empty_cells(grid):
        valid_numbers = get_valid_numbers(grid, row, column)
        if len(valid_numbers) == 1:
            single_possibilities[(row, column)] = valid_numbers[0]

    return single_possibilities
