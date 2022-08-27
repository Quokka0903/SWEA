for t in range(10) :
    idx = int(input())
    bd = list(map(int, input().split()))
    cnt = 0
    
    for j in range(2, idx - 2) :
        left, right = 0, 0
        if (bd[j] - bd[j-2]) > 0 and (bd[j] - bd[j-1]) > 0 :
            left = (bd[j] - bd[j-2] if bd[j-2] > bd[j-1] else bd[j] - bd[j-1])
        
        if (bd[j] - bd[j+2]) > 0 and (bd[j] - bd[j+2]) > 0 :
            right = (bd[j] - bd[j+2] if bd[j+2] > bd[j+1] else bd[j] - bd[j+1])
        
        if left > 0 and right > 0 :
            cnt += (left if left < right else right)

    print(f'#{t+1} {cnt}')