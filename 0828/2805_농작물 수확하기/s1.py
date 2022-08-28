for t in range(int(input())):
    N = int(input())
    bat = [input() for _ in range(N)]
    
    ans = 0
    for i in range(N):
        ans += int(bat[N//2][i])
    
    for j in range(1, N//2 + 1):
        for k in range(j, N - j):
            ans += int(bat[N//2 - j][k])
            ans += int(bat[N//2 + j][k])

    print(f'#{t + 1} {ans}')