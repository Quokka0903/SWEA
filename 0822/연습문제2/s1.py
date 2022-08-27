def f(i, N):
    if i == N:                          # 각 분기별로 연산되어 최댓값 원소까지 다다랐을 때
        chk = 0
        for i in range(N):
            if bit[i]:                  # 해당 비트 행렬에 값이 있을 시
                chk += (i + 1)          # 숫자 카운트
        if chk == 10:                   # 합이 10이면
            res = []
            for i in range(N):          # 행렬 쁘린뜨
                if bit[i]:
                    res.append(i + 1)
            print(res)
    else:
        bit[i] = 1
        f(i + 1, N)
        bit[i] = 0
        f(i + 1, N)

A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
bit = [0] * 10
f(0, 10)