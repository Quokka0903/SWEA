for t in range(int(input())):
    N, M = map(int, input().split())
    russia = [input() for _ in range(N)]

    min_cnt = M * N
    for i in range(N - 2):
        a_cnt = 0
        
        for a in range(i + 1):

            print('a')
            print(a)
            print(russia[a])

            for chk in russia[a]:
                if chk != 'W':
                    a_cnt += 1
        print('a_cnt')
        print(a_cnt)

        for j in range(i + 1, N - 1):
            b_cnt = a_cnt

            for b in range(i + 1, j + 1):

                print('b')
                print(b)
                print(russia[b])

                for chk in russia[b]:
                    if chk != 'B':
                        b_cnt += 1
            
            print('b_cnt')
            print(b_cnt)

            c_cnt = b_cnt
            for k in range(j + 1, N):                
                

                print('k')
                print(k)
                print(russia[k])

                for chk in russia[k]:
                    if chk != 'R':
                        c_cnt += 1
            
            print('c_cnt')
            print(c_cnt)

            if (c_cnt) < min_cnt:
                min_cnt = (c_cnt)

    print(f'#{t + 1} {min_cnt}')