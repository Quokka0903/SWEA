from pprint import pprint


for t in range(int(input())):
    N, M = map(int, input().split())
    pan = [[0] * N for _ in range(N)]
       
    pan[N//2 - 1][N//2 - 1 : N //2 + 1] = [2, 1]
    pan[N//2][N//2 - 1 : N //2 + 1] = [1, 2]

    for _ in range(M):
        x, y, dol = map(int, input().split())
        pan[y - 1][x -1] = dol

        for i, j in [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]]:
            while 0 <= y - 1 + i < N and 0 <= x - 1 + j < N:
                
                if pan[y - 1 + i][x - 1 + j] == 0:
                    break

                elif pan[y - 1 + i][x - 1 + j] == dol:

                    if i == 0:
                        if j > 0:
                            for a in range(j):
                                pan[y - 1][x - 1 + a] = dol                        
                        else:
                            for a in range(0, j - 1, -1):
                                pan[y - 1][x - 1 + a] = dol
                        break  

                    elif j == 0:
                        if i > 0:
                            for a in range(i):
                                pan[y - 1 + a][x - 1] = dol                        
                        else:
                            for a in range(0, i - 1, -1):
                                pan[y - 1 + a][x - 1] = dol                        
                        break

                    elif i > 0 and j > 0:
                        for a in range(1, i):
                            pan[y - 1 + a][x - 1 + a] = dol
                        break
                    
                    elif i > 0 and j < 0:
                        for a in range(1, i):
                            pan[y - 1 + a][x - 1 - a] = dol
                        break

                    elif i < 0 and j > 0:
                        for a in range(1, j):
                            pan[y - 1 - a][x - 1 + a] = dol
                        break

                    elif i < 0 and j < 0:
                        for a in range(0, i - 1, -1):
                            pan[y - 1 + a][x - 1 + a] = dol
                        break                                        
                    

                if i:
                    i = (i + 1) if i > 0 else (i - 1)
                if j:
                    j = (j + 1) if j > 0 else (j - 1)
          

    A, B = 0, 0
    for i in range(N):
        for j in range(N):
            if pan[i][j] == 1:
                A += 1
            elif pan[i][j] == 2:
                B += 1
    
    print(f'#{t + 1} {A} {B}')