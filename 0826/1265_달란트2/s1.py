for t in range(int(input())):
    N, P = map(int, input().split())
    
    print(f'#{t + 1}', end=' ')

    ans = 1
    if N % P == 0:
        ans *= (N//P) ** P
    
    else:
        res = [N // P for _ in range(P)]
        num = N % P
        
        for i in range(num):
            res[i] += 1

        for a in res:
            ans *= a

    print(ans)