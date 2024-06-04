import sys

if __name__ == '__main__':
    number = int(input())
    buys = {}
    sells = {}
    b_sum = 0
    for i in range(number):
        string = input()
        list1 = string.split(' ')
        price = float(list1[0])
        buy = int(list1[1])
        if buy != 0:
            buys[price] = buy
        b_sum += buy
        sell = int(list1[2])
        if sell != 0:
            sells[price] = sell


    sells = dict(sorted(sells.items()))
    buys = dict(sorted(buys.items()))
    b_index = 0
    s_index = 0
    s_sum = 0
    max_turnover = 0
    the_price = 0
    if list(buys.keys())[-1] < list(sells.keys())[0]:
        print("impossible")
        sys.exit(0)
    for price, amount in buys.items():
        while s_index < len(sells) and list(sells.keys())[s_index] <= price:
            s_sum += list(sells.values())[s_index]
            s_index += 1
        current_turnover = min(b_sum, s_sum) * price
        if current_turnover > max_turnover:
            max_turnover = current_turnover
            the_price = price
        b_sum -= amount
    print(the_price, max_turnover)





