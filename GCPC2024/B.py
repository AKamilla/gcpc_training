TESTS=["""1 3
10 2 5""", 
"""1 3
10 4 5""", 
"""2 10
10 2 10
2 3 4""",
"""3 1000000000
1000000000 1000000000 1000000000
1000000000 1000000000 1000000000
1000000000 1000000000 1000000000"""]

lines = TESTS[3].split("\n")
n, H = list(map(int, input().split(" ")))
a =[]

for i in range(n):
    l, w, h = list(map(int, input().split(" ")))
    a.append((l, w, h))
def func(a):
    width = 0
    for i in range(n):
        """current = -1
        smallest = min(a[i])
        big = max(a[i])
        middle = list(filter(lambda x: x != big and x != smallest, a[i]))[0]"""
        a[i] = sorted(a[i])
        smallest = a[i][0]
        middle = a[i][1]
        big = a[i][2]
        #print(smallest, middle, big)
        if middle > H and smallest <= H:
            current = smallest
            width += middle
        elif smallest > H:
            return -1
        elif middle<= H or big <= H: 
            width += smallest
    return width
res = func(a)
if res == -1:
    print("impossible")
else:
    print(res)