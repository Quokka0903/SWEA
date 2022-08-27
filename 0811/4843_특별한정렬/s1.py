def sort_self (list, N) :
    for i in range(N-1, 0, -1) :
        for j in range(i) :
            if list[j] > list[j+1] :
                list[j], list[j+1] = list[j+1], list[j]
    return(list)

T = int(input())

for t in range(T) :
    N = int(input())
    res = []
    temp = sort_self(list(map(int, input().split())), N)
    for i in range(N//2) :
        res.append(temp[-i-1])
        res.append(temp[i])
    res = res[:10]

    print(f'#{t+1}', end=' ')
    print(*res)