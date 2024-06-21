n, w = list(map(int, input().strip().split(" ")))
words = input()
k = len(words)
for i in range(k//w + 1):
    print(words[i * w:i*w+w])