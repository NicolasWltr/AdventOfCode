def get_ranges(data):
    ranges = data.split(',')

    ranges_as_tuple = []

    for range in ranges:
        ranges_as_tuple.append(tuple(map(int, range.split('-'))))

    return ranges_as_tuple

def get_invalid_id_half(range_as_tuple):
    first, last = range_as_tuple

    invalid_ids = set()

    for i in range(first, last + 1):
        as_string = str(i)

        first_half, second_half = as_string[:len(as_string) // 2], as_string[len(as_string) // 2:]

        if first_half == second_half:
            invalid_ids.add(i)

    return invalid_ids

def split_string(s, n):
    return [s[i:i+n] for i in range(0, len(s), n)]   

def get_invalid_id_sub(range_as_tuple):
    first, last = range_as_tuple

    invalid_ids = set()

    for i in range(first, last + 1):
        as_string = str(i)

        for split_length in range(1, len(as_string) // 2 + 1):
            if len(as_string) % split_length != 0:
                continue
            split = split_string(as_string, split_length)
            
            invalid = True

            for j in range(len(split) - 1):
                if split[j] != split[j + 1]:
                    invalid = False
                    break
            if invalid:
                invalid_ids.add(i)

    return invalid_ids


def solve_first(data):
    ranges = get_ranges(data)

    invalid_ids = set()

    for range_as_tuple in ranges:
        invalid_ids = invalid_ids.union(get_invalid_id_half(range_as_tuple))

    sum = 0

    for id in invalid_ids:
        sum += id

    return sum
    

def solve_second(data):
    ranges = get_ranges(data)

    invalid_ids = set()

    for range_as_tuple in ranges:
        invalid_ids = invalid_ids.union(get_invalid_id_sub(range_as_tuple))

    sum = 0

    for id in invalid_ids:
        sum += id

    return sum