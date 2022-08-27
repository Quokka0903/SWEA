def indexing(n):
    n = int(n)
    if n % 2 == 0:
        return n // 2 - 1
    else:
        return n // 2


T = int(input())

for t in range(T):
    ans = 0
    cor = [0] * 200
    N = int(input())
    for i in range(N):
        here, togo = map(indexing, input().split())
        if here > togo:
            here, togo = togo, here
        for j in range(here, togo + 1):
            cor[j] += 1

    for k in range(200):
        if ans < cor[k]:
            ans = cor[k]
    print(f'#{t + 1} {ans}')