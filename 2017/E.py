TESTS = ["""2 2
1 2 0.5
2 1 2.3""",
         """2 2
1 2 0.5
2 1 0.7"""]

def dfs(graph, start, end):
    fringe = [(start, [])]
    while fringe:
        state, path = fringe.pop()
        if path and state == end:
            yield path
            continue
        for next_state in graph[state]:
            if next_state in path:
                continue
            fringe.append((next_state, path+[next_state]))


def read_input(inp):
    inp = inp.strip().split("\n")
    n, m = list(map(int, inp[0].strip().split(" ")))
    edges = [list(map(float, inp[i].strip().split(" "))) for i in range(1, len(inp))]
    edges = [[int(line[0]), int(line[1])] + [line[2]] for line in edges]
    return n, m, edges


def is_admissible_cycle(cycle, edges):
    out = 1
    for i in range(len(cycle) - 1):
        node_from = cycle[i]
        node_to = cycle[i + 1]
        for edge in edges:
            if edge[0] == node_from and edge[1] == node_to:
                out *= edge[2]
                break
    return out <= 0.9

if __name__ == "__main__":
    n, m, edges = read_input(TESTS[1])
    graph = {}
    for x in edges:
        graph[x[0]] = []
    for edge in edges:
        graph[edge[0]].append(edge[1])

    cycles = [[node] + path for node in graph for path in dfs(graph, node, node)]

    print(all(is_admissible_cycle(cycle, edges) for cycle in cycles))



