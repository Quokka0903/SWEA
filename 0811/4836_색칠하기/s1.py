T = int(input())

for t in range(T) :
    board = [[0]*10 for _ in range(10)]
    paint = int(input())
    for _ in range(paint) :
        xl, yl, xr, yr, color = map(int, input().split())
        for y in range(yl, yr + 1) :
            for x in range(xl, xr + 1) :
                if board[y][x] == color :
                    continue
                
                elif board[y][x] == 3 :
                    continue
                
                else :
                    board[y][x] += color
    
    cnt = 0
    for y in range(10) :
        for x in range(10) :
            if board[y][x] == 3 :
                cnt += 1
                
    print(f'#{t+1} {cnt}')