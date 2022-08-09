T = int(input())

for i in range(T) :
    A, B = map(int, input().split())
    temp = [0] * 10
    ans = 0
    while B - A :
        temp = A
        list_temp = str(temp)
        for i in range(10) :
            print(list_temp.count(i))
            temp[i] += list_temp.count(f'{i}')
        A += 1
    
    for j in range(10) :
        ans += temp[j] * (j * 1)

    print(f'#{i + 1} {ans}')