""""Grid type definition"""
GridType = list[list[int]]


def parse_grid(grid_str: str) -> GridType:
    """Parse a string into a grid

    Keyword arguments:
    grid_str -- The string to parse
    Return: The parsed grid
    """
    grid = []

    for row in grid_str.split("\n"):
        row = row.replace("*", "0")
        grid.append([int(cell) for cell in row])

    return grid


def format_grid(grid: GridType) -> str:
    """Format a grid into an ASCII art string

    Keyword arguments:
    grid -- The grid to format
    Return: The formatted grid as a string
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

    Keyword arguments:
    grid -- The grid to check
    row -- The row to check
    col -- The column to check
    num -- The number to check
    Return: True if the number can be placed in the cell, False otherwise
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

    Keyword arguments:
    grid -- The grid to check
    row -- The row of the cell
    col -- The column of the cell
    Return: A list of valid numbers for the cell
    """
    valid_numbers = []
    for num in range(1, 10):
        if is_vaild(grid, row, col, num):
            valid_numbers.append(num)

    return valid_numbers
