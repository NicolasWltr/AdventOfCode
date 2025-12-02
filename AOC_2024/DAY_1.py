def get_sorted_lists(data):
    lines = data.split("\n")

    lefts = []
    rights = []

    for line in lines:
        if not line.strip():
            continue

        left, right = map(int, line.split())

        lefts.append(left)
        rights.append(right)

    lefts.sort()
    rights.sort()

    return lefts, rights

def solve_first(data: str):
    distance = 0

    left, right = get_sorted_lists(data)

    while len(right) > 0 and len(left) > 0:
        r = right.pop()
        l = left.pop()

        dist = abs(r-l)
        distance += dist

    return distance


def solve_second(data):
    similarity = 0

    left, right = get_sorted_lists(data)

    for item in left:
        count_in_right = 0
        for searched in right:
            if item == searched:
                count_in_right += 1
        similarity += count_in_right * item

    return similarity

