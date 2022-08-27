T = int(input())

for t in range(T) :
    map_fly = []
    N, M = map(int, input().split())
    for _ in range(N) :
        map_fly.append(list(map(int, input().split())))

    fly_max = 0
    for i in range(N - M + 1) :
        for j in range(N - M + 1) :
            fly_sum = 0
            for y in range(i, i + M) :
                for x in range(j, j + M) :
                    fly_sum += map_fly[y][x]

            if fly_max < fly_sum :
                fly_max = fly_sum

    print(f'#{t+1} {fly_max}')