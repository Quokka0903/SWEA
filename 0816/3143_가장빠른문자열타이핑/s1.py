def my_len(a):
    res = 0
    for i in a:
        res += 1
    return res

T = int(input())

for t in range (T):
    A, B = input().split()

    cnt = 0
    i, j = 0, my_len(B)
    while i < (my_len(A)):

        if A[i] == B[0]:
        
            if A[i:i + j] == B:
                cnt += 1
                i += j
                continue

        cnt += 1
        i += 1
        
    print(f'#{t + 1} {cnt}')