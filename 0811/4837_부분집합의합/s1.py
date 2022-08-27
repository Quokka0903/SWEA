def sum_of_lists (list) :
    res = 0
    for i in list :
        res += i
    return res

def johab(list, n, leng) :
    res = []
    if n > leng:
        return res
    if n == 1 :
        for i in list :
            res.append([i])
    elif n > 1 :
        for i in range(len(list) - n + 1) :
            for j in johab(list[i + 1:], n - 1, leng):
                res.append([list[i]] + j)
    return res

def sum_of_parts (N, K, leng) :
    whole = []
    max, cnt = 0, 0

    for i in range (leng, leng-N, -1) :
        max += i

    if K > max :
        return (cnt)
    
    for i in range(leng) :
        whole.append(i+1)
    
    temp = johab(whole, N, leng)

    for chk in temp :
        if sum_of_lists(chk) == K :
            cnt += 1

    return cnt

T = int(input())

for t in range(T) :
    N, K = map(int, input().split())
    print(f'#{t+1} {sum_of_parts(N, K, 12)}')