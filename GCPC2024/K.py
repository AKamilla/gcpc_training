TESTS = ["""bbq
h""",
"""bbq
v""",
"""bbq
r""",
"""ppbddbq
hvrhv"""]

dict_h = {
    'b': 'd',
    'd': 'b',
    'q': 'p',
    'p': 'q'
}

dict_v = {
    'b': 'p',
    'd': 'q',
    'q': 'd',
    'p': 'b'
}


def do_h(s):
    res = str(s)
    res = res[::-1]
    res = list(res)
    for i, c in enumerate(res):
        res[i] = dict_h[c]
    empty = ""
    res = empty.join(res)
    return res

def do_v(s):
    res = str(s)
    res = list(res)
    for i, c in enumerate(res):
        res[i] = dict_v[c]
    empty = ""
    res = empty.join(res)
    return res

lines = TESTS[3].split("\n")
word = input()
operations = input()

v = 0
h = 0

for c in operations:
    if c == 'v':
        v += 1
    elif c == 'r':
        v += 1
        h += 1
    else:
        h += 1

if h % 2 == 1:
    word = do_h(word)
if v % 2 == 1:
    word = do_v(word)
print(word)