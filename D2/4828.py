T = int(input())
for t in range(1, T + 1):
    idx = int(input())
    res = list(map(int, input().split()))
    print(f'#{t} {max(res) - min(res)}')