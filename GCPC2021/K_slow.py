import math


def comb(n: int, k: int) -> int:
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))


def combinations(people: list[int], k: int) -> list[list[int]]:
    if k == 1:
        return [[person] for person in people]

    combs = []
    for i, person in enumerate(people):
        combs += [[person] + comb for comb in combinations(people[i+1:], k-1)]

    return combs


def n_friendly_groups(n: int) -> int:
    return sum([comb(n, k) for k in range(math.ceil(n / 2))])


def is_possible(local_combination: list[int], dislikes: list[tuple[int, ...]]) -> bool:
    for d1, d2 in dislikes:
        if d1 in local_combination and d2 in local_combination or d1 not in local_combination and d2 not in local_combination:
            return False
    return True

def main(n: int, m: int, p: int, dislikes: list[tuple[int, ...]]) -> int:
    people = set()
    for p1, p2 in dislikes:
        people.add(p1)
        people.add(p2)

    people_comb = []
    for k in range(n+1):
        people_comb += combinations(list(people), k)

    people_comb = [comb for comb in people_comb if is_possible(comb, dislikes)]

    friendly_groups = n_friendly_groups(n - len(people))
    out = math.ceil(len(people_comb) / 2) * (friendly_groups + 1)
    return (out + 1) % p if out != 0 \
        else "impossible" if friendly_groups == 0 \
        else (friendly_groups + 1) % p


def read_input(inp: str):
    lines = inp.strip().split('\n')
    n, m, p = map(int, lines[0].split(" "))
    dislikes: list[tuple[int, ...]] = []
    for line in lines[1:]:
        dislikes.append(tuple(map(int, line.split(" "))))

    return [n, m, p, dislikes]



TESTS = [
"""4 2 11
1 2
3 4""",
    """5 2 3
1 2
3 4""",
    """3 3 11
1 2
2 3
3 1""",
    """100 0 13""",
]

if __name__ == "__main__":
    n, m, p, dislikes = read_input(TESTS[0])
    print(n, m, p, dislikes)
    print(main(n, m, p, dislikes))
