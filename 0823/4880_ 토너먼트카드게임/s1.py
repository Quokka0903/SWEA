def do_game(l, i):
    if len(l) == 1:                 # 부전승
        return l[0], i[0]
    elif len(l) == 2:               # 이긴 사람 포지션과 인덱스 리턴
        if abs(l[0] - l[1]) == 1:
            if l[0] > l[1]:
                return l[0], i[0]
            else:
                return l[1], i[1]
        elif l[0] == l[1]:
            return l[0], i[0]
        else:
            if l[0] < l[1]:
                return l[0], i[0]
            else:
                return l[1], i[1]
    else:
        n = len(l)
        if n % 2 == 0:              # 짝수 슬라이싱
            l1, i1 = do_game(l[n//2:], i[n//2:])
            l2, i2 = do_game(l[:n//2], i[:n//2])
        
        else:                       # 홀수 슬라이싱
            l1, i1 = do_game(l[n//2 + 1:], i[n//2 + 1:])
            l2, i2 = do_game(l[:n//2 + 1], i[:n//2 + 1])

        if abs(l1 - l2) == 1:       # 취합해온 결과물 가지고 경기
            if l1 > l2:
                return l1, i1
            else:
                return l2, i2
        elif l1 == l2:
            if i1 < i2:
                return l1, i1
            else:
                return l2, i2
            
        else:
            if l1 < l2:
                return l1, i1
            else:
                return  l2, i2
        

T = int(input())

for t in range(T):
    N = int(input())
    seonsu = list(map(int, input().split()))
    
    index = []
    for i in range(N):
        index.append(i)
    
    res1, res2 = do_game(seonsu, index)
    print(f'#{t + 1} {res2 + 1}')