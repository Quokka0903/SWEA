def bfs(s, N):
    visited = [[0] * N for _ in range(N)]
    q = []
    q.append(s)
    visited[s[0]][s[1]] = 1                     # 시작점 visited에 표시

    while q:
        s = q.pop(0)                            # q 맨 앞의 좌표값(튜플) 팝
        for i, j in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            if s[0] + i >= N or s[1] + j >= N or s[0] + i < 0 or s[1] + j < 0:
                continue                        # 델타 이동값이 미로 밖이면 컨티뉴
            
            if miro[s[0] + i][s[1] + j] != '1' and visited[s[0] + i][s[1] + j] == 0:
                q.append((s[0] + i, s[1] + j))  # 델타 이동값이 벽이 아니고 방문하지 않은 곳이면                                                
                visited[s[0] + i][s[1] + j] = visited[s[0]][s[1]] + 1
                                                # 좌표 q에 넣고 이동거리 +1 해서 visited에 할당

            if miro[s[0] + i][s[1] + j] == '3': # 델타 이동값이 도착이면
                return visited[s[0]][s[1]] - 1  # 이동거리 리턴

    return 0                                    # 모든 탐색에도 못갔다? 0 리턴

T = int(input())

for t in range(T):
    N = int(input())
    miro = [input() for _ in range(N)]  # 미로 만들기

    s = ()
    for y in range(N):
        for x in range(N):
            if miro[y][x] == '2':
                s = (y, x)              # 시작위치 좌표 지정

    print(f'#{t + 1} {bfs(s, N)}')      # 결과값 출력