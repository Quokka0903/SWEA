for t in range(int(input())):
    N = int(input())
    n_list = list(map(int, input().split()))
    n_gob = []
    for a in range(N):
        for b in range(a + 1, N):
            n_gob.append(n_list[a] * n_list[b])
    res = -1
    for unit in n_gob:
        chk = str(unit)
        flag = 1
        for j in range(1, len(chk)):
            if chk[j - 1] > chk[j]:
                flag = 0
                break
        if flag:
            if res < unit:
                res = unit

    print(f'#{t + 1} {res}')