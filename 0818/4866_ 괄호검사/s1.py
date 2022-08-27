dict = {'(' : ')', '{' : '}', '[' : ']'}
gualho = [')', '}', ']']

T = int(input())

for t in range(T):
    stack = []
    chk = input()

    for word in chk:

        if word not in dict and word not in gualho:
            continue

        else :
            if stack and stack[-1] not in gualho and dict[stack[-1]] == word:
                stack.pop()
            
            else:
                stack.append(word)
    
    print(f'#{t + 1}', end=' ')
    if stack:
        print(0)
    else:
        print(1)