T = int(input())
for t in range(T) :
    N, Q = map(int, (input().split()))
    list_n = ['0'] * N
    for i in range(Q) :
        L, R = map(int, (input().split()))
        while L <= R :
            list_n[L - 1] = str(i + 1)
            L += 1
    
    print(f'#{t+ 1}', end=' ')
    print(' '.join(list_n))