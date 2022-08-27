T = int(input())

for t in range(T):
    N, M = map(int, input().split())
    fari = [list(map(int, input().split())) for _ in range(N)]

    max_mari = 0
    for i in range(N - M + 1):              # 파리채 만큼의 너비 확보해서 간격 설정
        for j in range(N  - M + 1):
            mari = 0
            for y in range(i, i + M):
                for x in range(j, j + M):   # 파리채 너비 만큼 마릿수 카운팅
                    mari += fari[y][x]

            if max_mari < mari:             # 최댓값 최신화
                max_mari = mari
            
    print(f'#{t + 1} {max_mari}')