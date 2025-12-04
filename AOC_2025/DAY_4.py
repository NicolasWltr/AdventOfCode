def make_grid(data):
    lines = data.split('\n')
    grid = []

    for line in lines:
        if line:
            grid.append(list(line))

    return grid

def position_in_grid(position, grid):
    if not position:
        return False
    x, y = position
    return y >= 0 and y < len(grid) and x >= 0 and x < len(grid[y])

def count_adjacent(x, y, grid):
    adjacent = 0

    if position_in_grid((x-1, y-1), grid) and (grid[y-1][x-1] == '@' or grid[y-1][x-1] == '#'):
        adjacent += 1
    if position_in_grid((x, y-1), grid) and (grid[y-1][x] == '@' or grid[y-1][x] == '#'):
        adjacent += 1
    if position_in_grid((x+1, y-1), grid) and (grid[y-1][x+1] == '@' or grid[y-1][x+1] == '#'):
        adjacent += 1
    if position_in_grid((x-1, y), grid) and (grid[y][x-1] == '@' or grid[y][x-1] == '#'):
        adjacent += 1
    if position_in_grid((x+1, y), grid) and (grid[y][x+1] == '@' or grid[y][x+1] == '#'):
        adjacent += 1
    if position_in_grid((x-1, y+1), grid) and (grid[y+1][x-1] == '@' or grid[y+1][x-1] == '#'):
        adjacent += 1
    if position_in_grid((x, y+1), grid) and (grid[y+1][x] == '@' or grid[y+1][x] == '#'):
        adjacent += 1
    if position_in_grid((x+1, y+1), grid) and (grid[y+1][x+1] == '@' or grid[y+1][x+1] == '#'):
        adjacent += 1

    return adjacent

def solve_first(data):
    grid = make_grid(data)
    count = 0

    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] != '@':
                continue
            
            if count_adjacent(x, y, grid) < 4:
                count += 1

    return count


def solve_second(data):
    grid = make_grid(data)
    count = 0
    currentCount = -1
    while currentCount != count:
        currentCount = count
        for y in range(len(grid)):
            for x in range(len(grid[y])):
                if grid[y][x] != '@':
                    continue
                
                if count_adjacent(x, y, grid) < 4:
                    grid[y][x] = '#'
                    count += 1

        for y in range(len(grid)):
            for x in range(len(grid[y])):
                if grid[y][x] == '#':
                    grid[y][x] = '.'

    return count