
def main(d, s, e):
    return s/d * (s-e)/s + 1 - s/d \
            if d - s - e < s \
            else (1 - s/d) * s/(d-s-e)


TESTS = [
    "3 1 1",
    "8 4 2",
    "15 4 2"
]

for test in TESTS:
    d, s, e = map(int, test.split(" "))
    print(main(d, s, e))
