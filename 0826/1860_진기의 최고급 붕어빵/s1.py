for t in range(int(input())):
    N, M, K = map(int, input().split())
    person = list(map(int, input().split()))
    
    dic_a = {}
    for i in person:
        if i not in dic_a:
            dic_a[i] = 1
        else:
            dic_a[i] += 1

    flag = 0
    bungbbang = 0
    for time in range(11112):
        if time > 0 and time % M == 0:
            bungbbang += K
        if time not in dic_a:
            continue
        else:
            bungbbang -= dic_a[time]
            if bungbbang < 0:
                flag = 1
                break

    print(f'#{t + 1}', end=' ')
    if flag:
        print('Impossible')
    else:
        print('Possible')
