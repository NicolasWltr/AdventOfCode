def solve_first(data):
    start_pos = 50
    zeros = 0

    tasks = data.split('\n')

    for task in tasks:
        if not task.strip():
            continue
        
        direction, value = task[:1], int(task[1:])

        if direction == 'L':
            start_pos -= value
        elif direction == 'R':
            start_pos += value

        start_pos = start_pos % 100
        if start_pos == 0:
            zeros += 1

    return zeros


def solve_second(data):
    start_pos = 50

    zeros = 0

    tasks = data.split('\n')

    for task in tasks:
        if not task.strip():
            continue

        direction, value = task[:1], int(task[1:])
        old_pos = start_pos

        if direction == 'L':
            start_pos -= value
        elif direction == 'R':
            start_pos += value
        
        while start_pos < 0:
            zeros += 1
            start_pos += 100

        while start_pos > 100:
            zeros += 1
            start_pos -= 100

        if old_pos == 0 and direction == 'L':
            zeros -= 1

        start_pos = start_pos % 100

        if start_pos == 0:
                zeros += 1

    return zeros