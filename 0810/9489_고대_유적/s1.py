T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max = 0
 
    for i in range(N):
        cnt = 0
        for j in range(M):
            if arr[i][j] == 1:
                cnt += 1
                if cnt > max:
                    max = cnt
            else:
                cnt = 0
 
    for j in range(M):
        cnt = 0
        for i in range(N):
            if arr[i][j] == 1:
                cnt += 1
                if cnt > max:
                    max = cnt
            else:
                cnt = 0
 
    print(f"#{t} {max}")