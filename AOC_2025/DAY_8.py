import math

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

            x1, y1, z1 = first
            x2, y2, z2 = second

            distance2 = (x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2

            all_coords.append((distance2, first, second))

    all_coords = sorted(all_coords, key=lambda x: x[0])

    return all_coords

def make_cluster(data, limit=True):
    coords = parse_coords(data)

    pairs = gen_pairs(coords)

    added = []

    junctions = []

    lastConnected = None

    pairs = pairs[:1000] if limit else pairs

    for pair in pairs:
        _, first, second = pair

        if len(junctions) == 1 and len(junctions[0]) == len(coords):
            break

        lastConnected = pair

        if first in added and second in added:
            cluster_first = -1
            cluster_second = -1

            for index, junc in enumerate(junctions):
                if first in junc:
                    cluster_first = index
                if second in junc:
                    cluster_second = index

            if cluster_first != -1 and cluster_second != -1 and cluster_first != cluster_second:
                junctions[cluster_first] += junctions[cluster_second]

                junctions.pop(cluster_second)

        elif first in added:
            added.append(second)
            for junc in junctions:
                if first in junc:
                    junc.append(second)    
        elif second in added:
            added.append(first)
            for junc in junctions:
                if second in junc:
                    junc.append(first)
        else:
            added.append(first)
            added.append(second)
            junctions.append([first, second])

    junctions = sorted(junctions, key=lambda x: len(x), reverse=True)

    if limit:
        return len(junctions[0]) * len(junctions[1]) * len(junctions[2])
    else:
        return lastConnected

def solve_first(data):
    return make_cluster(data)

def solve_second(data):
    lastConnected = make_cluster(data, False)

    _, first, second = lastConnected

    x1, _, _ = first
    x2, _, _ = second

    return x1 * x2