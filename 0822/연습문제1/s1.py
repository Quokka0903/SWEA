T = int(input())

for t in range(T):
    print(f'#{t + 1} ', end = ' ')
    susik = input()
    stack = []                                  # 스택 선언
    for chk in susik:
        if ord(chk) >= 48 and ord(chk) <= 57:   # 숫자면
            print(chk, end = '')                # 그냥 쁘린뜨
        else :
            stack.append(chk)                   # 아니면 스택에 푸쉬
    
    while stack:
        print(stack.pop(), end = '')            # 스택에 있는 것 순차적 쁘린뜨
    print()