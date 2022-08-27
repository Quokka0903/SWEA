def my_len(list_in):
    res = 0
    for i in list_in:
        res += 1
    return res


T = int(input())

for t in range(T):
    list_soi = input()
    leng = my_len(list_soi)

    idx = 0
    cnt = 0
    sum_soi = 0
    while idx < leng:
        if list_soi[idx] == '(':
            if list_soi[idx + 1] == ')':
                sum_soi += cnt
                idx += 1
            else :
                cnt += 1
                sum_soi += 1
        else :
            cnt -= 1
            
        idx += 1
    
    print(f'#{t + 1} {sum_soi}')