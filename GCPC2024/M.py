import math
n = int(input())

arr = list(map(int, input().strip().split(" ")))



diff = [] # i - a[i]
min_pos = 2e5 + 1
max_neg = -2e5 - 1
for i in range(n):
    tmp = i - arr[i]
    if tmp > 0:
        min_pos = min(min_pos, tmp)
    elif tmp < 0:
        max_neg = max(max_neg, tmp)
    diff.append(tmp)

s = 0
for d in diff:
    s += d


element1 = math.ceil(s / len(arr))

result = 0
for i in range(len(arr)):
    result += abs(diff[i] - element1)





element1 = math.floor(s / len(arr))

result2 = 0
for i in range(len(arr)):
    result2 += abs(diff[i] - element1)



element1 = sorted(diff)[len(diff) // 2]

result3 = 0
for i in range(len(arr)):
    result3 += abs(diff[i] - element1)

print(min(result, result2, result3))