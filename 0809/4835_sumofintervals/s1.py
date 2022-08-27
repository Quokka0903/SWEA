T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    list_v = list(map(int, input().split()))
    max_v, min_v = 0, 0 # max, min 초기화
    for num in range (M) :
        min_v += list_v[num] # 리스트 내 아무 값이나 M개만큼 더함.

    for i in range(N - M) :
        sum_v = 0
        for j in range(i, i + M) : # i 인덱스부터 M 개씩 합.
            sum_v += list_v[j]
        if sum_v > max_v : # 최댓값 최신화
            max_v = sum_v
        if sum_v < min_v : # 최솟값 최신화
            min_v = sum_v

    print(f'#{test_case} {max_v - min_v}')