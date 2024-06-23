TESTS = ["""3 6 8
1 1
1 2 
1 3
2 3
2 4
3 4
3 5
3 6""",
"""4 5 11
1 1
1 2
1 3
2 1 
2 2 
2 3
3 1 
3 2 
3 3
4 4
4 5""",
"""3 5 7
1 1
1 2
2 2 
2 3
2 4
3 4
3 5"""]

def read_input(s):
    lines = s.strip().split('\n')
    m, n, k = list(map(int, lines[0].strip().split(" ")))
    adj = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(1, k + 1):
        a, b = list(map(int, lines[i].strip().split(" ")))
        adj[a - 1][b - 1] = 1 # a is the socket
    return m, n, k, adj


def bmp(u, matchR, seen, adj):
    for v in range(n):
        if adj[u][v] and seen[v] == False:
            seen[v] = True
            if matchR[v] == -1 or bmp(matchR[v], matchR, seen, adj):
                matchR[v] = u
                return True
    return False

def max_matching(n, m, adj):
    matchR = [-1] * n
    result = 0
    for i in range(m):
        seen = [False] * n
        if bmp(i, matchR, seen, adj):
            result += 1
    return result


if __name__ == '__main__':
    for i in range(3):
        m, n, k, adj = read_input(TESTS[2])

        max_len = 0
        index = -1
        for i in range(m):
            if sum(adj[i]) > max_len:
                max_len = sum(adj[i])
                index = i
        max_m = 0
        for i in range(m):
            adj_c = adj.copy()
            adj_c.append(adj[i].copy())
            adj_c.append(adj[i].copy())
            mm = max_matching(n, m + 2, adj_c)
            if mm > max_m:
                max_m = mm

        print(max_m)

