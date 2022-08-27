T = int(input())

for t in range(T):
    N, Q = map(int, input().split())
    boxes = [0] * N

    for i in range(Q):
        L, R = map(int, input().split())
        for j in range(L - 1, R):
            boxes[j] = i + 1

    print(f'#{t + 1}', end=' ')
    print(*boxes)