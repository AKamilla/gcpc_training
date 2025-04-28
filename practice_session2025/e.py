import random
import time
from itertools import combinations_with_replacement


def solve():
    def eval_pair(t1, t2):
        max_dimension = t1[1] if t1[1] > t2[1] else t2[1]
        min_dimension = t1[0] if t1[0] < t2[0] else t2[0]
        return max_dimension * min_dimension ** 2

    out = 0
    for t1, t2 in combinations_with_replacement(c, 2):
        out = max(out, eval_pair(t1, t2))
    return out


def filter_pairs(c):
    out = []
    for min_dim, max_dim in c:
        if not any([min_dim < min_dim2 and max_dim < max_dim2 for min_dim2, max_dim2 in c]):
            out.append((min_dim, max_dim))

    return out


def solve_v2(c):
    out = 0

    for i in range(len(c)):
        for j in range(i, len(c)):
            out = max(
                out,
                c[i][1] * min(c[i][0], c[j][0]) ** 2
            )

    return out


n = int(input())
c = list(map(
    lambda x: ((x[0], x[1]) if x[1] > x[0] else (x[1], x[0])),
    [list(map(
        int,
        input().split(" "))) for _ in range(n)
    ])
)

print(solve_v2(filter_pairs(c)))

"""
def generate_pairs(n=int(1e4)):
    out = []
    for i in range(n):
        min_dim = random.randint(1, 1000)
        out.append((min_dim, random.randint(min_dim, 2000)))
    return out

c = generate_pairs()

start = time.time()
out1 = solve()
end = time.time()
print(f"v1: {end - start}s, {out1=}")

start = time.time()
out2 = solve_v2(c)
end = time.time()
print(f"v2: {end - start}s, {out2=}")

start = time.time()
out3 = solve_v2(filter_pairs(c))
end = time.time()
print(f"v3: {end - start}s, {out3=}")

# v1: 11.597122192382812s, out1=1988000000
# v2: 14.129420757293701s, out2=1988000000
# v3: 3.031428098678589s, out3=1988000000
"""