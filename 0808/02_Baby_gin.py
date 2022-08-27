T = int(input())

for t in range(T) :
    gin = input()
    num = [0] * 10
    for i in range(6) :
        num[int(gin[i])] += 1

    flag = 0
    for j in range(10) :
        if num[j] >= 3 :
            flag += num[j] // 3
            num[j] = num[j] % 3

    for k in range(2, 10) :
        if num[k] > 0 and num[k-1] > 0 and num[k-2] > 0 :
            min = (num[k] if num[k] < num[k-1] else num[k-1])
            min = (min if min < num[k-2] else num[k-2])

            flag += min
            num[k] -= min
            num[k-1] -= min
            num[k-2] -= min

    print(f'#{t+1}', end=' ')
    if flag == 2 :
        print (1)
    else :
        print (0)