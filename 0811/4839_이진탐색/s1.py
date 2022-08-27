T = int(input())

for t in range(T) :
    P, A, B = map(int, input().split())

    la, ra, lb, rb = 1, P, 1, P
    flag =''

    while True :

        ca, cb = int((la+ra)/2), int((lb+rb)/2)

        if ca == A :
            flag += 'A'
            break
        if cb == B :
            flag += 'B'
            break

        if A < ca :
            ra = ca
        elif A > ca :
            la = ca
        
        if B < cb :
            rb = cb
        elif B > cb :
            lb = cb
        
    if ca == A and cb == B :
        print(f'#{t+1} 0')
    else :
        print(f'#{t+1} {flag}')