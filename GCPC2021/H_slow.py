
def permutation(current, stack1, stack2):
    if current in stack1:
        position = stack1.index(current)
        stack2 = stack2 + list(reversed(stack1[position + 1:]))
        stack1 = stack1[:position]
    elif current in stack2:
        position = stack2.index(current)
        stack1 = stack1 + list(reversed(stack2[position + 1:]))
        stack2 = stack2[:position]
    return stack1, stack2




if __name__ == '__main__':
    list1 = list(map(int, input().split(' ')))
    n = list1[0]
    stack1 = list(map(int, input().split(' ')))
    stack2 = list(map(int, input().split(' ')))

    opportunities = 0
    for i in range(1, n + 1):
        stack1, stack2 = permutation(i, stack1, stack2)
        if (stack1 and stack1[-1] == 0) or (stack2 and stack2[-1] == 0):
            opportunities += 1

    print(opportunities)

