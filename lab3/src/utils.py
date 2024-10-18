def parse_grid(grid_str: str) -> list[list[int]]:
    grid = []

    for row in grid_str.split("\n"):
        if not row:
            continue
        grid.append([cell for cell in row.split()])

    return grid
