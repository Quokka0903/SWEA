def rect(arr, n):
    temp = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            temp[j][n - i - 1] = arr[i][j]

    return temp

T = int(input())

for t in range(T) :
    print(f'#{t+1}')
    N = int(input())
    temp = []
    ans = []
    list_a = [list(map(str, input().split())) for _ in range(N)]
    for i in range(3) :
        list_a = rect(list_a, N)
        temp.extend(list_a)
    for i in range(N * 3) :
        ans += {''.join(temp[i])}
    for i in range(N) :
        a = ans[i::N]
        count = 0 
        for i in a:
            count += 1
            if count == 3:
                print(i)
                count = 0
            else:
                print(i, end = ' ')