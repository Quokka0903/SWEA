T = int(input())

for t in range(T):
    h = int(input())
    pascal = []

    print(f'#{t + 1}')
    for i in range(h):
        if i <= 1:
            pascal.append(1)
        
        else:
            pascal.append(pascal[-1])
            for j in range(i - 1, 0, -1): 
                pascal[j] = pascal[j] + pascal[j - 1]

        print(*pascal)