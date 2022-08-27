def my_len(x):
    res = 0
    for i in x:
        res += 1
    return res


T = int(input())

for t in range(T):
    sero = ['' for _ in range(15)]
    for i in range(5):
        list_garo = input()
        for j in range(15):
            sero[j] += (list_garo[j])
            if j == my_len(list_garo) - 1:
                break

    print(f'#{t + 1}', end=' ')
    for k in range(15):
        print(sero[k], end='')
    print()