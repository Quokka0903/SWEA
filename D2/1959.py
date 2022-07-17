T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    ans = 0
    for i in range(abs(N - M) + 1) :
        val = 0
        for j in range(min(N, M)) :
            if len(A) > len(B) :
                val += int(A[j+i]) * int(B[j])
            elif len(A) < len(B) :
                val += int(A[j]) * int(B[j+i])
            else :
                val += int(A[j]) * int(B[j])
        if val > ans :
            ans = val

    print('#%d %d' % (t, ans))