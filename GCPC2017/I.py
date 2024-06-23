
TESTS = ["""4 2
1 1 1 1""",
"""9 3
1 1 2 2 3 2 3 2 1
""",
         """1 2
1 1 10 15 1"""
         ]

def read_input(inp):
    inp = inp.split("\n")
    n, m = list(map(int, inp[0].strip().split(" ")))
    opponents = list(map(int, inp[1].strip().split(" ")))
    return n, m, opponents

def get_possible_array_rest(arr, i, m):
    return arr[i + m:]

def solve(n, m, opponents):
    for i in range(len(opponents) - 1, -1 + m, -1):
        max_possible = get_possible_array_rest(opponents, i, m)
        if not max_possible:
            max_possible = 0
        else:
            max_possible = max(max_possible)
        opponents[i] = opponents[i] + max_possible
    return max(opponents)


if __name__ == "__main__":
    print(solve(*read_input(TESTS[2])))