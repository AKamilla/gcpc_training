
w = input().lower()

print("yes" if all(y <= x for x, y in zip(w, w[1:])) or all(y >= x for x, y in zip(w, w[1:])) else "no")
