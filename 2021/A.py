
def is_possible(n) -> bool:
    return (n - 1).bit_count() in [2, 1] and n & 0b1 == 0b1


def first_choice(n) -> int:
    return int(f'1{bin(n-1)[2:].split("1")[-1]}', 2) + 1


if __name__ == "__main__":
    while True:
        n = int(input())
        if n == 0:
            break
        if is_possible(n):
            print(f"{first_choice(n)}")
        else:
            print("impossible")
