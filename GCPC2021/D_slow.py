
def number_mistakes(number, encrypted, decrypted):
    shifts = [0] * number
    for i, c in enumerate(decrypted):
        shifts[i] = (ord(decrypted[i]) - ord(encrypted[i]) + 26) % 26

    counts = dict.fromkeys(shifts, 0)
    #print(shifts)
    for num in shifts:
        counts[num] += 1

    return number - max(list(counts.values()))



if __name__ == '__main__':
    number = int(input())
    encrypted = input()
    decrypted = input()
    min_number_mistakes = 1e1000
    for i in range(number):
        #print(encrypted[i:] + encrypted[:i])
        k = number_mistakes(number, encrypted[i:] + encrypted[:i], decrypted)
        #print(k)
        if k < min_number_mistakes:
            min_number_mistakes = k
    print(min_number_mistakes)



