def make_grid(data):
    lines = data.split('\n')
    grid = []

    for line in lines:
        if line:
            grid.append(list(line))

    return grid

def find_pos(grid):
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == '^':
                return (x, y)
    return None

def position_in_grid(position, grid):
    if not position:
        return False
    x, y = position
    return y >= 0 and y < len(grid) and x >= 0 and x < len(grid[y])

def obstacle_ahead(position, direction, grid):
    x, y = position

    if direction == 0:
        x -= 1
    elif direction == 1:
        y -= 1
    elif direction == 2:
        x += 1
    elif direction == 3:
        y += 1

    if not position_in_grid((x, y), grid):
        return False

    return grid[y][x] == '#'

def traverse_grid(grid):
    direction = 1 
    start = find_pos(grid)
    position = start

    visitedDirectional = set()
    visited = set()

    while position_in_grid(position, grid):
        x, y = position
        grid[y][x] = "X"
        if (position, direction) in visited:
            return None, None
        if position != start:
            visited.add((position, direction))
        visitedDirectional.add(position)

        while obstacle_ahead(position, direction, grid):
            direction = (direction + 1) % 4

        if direction == 0:
            position = (x - 1, y)
        elif direction == 1:
            position = (x, y - 1)
        elif direction == 2:
            position = (x + 1, y)
        elif direction == 3:
            position = (x, y + 1)

    return visitedDirectional, visited


def solve_first(data):
    grid = make_grid(data)

    visited, _ = traverse_grid(grid)

    return len(visited)

def has_loop(grid):
    result = traverse_grid(grid)

    visitedDirectional, _ = result

    return visitedDirectional is None

def solve_second(data):
    grid = make_grid(data)

    _, possible_obstacles = traverse_grid(grid)

    obstacles = set()

    for (x, y), _ in possible_obstacles:
        new_grid = make_grid(data)
        new_grid[y][x] = '#'
        if has_loop(new_grid):
            obstacles.add((x, y))

    return len(obstacles)