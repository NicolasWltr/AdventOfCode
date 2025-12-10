def parse_buttons(buttons):
    result = []

    for button in buttons:
        button = button[1:-1]

        result.append(list(map(int, button.split(','))))

    return result

def parse_input(data):
    lines = data.split('\n')

    machines = []

    for line in lines:
        if not line.strip():
            continue
        
        arguments = line.split()

        light = arguments[0][1:-1]
        buttons = parse_buttons(arguments[1:-1])
        joltage = arguments[-1][1:-1]

        machines.append((light, buttons, joltage))

    return machines

def buttons_for_on(lights, buttons):
    n = len(buttons)

    minPresses = len(buttons)

    for i in range(2 ** n):
        result = ['.' for i in range(len(lights))]
        presses = 0
        for j in range(n):
            choice = (i >> j) & 1
            
            if choice == 1:
                presses += 1
                button = buttons[j]

                for switch in button:
                    result[switch] = '#' if result[switch] == '.' else '.'

        if lights == ''.join(result):
            minPresses = min(minPresses, presses)

    return minPresses

def solve_first(data):
    machines = parse_input(data)

    count = 0

    for machine in machines:
        lights, buttons, _ = machine

        count += buttons_for_on(lights, buttons)

    return count

def buttons_for_level(buttons, joltages):
    n = len(buttons)

    minPresses = len(buttons)

    for i in range(2 ** n):
        result = [0 for i in range(len(joltages.split(',')))]
        presses = 0
        for j in range(n):
            choice = (i >> j) & 1
            
            if choice == 1:
                presses += 1
                button = buttons[j]

                for switch in button:
                    result[switch] = result[switch] + 1

        if joltages == ','.join(result):
            minPresses = min(minPresses, presses)

    return minPresses

def solve_second(data):
    machines = parse_input(data)

    count = 0

    for machine in machines:
        _, buttons, joltages = machine

        count += buttons_for_level(buttons, joltages)

    return count