def abs_self (num) :
    if num < 0 :
        return -num
    else :
        return num

def delta_custom_sum (list, width) :
    
    delta_i = [0, 0, 1, -1]
    delta_j = [1, -1, 0, 0]
    res = 0
    
    for i in range(width) :
        for j in range(width):
            for k in range(4):
                if (i + delta_i[k]) >= 0 and (i + delta_i[k]) < width \
                    and (j + delta_j[k]) >= 0 and (j + delta_j[k]) < width :

                    res += abs_self(list[i + delta_i[k]][j + delta_j[k]] - list[i][j])

    return res


T = int(input())

for t in range(T) :
    width = int(input())
    list_delta = []
    for i in range(width) :
        list_delta.append(list(map(int, input().split())))
    ans = delta_custom_sum(list_delta, width)

    print(f'#{t+1} {ans}')
