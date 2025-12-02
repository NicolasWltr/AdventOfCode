def make_grid(data):
    lines = data.split('\n')
    grid = []

    for line in lines:
        if line:
            grid.append(list(line))

    return grid

def rotate90(data):
    result_string = ""

    grid = make_grid(data)

    while True:
        for row in grid:
            result_string += row.pop()
        result_string += '\n'

        if not grid[0]:
            break

    return result_string

def rotate45(data, left):
    grid = make_grid(data)

    result_string = ""

    start_x = len(grid[0]) - 1 if left else 0
    start_y = 0

    x = start_x
    y = start_y

    while True:
        result_string += grid[y][x]
        if left:
            x += 1
            y += 1
        else:
            x += 1
            y -= 1

        y_in_grid = y < len(grid) and y >= 0
        x_in_grid = False
        if y_in_grid:
            x_in_grid = x < len(grid[y]) and x >= 0

        next_in_grid = y_in_grid and x_in_grid

        if not next_in_grid:
            result_string += '\n'
            if left:
                if start_x > 0:
                    start_x -= 1
                elif start_y < len(grid) - 1:
                    start_y += 1
                else:
                    break
            else:
                if start_y < len(grid) - 1:
                    start_y += 1
                elif start_x < len(grid[y]) - 1:
                    start_x += 1
                else:
                    break
            x = start_x
            y = start_y

    return result_string

def solve_first(data):
    count = 0

    count += data.count('XMAS')
    count += data.count('SAMX')

    rotated90 = rotate90(data)

    count += rotated90.count('XMAS')
    count += rotated90.count('SAMX')

    rotated45 = rotate45(data, True)

    count += rotated45.count('XMAS')
    count += rotated45.count('SAMX')

    leftrotated45 = rotate45(data, False)

    count += leftrotated45.count('XMAS')
    count += leftrotated45.count('SAMX')

    return count



def solve_second(data):
    grid = make_grid(data)

    count = 0

    for y in range(1, len(grid) - 1):
        for x in range(1, len(grid[y]) - 1):
            if grid[y][x] == 'A':
                tlbr_diago = f"{grid[y-1][x-1]}{grid[y][x]}{grid[y+1][x+1]}"
                bltr_diago = f"{grid[y+1][x-1]}{grid[y][x]}{grid[y-1][x+1]}"

                if (tlbr_diago == 'MAS' or tlbr_diago == 'SAM') and (bltr_diago == 'MAS' or bltr_diago == 'SAM'):
                    count += 1 

    return count