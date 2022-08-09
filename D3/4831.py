T = int(input())

for t in range(T) :
    K, N, M = map(int,input().split())

    charge_point = (list(map(int,input().split())))
    noseon = 0
    idx = 0
    count = 0

    while noseon < N - K : # N - K 이후의 거리는 한 번의 충전으로 갈 수 있음
        noseon += K # 최대 거리만큼 우선 탐색

        if noseon  < charge_point[idx] : # 최대거리 안에 다음 충전소 없으면 0
            count = 0
            break
        while (idx < M) and (charge_point[idx] <= noseon) : # 최대거리 안에서 가장 먼 충전소까지 idx 이동
            idx += 1

        # while문에서 가장 먼 충전소 다음 충전소 idx로 나오게 됨

        noseon = charge_point[idx - 1]  # 최대거리 안에서 가장 먼 충전소까지 버스 이동
        count += 1 # 충전횟수 증가

    print(f'#{t + 1} {count}')


    