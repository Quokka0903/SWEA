from re import L


def rect(arr, n):
    temp = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            temp[j][n - i - 1] = arr[i][j]

    return temp

T = int(input())

for t in range(T) :
    N = int(input())
    ans = []
    list_a = [list(map(int, input().split())) for _ in range(N)]
    ans.append(rect(list_a, N))
    for x in range(N - 1):
        print(ans[x])
        ans.append(rect(ans[x], N))

    

