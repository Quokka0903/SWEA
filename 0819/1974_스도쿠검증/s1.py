def my_sum(a):
    res = 0
    for i in a:
        res += i
    return res

def my_sudoku():
    sudoku = [list(map(int, input().split())) for _ in range(9)]

    for i in range(3):

        for j in range(3):
            if my_sum(sudoku[3 * i + j]) != 45:
                return 0
        
        for k in range(3):
            sum_sudoku = 0
            for a in range(3):
                for b in range(3):
                    sum_sudoku += sudoku[i * 3 + a][k * 3 + b]
            if sum_sudoku != 45:
                return 0
    
    for y in range(9):
        sum_sudoku = 0
        for x in range(9):
            sum_sudoku += sudoku[x][y]
        if sum_sudoku != 45:
                return 0
    return 1


T = int(input())

for t in range(T):
    print(f'#{t + 1} {my_sudoku()}')