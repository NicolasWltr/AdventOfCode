def extract_data(data):
    plain_ranges, plain_available = data.split('\n\n')

    ranges = []

    for range in plain_ranges.split('\n'):
        first, last = range.split('-')

        ranges += [(int(first), int(last))]

    available = plain_available.strip().split('\n')

    return ranges, available

def is_available(item, ranges):
    for range in ranges:
        first, last = range

        if item >= first and item <= last:
            return True
        
    return False


def solve_first(data):
    ranges, available = extract_data(data)

    count = 0

    for item in available:
        if is_available(int(item), ranges):
            count += 1

    return count

def resolve_overlaps(ranges):
    ranges = sorted(ranges, key=lambda x: (x[0], x[1]))

    merged = []
    for first, last in ranges:
        if not merged:
            merged.append([first, last])
        else:
            _, before_end = merged[-1]
            if first <= before_end + 1:
                merged[-1][1] = max(before_end, last)
            else:
                merged.append([first, last])

    count = sum(end - start + 1 for start, end in merged)
    return count


def solve_second(data):
    ranges, _ = extract_data(data)

    count = resolve_overlaps(ranges)

    return count