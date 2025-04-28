import sys


def query(num, is_answer=False):
    sys.stdout.write(f"{'?' if not is_answer else '!' } {num}")
    if not is_answer:
        out = input()
    sys.stdout.flush()
    if not is_answer:
        return out




def binary_search(r, l=0):
    while l < r:
        mid = (l + r) // 2

        # lion is at the start of the steet
        if query(mid) == "lion":    # bound on the right
            l = mid + 1
        else:                       # bound ont he left
            r = mid

    return l - 1


n = int(input())
edge = binary_search(n)
query(edge, is_answer=True)
