T = int(input())

for test_case in range(1, T + 1):
    max_v, min_v = 0, 2147483647
    N, M = map(int, input().split())
    list_v = list(map(int, input().split()))
    for i in range(N - M) :
        sum_v = 0
        for j in range(i, i + M) :
            sum_v += list_v[j]
        if sum_v > max_v :
            max_v = sum_v
        print(max_v)
        if sum_v < min_v :
            min_v = sum_v
        print(min_v)

    print(f'#{test_case} {max_v - min_v}')