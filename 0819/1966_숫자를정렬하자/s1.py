def my_sort(a, N) :
    for i in range(N-1, 0, -1) :
        for j in range(i) :
            if a[j] > a[j+1] :
                a[j], a[j+1] = a[j+1], a[j]
    return(a)

T = int(input())

for t in range(1, T + 1):
    N = int(input())
    text = list(map(int, input().split()))
    ans = my_sort(text, N)
    print(f'#{t}', end=' ')
    print(*ans)