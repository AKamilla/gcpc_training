TESTS = ["""4 
4 4 1
1 2
2 3
3 4
4 1
1 2
2 1
5 4 
3 3""",
"""6
4 4 1
1 2
2 3
3 4
4 1
1 2
2 1
5 4
3 3"""]

def read_input(s):
    cost_array = []
    time_array = []
    lines = s.strip().split('\n')
    T = int(lines[0])
    n, m, path_time = list(map(int, lines[1].split(" ")))
    adj = [[i - 1] for i in range(1, n + 2)]
    number = 2
    for i in range(m):
        a, b = list(map(int, lines[number].strip().split(" ")))
        adj[a].append(b)
        adj[b].append(a)
        number += 1
    for i in range(n):
        t, c = list(map(int, lines[number].strip().split(" ")))
        number += 1
        cost_array.append(c)
        time_array.append(t)
    return n, m, T, path_time, cost_array, time_array, adj

def recursion(T, path_time, cost_array, time_array, current_time, current_cost, current_vertex, adj): # count min_cost till vertex 1
    #print(current_vertex, current_time, current_cost)
    if current_vertex == 1 and current_cost != 0:
        if time_array[current_vertex - 1] + current_time == T:
            return current_cost + cost_array[current_vertex - 1]
    min_cost = 1e7
    current_time += time_array[current_vertex - 1]
    current_cost += cost_array[current_vertex - 1]
    if current_time >= T:
        return -1
    for i, next_vertex in enumerate(adj[current_vertex]):
        if next_vertex != current_vertex:
            c = path_time + current_time
        else:
            c = current_time
        if current_time + time_array[next_vertex - 1] > T:
            continue
        m = recursion(T, path_time, cost_array, time_array, c, current_cost, next_vertex, adj)
        if m != -1 and m < min_cost:
            min_cost = m
    if min_cost == 1e7:
        min_cost == -1
    return min_cost






if __name__ == '__main__':
    for i in range(2):
        n, m, T, path_time, cost_array, time_array, adj = read_input(TESTS[i])
        #print(n, m, T, path_time, cost_array, time_array, adj)
        print(recursion(T, path_time, cost_array, time_array, 0, 0, 1, adj))






