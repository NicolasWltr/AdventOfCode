def make_grid(data):
    lines = data.split('\n')
    grid = []

    for line in lines:
        if line:
            grid.append(line.split())

    return grid

def make_grid_per_char(data):
    lines = data.split('\n')
    grid = []

    for line in lines:
        if line:
            grid.append(list(line))

    return grid

def solve_first(data):
    grid = make_grid(data)

    rows = len(grid)
    cols = len(grid[0])
    transposed = [[grid[x][y] for x in range(rows)] for y in range(cols)]

    result = 0

    for row in transposed:
        operator = row[-1]
        numbers = row[:-1]

        if operator == '*':
            result_for_row = 1
            for x in numbers:
                result_for_row *= int(x)
            result += result_for_row

        if operator == '+':
            for x in numbers:
                result += int(x)
        

    return result

def solve_second(data):
    grid = make_grid_per_char(data)

    rows = len(grid)
    columns = len(grid[0])
    transposed = [[grid[x][y] for x in range(rows)] for y in range(columns)]

    result = 0
    current_operator = ''

    mul_result = 1
    for row in transposed:
        operator = row[-1]
        if operator == '*' or operator == '+':
            if current_operator == '*':
                result += mul_result
                mul_result = 1
            current_operator = operator

        number_as_string = (''.join(row[:-1]))

        if not number_as_string.split():
            continue
        
        number = int(number_as_string)

        if current_operator == '*':
            mul_result *= number
        elif current_operator == '+':
            result += number

    return result