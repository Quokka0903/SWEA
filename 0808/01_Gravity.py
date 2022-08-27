T = int(input())

for t in range(T) :
    
    N = int(input())
    arr = list(map(int, input().split()))

    fall, max = 0, 0

    # 이중포문
    for idx_1 in range(len(arr)) :
        fall = N - idx_1 - 1
        for idx_2 in range(idx_1 + 1, len(arr)) :
            if arr[idx_1] <= arr[idx_2] :
                fall -= 1
        
        if max < fall :
            max = fall

    print(f'#{t + 1} {max}')