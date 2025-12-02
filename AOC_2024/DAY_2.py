def is_save(list):
    increasing = list[0] < list[1]

    for i in range(1, len(list)):
        distance = list[i] - list[i - 1]
        if abs(distance) > 3 or abs(distance) < 1:
            return False
        if (increasing and distance < 0) or (not increasing and distance > 0):
            return False
    
    return True

def puzzle_safe(list, threshold):
    is_safe = is_save(list)

    if is_safe:
        return 1

    if threshold > 0:
        check = 0
        for i in range(len(list)):
            test = list.copy()
            test.pop(i)
            check += puzzle_safe(test, threshold - 1)

        if check > 0:
            return 1
        
    return 0

def solve_first(data):
    lines = data.split("\n")
    safe = 0

    for line in lines:
        if not line.strip():
            continue

        puzzle = list(map(int, line.split()))

        safe += puzzle_safe(puzzle, 0)
    
    return safe


def solve_second(data):
    lines = data.split("\n")
    safe = 0

    for line in lines:
        if not line.strip():
            continue

        puzzle = list(map(int, line.split()))

        safe += puzzle_safe(puzzle, 1)
    
    return safe