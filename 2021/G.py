
def read_input(inp: str):
    lines = inp.strip().split('\n')
    n: int = int(lines[0].split(" ")[0])
    m: int = int(lines[0].split(" ")[1])
    color_coords = []
    for y in range(n):
        for x in range(m):
            if lines[y+1][x] != "_":
                color_coords.append((x, y))

    return [n, m, color_coords]


def is_possible(coord1, coord2) -> bool:
    x1, y1 = coord1
    x2, y2 = coord2
    return (x1 <= x2 and y1 <= y2) or (x1 >= x2 and y1 >= y2)


def evaluate_for_multiple_buckets(multiple_buckets, buckets):
    for x, y in multiple_buckets:
        possible_buckets = []
        for i, bucket in enumerate(buckets):
            last_element = bucket[-1]
            if is_possible(last_element, (x, y)):
                possible_buckets.append(i)

        # Only one bucket is possible
        if len(possible_buckets) == 1:
            buckets[possible_buckets[0]].append((x, y))
            multiple_buckets.remove((x, y))

    return multiple_buckets, buckets


TESTS = [
    """4 4
__C_
C_C_
_C_C
_CCC""",
    """4 6
CC____
_CCC__
___C_C
C__CCC""",
    """3 5
CC__C
_C_CC
CCCCC"""
]

if __name__ == "__main__":
    n, m, color_coords = read_input(TESTS[2])
    print(n, m, color_coords)

    buckets: list[list[tuple[int, int]]] = [[color_coords[0]]]
    multiple_buckets = []
    for x, y in color_coords[1:]:
        possible_buckets = []
        for i, bucket in enumerate(buckets):
            last_element = bucket[-1]
            if is_possible(last_element, (x, y)):
                possible_buckets.append(i)

        # No buckets are possible
        if len(possible_buckets) == 0:
            buckets.append([(x, y)])

        # Only one bucket is possible
        elif len(possible_buckets) == 1:
            buckets[possible_buckets[0]].append((x, y))
            multiple_buckets, buckets = evaluate_for_multiple_buckets(multiple_buckets, buckets)

        # Multiple buckets are possible
        else:
            multiple_buckets.append((x, y))

    print(len(buckets))
