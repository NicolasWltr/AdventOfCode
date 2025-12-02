def solvable(target, numbers, operators=['+', '*']):
    n = len(numbers) - 1
    for i in range(len(operators) ** n):
        result = numbers[0]
        temp = i
        for j in range(n):
            choice = temp % len(operators)
            op = operators[choice]
            temp //= len(operators)

            next_number = numbers[j + 1]
            if op == '+':
                result += next_number
            elif op == '*':
                result *= next_number
            elif op == '||':
                result = int(str(result) + str(next_number))

        if result == target:
            return True
    return False


def solve_first(data):
    lines = data.splitlines()

    count_solvable = 0

    for line in lines:
        if not line.strip():
            continue

        target, numbers = line.split(': ')

        target = int(target)
        numbers = list(map(int, numbers.split(' ')))

        count_solvable += target if solvable(target, numbers) else 0

    return count_solvable


def solve_second(data):
    lines = data.splitlines()

    count_solvable = 0

    for line in lines:
        if not line.strip():
            continue

        target, numbers = line.split(': ')

        target = int(target)
        numbers = list(map(int, numbers.split(' ')))

        count_solvable += target if solvable(target, numbers, ['+', '*', '||']) else 0

    return count_solvable