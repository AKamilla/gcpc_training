
TESTS = ["""5 2000 3
John 999
Lyndon 450
Richard 1234
Gerald 1001
Jimmy 300""",
"""3 5555 2
Ronald 1000
George 2000
Bill 3000"""]


def read_input(s):
    lines = s.strip().split("\n")
    n, d, k = list(map(int, lines[0].strip().split(" ")))
    people = {}
    for i in range(n):
        name, pay = lines[1 + i].strip().split(" ")
        people[name] = int(pay)
    people = dict(sorted(people.items(), key=lambda x: -x[1]))
    return n, d, k, people

if __name__ == '__main__':
    for i in range(2):
        n, d, k, people = read_input(TESTS[i])
        sum = 0
        fired = []
        number = 0
        for key, v in people.items():
            sum += v
            number += 1
            if sum >= d and number <= k: # last valid person
                fired.append(key)
                break
            if sum >= d and number > k:
                number = -1
                break
            fired.append(key)
        if number == -1:
            print("impossible")
        else:
            print(number)
            for i in range(number):
                print(fired[i] +  ", YOU ARE FIRED!")




