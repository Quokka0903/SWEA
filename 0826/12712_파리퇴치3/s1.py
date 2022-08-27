sipza = [[1, 0], [-1, 0], [0, 1], [0, -1]]
eksu = [[1, 1], [1, -1], [-1, 1], [-1, -1]]

for t in range(int(input())):
    N, M = map(int, input().split())

    fari = [list(map(int, input().split())) for _ in range(N)]

    max_mari = 0
    for i in range(N):
        for j in range(N):
            s_mari = fari[i][j]
            e_mari = fari[i][j]

            for m in range(1, M):
                for y, x in sipza:
                    if 0 <= (i + m * y) < N and 0 <= (j + m * x) < N:
                        s_mari += fari[i + m * y][j + m * x]
                        
                for y, x in eksu:
                    if 0 <= (i + m * y) < N and 0 <= (j + m * x) < N:
                        e_mari += fari[i + m * y][j + m * x]


            max_mari = max(max_mari, s_mari, e_mari)
    
    print(f'#{t + 1} {max_mari}')


    