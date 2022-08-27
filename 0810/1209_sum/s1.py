for t in range(10) :
    time = int(input())
    list_test = [list(map(int, input().split())) for _ in range(100)]
    
    z_sum_1, z_sum_2 = 0, 0
    max = 0

    for i in range(100) :
        x_sum, y_sum = 0, 0
        for j in range(100) :
            if i == j :
                z_sum_1 += list_test[i][j]
            
            if i + j == 99 :
                z_sum_2 += list_test[i][j]
            
            x_sum += list_test[i][j]
            y_sum += list_test[j][i]
        
        if max < x_sum :
            max = x_sum
        if max < y_sum :
            max = y_sum
    
    if max < z_sum_1 :
        max = z_sum_1
    if max < z_sum_2 :
        max = z_sum_2
    
    print(f'#{time} {max}')