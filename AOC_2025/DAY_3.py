def bank_to_intarray(bank):
    return [int(bank[index]) for index in range(len(bank))]

def find_largest(bank):
    largest = -1
    index = -1

    for ind, batterie in enumerate(bank):
        if batterie > largest:
            index = ind
            largest = batterie

    return index, largest

def solve_first(data):
    banks = data.splitlines()

    sum = 0

    for bank in banks:
        bank_array = bank_to_intarray(bank)
        index, largest = find_largest(bank_array[:-1])

        _, second_largest = find_largest(bank_array[index+1:])

        sum += largest * 10 + second_largest

    return sum

def array_to_int(selected):
    sum = 0

    for index, batterie in enumerate(selected):
        sum += batterie * pow(10, len(selected) - 1 - index)

    return sum

def solve_second(data):
    banks = data.splitlines()

    sum = 0

    for bank in banks:
        bank_array = bank_to_intarray(bank)

        value = 0
        prevInd = -1

        for i in reversed(range(0, 12)):
            index, largest = find_largest(bank_array[prevInd + 1:-i if i > 0 else len(bank_array)])
            prevInd = index + prevInd + 1
            value += largest * pow(10, i)
        
        sum += value

    return sum