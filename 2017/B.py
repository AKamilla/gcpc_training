import math

TESTS = ["1 3 1", "2 5 2"]

def read_input(s):
    list = map(int, s.split(" "))
    return list


# using the formula for circular permutations with repetition 1/m sum(i = 0; m) k **(gcd(i, m)
def count(n, m, c):
    one_wall_possibilities = c ** (n * n)
    k = one_wall_possibilities
    s = 0
    for i in range(m):
        s += k ** (math.gcd(m, i))
    s //= m
    return s % (10 ** 9 + 7)


if __name__ == '__main__':
    for i in range(2):
        n, m, c = read_input(TESTS[i])
        print(count(n, m, c))


