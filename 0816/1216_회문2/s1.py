def my_len(a):
    res = 0
    for i in a:
        res += 1
    return res

for _ in range(10):
    t = int(input())
    palin = [(input()) for _ in range(100)]

    maxlen = 0
    for i in range(1, 100):
        for j in range(100):
            for k in range(100 - i + 1):
                col, row = '', ''

                for x in range(i):
                    col += palin[j][k + x]
                    row += palin[k + x][j]


                if col == col[::-1]:
                    maxlen = i
                if row == row[::-1]:
                    maxlen = i
            

    print(f'#{t} {maxlen}')