for t in range(1, 11):
    leng, list_num = input().split()
    stack = []

    for num in list_num:

        if stack and stack[-1] == num:
            stack.pop()
        
        else:
            stack.append(num)
        
    ans = ''
    for res in stack:
        ans += res
    
    print(f'#{t} {ans}')