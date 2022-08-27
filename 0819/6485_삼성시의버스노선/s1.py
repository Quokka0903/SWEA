T = int(input())

for t in range(T):
    noseon = [0] * 5000
    res = []

    N = int(input())
    for i in range(N):
        a, b = map(int, input().split())
        for j in range(a - 1, b):
            noseon[j] += 1

    P = int(input())
    for k in range(P):
        C = int(input())
        res.append(noseon[C - 1])

    print(f'#{t + 1}', end = ' ')
    print(*res)