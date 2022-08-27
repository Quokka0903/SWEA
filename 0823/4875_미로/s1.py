dy = [0, 0, 1, -1]          # 델타값 설정
dx = [1, -1, 0, 0]

def gazua(y, x):
    flag = 0
    visited[y][x] = 1       # 현재 위치 visited 추가
    for d in range(4):      # 델타 탐색
        if y + dy[d] >= 0 and y + dy[d] < N and x + dx[d] >= 0 and x + dx[d] < N:
            if miro[y + dy[d]][x + dx[d]] == '3':
                return 1    # 찾았으면 1 리턴
            elif miro[y + dy[d]][x + dx[d]] == '0':
                if visited[y + dy[d]][x + dx[d]] == 0: # 안가본 길로 재귀
                    if gazua(y + dy[d], x + dx[d]):    # 보낸 값이 1이면
                        return 1                       # 얘도 1 리턴
    return flag             # 못찾았으면 0이지


T = int(input())

for t in range(T):
    N = int(input())
    miro = [list(input()) for _ in range(N)]
    
    idx_y = N
    idx_x = N
    for i in range(N):
        for j in range(N):  # 시작지점 찾기
            if miro[i][j] == '2':
                idx_y = i
                idx_x = j
                break    

    visited = [[0] * N for _ in range(N)]

    if idx_y == N or idx_x == N:
        res = 'error'       # 출발지점 없으면 에러
    else :                  # 있으면 미로 탐색
        res = gazua(idx_y, idx_x)
    print(f'#{t + 1} {res}')