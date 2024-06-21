import math

n, v = list(map(int, input().strip().split(" ")))
optimal_volume = 10e9
index = -1
for i in range(n):
    h, r = list(map(int, input().strip().split(" ")))
    volume = math.pi * (r ** 2) * h
    if volume >= v and volume <= optimal_volume:
        index = i + 1
        optimal_volume = volume
if index == -1:
    print("impossible")
else:
    print(index)

