for t in range(int(input())):
    n = int(input())
    case = [list(map(int, input().split())) for _ in range(n)]

    keugi = []
    for y in range(n):
        for x in range(n):
            if case[y][x] == -1:            # 방문한 애 스킵
                continue
            elif case[y][x] != 0:           # 안 방문한 애면
                neobi = 0                   # 너비 깊이 선언
                gipi = 0
                y1, x1 = y, x               # 크기 잴 때 변수 선언
                y2, x2 = y, x
                while x1 < n and case[y1][x1] != 0 and case[y1][x1] != -1:
                    case[y1][x1] = -1       # 없는 값이나 가본 값 제외한
                    x1 += 1                 # x값까지 전진
                neobi = x1 - x2             # 너비 할당
                case[y2][x2] = 1            # 시작부분 초기화
                while y2 < n and case[y2][x2] != 0 and case[y2][x2] != -1:
                    case[y2][x2:x1] = [-1] * neobi
                    y2 += 1                 # 직사각형이므로 안가본 애 만큼
                gipi = y2 - y1              # 모조리 -1 만들면서 깊이 할당
                keugi.append([neobi * gipi, neobi, gipi])
                                            # 크기에 넓이, 너비, 깊이 어펜드

    ans = sorted(keugi, key = lambda x: (x[0], x[2]))
                                            # 넓이, 깊이 순으로 정렬
    print(f'#{t + 1} {len(ans)}', end=' ')
    for i, j, k in ans:                     # 깊이랑 너비 각각 프린트
        print(f'{k} {j}', end=' ')
    print()