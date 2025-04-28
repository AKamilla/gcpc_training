import sys

QUERY_SIZE = 1000
STRING_SIZE = 4
ALPHABET = list("abcdefghijklmnopqrstuvwxyz")


def send_query(query, is_answer=False):
    print(f"{'?' if not is_answer else '!'} {query}")
    sys.stdout.flush()
    if not is_answer:
        return input()

# just a paste from wikipedia btw
def de_bruijn(k, n) -> str:
    """de Bruijn sequence for alphabet k
    and subsequences of length n.
    """
    # Two kinds of alphabet input: an integer expands
    # to a list of integers as the alphabet..
    if isinstance(k, int):
        alphabet = list(map(str, range(k)))
    else:
        # While any sort of list becomes used as it is
        alphabet = k
        k = len(k)

    a = [0] * k * n
    sequence = []

    def db(t, p):
        if t > n:
            if n % p == 0:
                sequence.extend(a[1 : p + 1])
        else:
            a[t] = a[t - p]
            db(t + 1, p)
            for j in range(a[t - p] + 1, k):
                a[t] = j
                db(t + 1, t)

    db(1, 1)
    return "".join(alphabet[i] for i in sequence)

def binary_search(seq, l, r):
    while l < r:
        mid = (l + r) // 2

        if send_query(seq[l:mid if mid - l > STRING_SIZE else l + STRING_SIZE]) == "yes":
            if len(seq[l:mid if mid - l > STRING_SIZE else l + STRING_SIZE]) == STRING_SIZE:
                return l
            r = mid + STRING_SIZE - 1
        else:
            l = mid + 1 - STRING_SIZE
        print(f"{l=}, {r=}")

    return l - 1

def solve():
    seq = de_bruijn(ALPHABET, STRING_SIZE)

    for i in range(1, len(seq), QUERY_SIZE - 1):
        if send_query(seq[i - 1:i + QUERY_SIZE - 1]) == "yes":
            start_idx = binary_search(seq, i - 1, i + QUERY_SIZE - 1)
            send_query(seq[start_idx:start_idx+STRING_SIZE], is_answer=True)
            break

solve()
