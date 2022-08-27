T = int(input())

for t in range(T):
    N, M = map(int, input().split())
    suyeol = list(map(int, input().split()))
    print(f'#{t + 1} {suyeol[M % N]}')       # 한 바퀴 도는 것은 아예 제외하고 계산!