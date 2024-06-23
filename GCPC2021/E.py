from time import time
def parse_input(inp: str) -> list:
    lines = inp.strip().split('\n')
    n: int = int(lines[0].split(" ")[0])
    m: int = int(lines[0].split(" ")[1])

    # roads stored as (d, w) on index city on array roads
    roads: list[list[tuple[int, int]]] = [[] for _ in range(n-1)]
    car_weights = []

    for i in range(1, m+1):
        local_line = lines[i].split(" ")
        local_n = int(local_line[0])
        local_d = int(local_line[1])
        local_w = int(local_line[2])
        roads[local_n - 1].append((local_d, local_w))

    n_cars = int(lines[m+1])
    for i in range(m+2, len(lines)):
        car_weights.append(int(lines[i]))

    return [roads, car_weights]

def evaluate_cities(roads: list[list[tuple[int, int]]], cars: list[int]) -> list[int]:
    results = []
    for car in cars:
        local_distance = 0
        for road_list in roads:
            min_d_road = 1e9
            for road in road_list:
                if car <= road[1]:
                    min_d_road = min(min_d_road, road[0])
            local_distance += min_d_road

        results.append(local_distance if local_distance < 1e9 else "impossible")
    return results


TESTS = [
    """2 2
1 100 300
1 1 30
5
400
500
300
20
1""",
    """5 7
1 200 30
2 200 31
3 200 32
4 200 33
1 5000 33
2 5000 33
3 5000 33
3
30
31
33""",
    """2 3
1 3 3
1 4 2
1 2 1
3
1
3
2"""
]

if __name__ == "__main__":
    start = time()
    cities, cars = parse_input(TESTS[2])
    results = evaluate_cities(cities, cars)
    print(f"Time: {time()-start}")
    for result in results:
        print(result)
