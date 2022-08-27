dx = [0, 1, -1]
dy = [1, 0, 0]

for _ in range(10):
    t = int(input())
    sadari = [list(map(int, input().split())) for _ in range(100)]

    dir, res = 0, 0
    min_cnt = 100 ** 2
    for x in range(100):
        temp_x = x
        if sadari[0][x] == 0:
            continue
        else:
            cnt, y = 0, 0
            while y != 99:
                if dir == 0:
                    if x > 1 and sadari[y][x - 1] == 1:
                        dir = 2
                    elif x <= 98 and sadari[y][x + 1] == 1:
                        dir = 1

                if x + dx[dir] < 0 or x + dx[dir] > 99 or sadari[y][x + dx[dir]] == 0 :
                    dir = 0

                x += dx[dir]
                y += dy[dir]
                cnt += 1
                
            if min_cnt > cnt:
                min_cnt = cnt
                res = temp_x
            
    print(f'#{t} {res}')