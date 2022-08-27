def hap(y, N, res, min_res):        # y축 값, 행과 열 갯수, 결과, 최솟값
    if res > min_res[0]:            # 최솟값보다 크면 끊기
        return 0
    else:
        if y == N:                  # 모두 다 돌았을 때
            if res < min_res[0]:    # 최솟값 최신화
                min_res[0] = res
        else:
            for x in range(N):
                if visited[x] == 0: # 방문하지 않은 곳이면
                    visited[x] = 1  # 방문했다고 체크하고
                    hap(y + 1, N, res + field[y][x], min_res)
                    visited[x] = 0  # 다른 가짓수를 위해 초기화


T = int(input())

for t in range(T):
    N = int(input())
    field = [list(map(int, input().split())) for _ in range(N)]
    
    min_res = [10 * N]              # 최솟값 선언
    for i in range(N):
        visited = [0] * N
        res = field[0][i]
        visited[i] = 1              # i 값 먼저 체크
        hap(1, N, res, min_res)     # 부분합 돌리기
        

    print(f'#{t + 1} {min_res[0]}')