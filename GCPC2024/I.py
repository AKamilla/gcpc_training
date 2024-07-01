
TESTS =["""4 10
! 2 7 1
? 9
? 7 
? 6""", 
"""7 10
! 2 6 1
! 3 8 2
! 5 2 3
? 6
! 5 5 4
? 8
? 9""", 
"""6 12
! 1 6 1
? 6
! 5 7 4
? 6
! 6 3 2
? 6""",
"""6 12
! 1 7 1
! 7 3 2
? 6
? 7
? 8
? 10"""
]

def calc(wave, x):
    dict = {0:1, 1:0, 2:-1, 3:0}
    p, l, a = wave
    l -= 1
    if x < p or x > p + l:
        return 0
    else:
        return a * dict[(x - p) % 4]


lines = TESTS[-1].split("\n")
#n, w = map(int, lines[0].split(" "))
n, w = map(int, input().split(" "))
waves =[]

for i in range(n):
    line = input()
    if line[0] == "!":
        p, l, a = map(int, line[1:].strip().split(" "))
        waves.append((p, l, a))
    else:
        p = int(line[2:].strip())
        sum = 0
        for i in range(len(waves)):
            #print(f"{i}: p={p} {calc(waves[i], p)}")
            sum += calc(waves[i], p)
        print(sum)
