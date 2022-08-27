def snail (N) :
    list_snail = [[0] * N for _ in range(N)]
    leng = N
    stack = 0
    cnt = 0
    direction = 0
    i, j = 0, 0

    for num in range(N**2) :
        if (num + 1) - stack == 4 * leng - 4 :
            leng -= 2
            stack = num + 1
            cnt += 1
        list_snail[i][j] = str(num + 1)
        if direction == 0 :
            if j == N - cnt - 1 :
                direction = 1
                i += 1
                continue
            j += 1
        elif direction == 1 :
            if i == N - cnt - 1 :
                direction = 2
                j -= 1
                continue
            i += 1
        elif direction == 2 :
            if j == 0 + cnt :
                direction = 3
                i -= 1
                continue
            j -= 1
        elif direction == 3 :
            if i == 0 + cnt :
                direction = 0
                j += 1
                continue
            i -= 1
            
    return list_snail

T = int(input())
for t in range(T) :
    N = int(input())
    ans = snail(N)
    
    print(f'#{t+1}')
    for i in range(N) :
        print(' '.join(ans[i]))
