for t in range(int(input())):
    N, K = map(int, input().split())
    whole = set()
    for i in range(N):
        whole.add(i + 1)
    print(f'#{t + 1}', end=' ')
    print(*whole^set(map(int, input().split())))