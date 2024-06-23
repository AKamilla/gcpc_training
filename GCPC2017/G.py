import math

TESTS = ["""4
0 0
0 10
10 10
10 0"""]

def read_input(s):
    lines = s.strip().split("\n")
    n = int(lines[0].strip())
    list_of_coordinates = []
    for i in range(n):
        a, b = list(map(int, lines[i + 1].strip().split(" ")))
        list_of_coordinates.append((a, b))
    return n, list_of_coordinates

def compute_area(coordinate_list, n):
    area = 0.0
    j = n - 1
    for i in range(n):
        area += (coordinate_list[j][0] + coordinate_list[i][0]) * (coordinate_list[j][1] - coordinate_list[i][1])
        j = i
    return int(abs(area / 2.0))


if __name__ == '__main__':
    n, coordinate_list = read_input(TESTS[0])
    area = compute_area(coordinate_list, n)
    r = 0
    for k in range(n):
        r += math.gcd(coordinate_list[(k + 1) % n][0] - coordinate_list[k][0], coordinate_list[(k + 1) % n][1] - coordinate_list[k][1])
    i = area - r / 2 + 1
    print(int(i))




