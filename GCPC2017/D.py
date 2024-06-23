TESTS = ["""4 5
Mexicans are worse than Americans
Russians are worse than Mexicans
NorthKoreans are worse than Germans
Canadians are worse than Americans
Russians are worse than Americans
Germans are worse than NorthKoreans
NorthKoreans are worse than Mexicans
NorthKoreans are worse than French
Mexicans are worse than Canadians"""]


def read_input(s):
    lines = s.strip().split("\n")
    n, m = list(map(int, lines[0].strip().split(" ")))
    dict_nyt = {}
    dict_trump = {}
    for i in range(n):
        current = lines[i + 1]
        first_country = current[:current.find(" are worse than ")]
        
        second_country = current[current.find(" are worse than ") + 16:]
        dict_nyt[first_country] = second_country



    return n, m, dict_nyt, dict_trump, lines[n + 1:]



def computePaths(adj, n):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                 adj[i][j] = (adj[i][j] | (adj[i][k] and adj[k][j]))
    return adj

if __name__ == '__main__':
    n, m, dict_nyt, dict_trump, trump_lines = read_input(TESTS[0])
    country_map = {}
    i = 1

    for k, v in dict_nyt.items():
        if k not in list(country_map.keys()):
            country_map[k] = i
            i += 1
        if v not in list(country_map.keys()):
            country_map[v] = i
            i += 1
        a = country_map[k]
        b = country_map[v]
    n = len(country_map.keys())
    adj = [[0 for _ in range(n)] for _ in range(n)]
    for k, v in dict_nyt.items():
        a = country_map[k]
        b = country_map[v]
        adj[a - 1][b - 1] = 1
        adj[a - 1][a - 1] = 1
        adj[b - 1][b - 1] = 1
    adj_with_all = computePaths(adj, n)

    for i in range(m):
        line = trump_lines[i]

        first_country = line[:line.find(" are worse than ")]
        second_country = line[line.find(" are worse than ") + 16:]
        if first_country in country_map.keys() and second_country in country_map.keys():
            #print(country_map[first_country] - 1, country_map[second_country] - 1)
            if adj_with_all[country_map[first_country] - 1][country_map[second_country] - 1] == 1:
                print("Fact")
            elif adj_with_all[country_map[second_country] - 1][country_map[first_country] - 1] == 1:
                print("Alternative Fact")
            else:
                print("Pants On Fire")
        else:
            print("Pants On Fire")


