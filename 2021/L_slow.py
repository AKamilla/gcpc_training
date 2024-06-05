from functools import cache
from time import time


def next(x:int, y:int, c:chr):
    for i in range(x, len(matrix[0])):
        if matrix[y][i] == c:
            return i - x
    return 1e1000


def area(x:int, y:int, h:int) -> int:
    area = 1e1000
    for c_h in range(1, h - y + 1): #O(w * h * h)
        max_c = 0
        for c in "WALDO": #O(5 * w * h)
            min_h = 1e1000
            for k in range(0, c_h): #O(w * h)
                n = next(x, y + k, c) # O(w)
                if n < min_h:
                    min_h = n
            if min_h > max_c:
                max_c = min_h

        c_w = max_c + 1

        if c_h * c_w < area:
            area = c_h * c_w
    return area

TESTS = [
    """5 5
ABCDE
FGHIJ
KLMNO
PQRST
VWXYZ""",
    """5 10
ABCDEABCDE
FGHIJFGHIJ
KLMNOKLMNO
PQRSTPQRST
VWXYZVWXYZ""",
    """5 10
WAALDLODOW
AWWLAOODOW
LOLADOWALO
ADALLLWWOL
WWOOAAAALO""",
    """2 3
WAL
TER"""
]


def read_input(s:str):
    lines = s.strip().split('\n')
    list1 = list(map(int, lines[0].split(' ')))
    h = list1[0]
    w = list1[1]
    matrix = [[] * w] * h
    for i in range(1, h + 1):
        matrix[i - 1] = list(lines[i])
    return h, w, matrix


if __name__ == '__main__':

    for i in range(len(TESTS)):
        h, w, matrix = read_input(TESTS[i])
        min_area = 1e1000
        start = time()
        for x in range(w):
            for y in range(h):
                a = area(x, y, h)
                if a < min_area:
                    min_area = a
        end = time()
        print(f"Test {i + 1} took {end - start} s")
        if min_area >= 1e1000:
            print("impossible")
        else:
            print(min_area)
