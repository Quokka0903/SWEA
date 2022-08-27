def my_len(a):
    res = 0
    for i in a:
        res += 1
    return res

T = int(input())

for t in range(T):
    N, M = map(int, input().split())

    list_str = [list(input()) for _ in range(N)]

    flag = False
    ans = []
    for i in range(N):
        for j in range(N - M + 1):
            if list_str[i][j] == list_str[i][j + M - 1]:
                if list_str[i][j:j + (M//2)] == list_str[i][j + M : j + M  - (M//2) - 1: -1]:
                    ans = list_str[i][j : j + M]
                    flag = True
                    break
        if flag == True:
            break
    
    i, j = 0, 0
    if flag == False:
        for i in range(N):
            for j in range(N - M + 1):
                if list_str[j][i] == list_str[j + M - 1][i]:
                    for k in range(M//2) :
                        if list_str[j + k][i] == list_str[j + M - k - 1][i]:
                            ans.extend(list_str[j + k][i])
                            if my_len(ans) == M//2:
                                for x in range(j + k + 1, j + M):
                                    ans.extend(list_str[x][i])
                                flag = True
                                break
                        else :
                            ans = []
                            break                     
            if flag == True:
                break


    
    res = ''
    for text in ans:
        res += text
    print(f'#{t + 1} {res}')