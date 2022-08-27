sunseo = {'+' : 1, '-' : 1, '*' : 2, '/' : 2}       # 연산 순서
gualho = {'(' : ')'}                                # 괄호

T = int(input())

for t in range(T):
    print(f'#{t + 1}', end = ' ')
    susik = input()
    stack = []
    for chk in susik:
        if ord(chk) >= 48 and ord(chk) <= 57:       # 숫자면
            print(chk, end = '')                    # 그냥 쁘린뜨
        else :
            if chk in sunseo:                       # 숫자가 아니고 연산이면
                if stack:                           # 스택이 있을 때
                    while stack and stack[-1] in sunseo and sunseo[stack[-1]] >= sunseo[chk]:
                        print(stack.pop(), end = '')# 순서 낮은 애 나올 때까지 팝해서 쁘린뜨
                stack.append(chk)                   # 하고 나서 푸쉬
            else :
                if chk in gualho:                   # 괄호 '('면
                    stack.append(chk)               # 일단 넣기
                else:
                    while stack[-1] != '(':         # 괄호 ')'면
                        print(stack.pop(), end = '')# '(' 나올 때까지 팝해서 쁘린뜨
                    stack.pop()                     # '('도 팝
    while stack:
        print(stack.pop(), end = '')                # 남아있는 연산이 있으면 쁘린뜨
    print()