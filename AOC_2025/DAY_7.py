def make_grid(data):
    lines = data.split('\n')
    grid = []

    for line in lines:
        if line:
            grid.append(list(line))

    return grid

def find_star(grid):
    for i in range(len(grid[0])):
        if grid[0][i] == 'S':
            return (i, 0)

def traverse_tree(grid, pos):
    x, y = pos

    if y >= 0 and y < len(grid) and x >= 0 and x < len(grid[y]):
        if grid[y][x] == '.':
            grid[y][x] = '|'
    else:
        return 0
    next_y = y + 1

    if next_y < len(grid):
        if grid[next_y][x] == '^':
            left = traverse_tree(grid, (x-1, next_y))
            right = traverse_tree(grid, (x+1, next_y))
            return 1 + left + right
        elif grid[next_y][x] == '|':
            return 0
        else:
            split = traverse_tree(grid, (x, next_y))
            return split
    else:
        return 0

def solve_first(data):
    grid = make_grid(data)

    star_pos_x, star_pos_y = find_star(grid)

    return traverse_tree(grid, (star_pos_x, star_pos_y+1))

def solve_second(data):
    grid = make_grid(data)

    star_pos_x, star_pos_y = find_star(grid)

    traverse_tree(grid, (star_pos_x, star_pos_y + 1))

    for y, row in enumerate(grid):
        for x, element in enumerate(row):
            summe = 0
            if element == '|':
                if grid[y-1][x] == 'S':
                    summe = 1
                if type(grid[y-1][x]) == int:
                    summe += grid[y-1][x]

                if x-1 >= 0 and grid[y][x-1] == '^' and type(grid[y-1][x-1]) == int:
                    summe += grid[y-1][x-1]
                if x+1 < len(row) and grid[y][x+1] == '^' and type(grid[y-1][x+1]) == int:
                    summe += grid[y-1][x+1]

                grid[y][x] = summe

    lastRow = [(grid[-1][x] if grid[-1][x] != '.' else 0) for x in range(len(grid[-1]))]

    return sum(lastRow)
