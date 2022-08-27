def selectionsort(a, N) :
    for i in range(N-1, 0, -1) :
        for j in range(i) :
            if a[j] > a[j+1] :
                a[j], a[j+1] = a[j+1], a[j]
    return(a)

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    list_num = list(map(int, input().split()))
    ans = selectionsort(list_num, N)
    print(f'#{test_case}', end=' ')
    print(*ans)