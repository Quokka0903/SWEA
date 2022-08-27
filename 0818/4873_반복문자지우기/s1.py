T = int(input())

for t in range(T):
    chk = input()
    stack = []
    idx = 0

    for word in chk:
        if stack and stack[-1] == word:
            stack.pop()
            idx -= 1
        else:
            stack.append(word)
            idx += 1
    
    print(f'#{t + 1} {idx}')