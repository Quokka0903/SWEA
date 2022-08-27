def bin_search(L, R, goal, tried):                      # 이진 탐색 함수 (시작 페이지, 끝 페이지, 찾는 페이지, 시도 횟수)
    tried += 1                                          # 한번 할때 마다 시도횟수 추가
    half = int((L + R) / 2)
    if half == goal:                                    # 찾으면 시도횟수 반환
        return tried
    else:
        if half > goal:                                 # 못찾으면, 왼쪽 오른쪽으로 범위 바꿔서 다시 이진 탐색
            return bin_search(L, half, goal, tried)
        else:
            return bin_search(half, R, goal, tried)


tc = int(input())

for testcase in range(tc):
    total, A, B = tuple(map(int, input().split()))
    result_a = bin_search(1, total, A, 0)
    result_b = bin_search(1, total, B, 0)

    if result_a > result_b:
        print(f'#{testcase + 1} B')
    elif result_a < result_b:
        print(f'#{testcase + 1} A')
    else:
        print(f'#{testcase + 1} 0')