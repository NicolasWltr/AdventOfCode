def parse_coords(data):
    lines = data.split('\n')

    coords = []

    for line in lines:
        if not line.strip():
            continue
        coords.append(tuple(map(int, line.split(','))))

    return coords

def gen_pairs(coords):
    all_coords = []

    for x in range(len(coords)):
        for y in range(x+1, len(coords)):
            first = coords[x]
            second = coords[y]

            x1, y1 = first
            x2, y2 = second

            area = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)

            all_coords.append((area, first, second))

    all_coords = sorted(all_coords, key=lambda x: x[0])

    return all_coords

def solve_first(data):
    coords = parse_coords(data)

    pairs = gen_pairs(coords)

    pairs = sorted(pairs, key=lambda x: x[0])

    greatest = pairs[-1]

    area, _, _ = greatest

    return area

def is_inside(coords, first_corner, second_corner, thrid_corner, fourth_corner):
    return False

def solve_second(data):
    coords = parse_coords(data)

    pairs = gen_pairs(coords)

    pairs = sorted(pairs, key=lambda x: x[0])

    for pair in reversed(pairs):
        area, first, second = pair

        x1, y1 = first
        x2, y2 = second

        first_corner = first
        second_corner = second
        thrid_corner = (x1, y2)
        fourth_corner = (x2, y1)

        if is_inside(coords, first_corner, second_corner, thrid_corner, fourth_corner):
            return area