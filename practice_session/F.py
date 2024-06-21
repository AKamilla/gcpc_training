from collections import deque

TESTS = ["""6 2
7 2 1 5 3 6
""",
"""2 5
1 7""",
"""7 3
1 9 5 4 5 15 7"""]
lines = TESTS[0].split("\n")
n, m = list(map(int, lines[0].strip().split(" ")))
a = list(map(int, lines[1].strip().split(" ")))

d = deque()
obtained_max = 0
for i in range(n):
    while d and d[0][1] < i - m:
        d.popleft()
    if d:
        current_min = d.popleft()
        if a[i] - current_min[0] > obtained_max:
            obtained_max = a[i] - current_min[0]
        d.appendleft(current_min)
    if d:
        while d and d[-1][0] > a[i]:
            d.pop()
    d.append((a[i], i))
print(obtained_max)
