def my_len(list_in):
    res = 0
    for _ in list_in:
        res += 1
    return res


T = int(input())

for t in range(T):
    days = int(input())
    price = list(map(int, input().split()))

    leng = my_len(price)

    sum_ik = 0
    day = leng - 1
    high = leng - 1

    while day != 0:
        if price[day] > price[high]:
            for i in range(day + 1, high):
                sum_ik += price[high] - price[i]
            high = day
        day -= 1

        if day == 0 :
            for i in range(day, high):
                if price[high] - price[i] > 0:
                    sum_ik += price[high] - price[i]


    print(f'#{t + 1} {sum_ik}')