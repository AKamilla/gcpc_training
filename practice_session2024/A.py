n = int(input())
a = list(map(int, input().split()))
max_el = 0
for i in range(n):
  if a[i] > max_el:
    max_el = a[i]
print(max_el * max_el * max_el) # last element - the biggest product