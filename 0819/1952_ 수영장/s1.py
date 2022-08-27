def my_min(a):
    if a:
        min = a[0]
        for x in a:
            if x < min:
                min = x
        return min
    else:
        return 0


def my_sum(a):
    res = 0
    for x in a:
        res += x
    return res


T = int(input())

for t in range(T):
    price = list(map(int, input().split()))
    plan = list(map(int, input().split()))
    cost = [0] * 15

    cnt = 1
    sum_il = 0
    for i in range(12):                      # 1개월권 or 일일권
        if plan[i]:
            
            if plan[i] < price[1] // price[0]:
                cost[i] = price[0] * plan[i]
            else :
                cost[i] = price[1]
            sum_il += cost[i]
     
     
    min_sam = sum_il
    for i in range(3):                      # 3개월권 4개
        for j in range(i + 3, 6):
            for k in range(j + 3, 9):
                for l in range(k + 3, 12):
                    sum_sam = 0
                    rest = (my_sum(cost[:i]) + my_sum(cost[i + 3 : j]) \
                         + my_sum(cost[j + 3 : k]) + my_sum(cost[k + 3: l])) \
                            + my_sum(cost[l + 3:])
                    sum_sam += price[2] * 4 + rest
                    if sum_sam < min_sam:
                        min_sam = sum_sam


    for i in range(6):                      # 3개월권 3개
        for j in range(i + 3, 9):
            for k in range(j + 3, 12):
                sum_sam = 0
                rest = (my_sum(cost[:i]) + my_sum(cost[i + 3 : j]) \
                     + my_sum(cost[j + 3 : k]) + my_sum(cost[k + 3:]))
                sum_sam += price[2] * 3 + rest
                if sum_sam < min_sam:
                    min_sam = sum_sam

    for i in range(9):                      # 3개월권 2개
        for j in range(i + 3, 12):
            sum_sam = 0
            rest = (my_sum(cost[:i]) + my_sum(cost[i + 3 : j]) \
                     + my_sum(cost[j + 3 :]))
            sum_sam += price[2] * 2 + rest
            if sum_sam < min_sam:
                min_sam = sum_sam

    for i in range(12):                      # 3개월권 1개
        sum_sam = 0
        rest = (my_sum(cost[:i]) + my_sum(cost[i + 3 :]))
        sum_sam += price[2] + rest
        if sum_sam < min_sam:
            min_sam = sum_sam
    
    
    if min_sam > price[3]:                   # 1년권
        res = price[3]
    else:
        res = min_sam
                
    print(f'#{t + 1} {res}')