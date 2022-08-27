for _ in range(10) :
    t = int(input())
    ladder = []
    for i in range(100) :
        ladder.append(list(map(int, input().split())))

    di = [0, 0, -1]
    dj = [1, -1, 0]
    direction = 2

    for x in range(100) :
        if ladder[99][x] == 2 :
            
            y_here, x_here = 99, x
            
            while y_here != 0 :
                if direction == 1 :
                    if ((x_here - 1) >= 0) and (ladder[y_here][x_here - 1] == 1) :
                        direction = 1
                    else :
                        direction = 2

                elif direction == 0 :
                    if ((x_here + 1) <= 99) and (ladder[y_here][x_here + 1] == 1):
                        direction = 0
                    else :
                        direction = 2

                else :
                    if ((x_here - 1) >= 0) and (ladder[y_here][x_here - 1] == 1) :
                        direction = 1
                    elif ((x_here + 1) <= 99) and (ladder[y_here][x_here + 1] == 1):
                        direction = 0
                    else :
                        direction = 2

                y_here += di[direction]
                x_here += dj[direction]

            print(f'#{t} {x_here}')