T = int(input())

for t in range (T) :
    leng = int(input())
    list_cnt = input()
    cnt, max = 0, 0
    for chk in list_cnt :
        if chk == '1' :
            cnt += 1
        elif chk == '0' :
            if max < cnt :
                max = cnt
            cnt = 0
        if chk is list_cnt[-1] :
            if max < cnt :
                max = cnt
                
    print(f'#{t+1} {max}')