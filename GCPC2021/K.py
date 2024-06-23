

def read_input(s:str):
    lines = s.strip().split('\n')
    list1 = lines[0].split(' ')
    n = int(list1[0])
    m = int(list1[1])
    p = int(list1[2])
    adj = [[] for i in range(n + 1)]
    for i in range(m):
        list2 = lines[i + 1].split(' ')
        u = int(list2[0])
        v = int(list2[1])
        adj[v].append(u)
        adj[u].append(v)
    return n, m, p, adj


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
    """100 0 13"""
]


def isBipartite(adj, v, visited, color):
    for u in adj[v]:

        # If vertex u is not explored before
        if (visited[u] == False):

            # Mark present vertices as visited
            visited[u] = True

            # Mark its color opposite to its parent
            color[u] = not color[v]

            # If the subtree rooted at vertex v
            # is not bipartite
            if (not isBipartite(adj, u,
                                visited, color)):
                return False

        # If two adjacent are colored with
        # same color then the graph is not
        # bipartite
        elif (color[u] == color[v]):
            return False
    return True


def graph(n, m, adj):
    visited = [0 for i in range(n + 1)]
    color = [0 for i in range(n + 1)]
    comp_number = 0
    possible = True
    for i in range(1, n + 1):
        if not visited[i]:
            comp_number += 1
            possible = possible and isBipartite(adj, i, visited, color)
    return possible, comp_number

if __name__ == '__main__':
    for i in range(4):
        n, m, p, adj = read_input(TESTS[i])
        possible, comp_number = graph(n, m, adj)
        if possible:
            print((2 ** (comp_number - 1) + 1) % p)
        else:
            print("impossible")