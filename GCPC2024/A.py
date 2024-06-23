TESTS = ["""5 3
1 2
2 3
4 5""",
"""3 0""",
"""8 8
1 2
2 3
3 4 
1 4
1 5
2 6
3 7
4 8"""]



def component_size(i, visited, adj):
    size = 1
    visited[i] = 1
    for neighbor in adj[i]:
        if not visited[neighbor]:
            size += component_size(neighbor, visited, adj)
    return size


import sys
sys.setrecursionlimit(200001)

lines = TESTS[2].split("\n")

n, m = list(map(int, input().strip().split(" ")))

adj = [[] for i in range(n)]

for i in range(m):
    a, b = list(map(int, input().strip().split(" ")))
    adj[a - 1].append(b - 1)
    adj[b - 1].append(a - 1)

visited = [0 for i in range(n)]

max_size = 0
for i in range(n):
    if not visited[i]:
        max_size = max(max_size, component_size(i, visited, adj))
print(max_size)