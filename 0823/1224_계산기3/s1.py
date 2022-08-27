def cal(wrd, stack):
    for char in wrd:
        if char not in '(+*)':      # 숫자일 경우
            stack.append(int(char)) # 스택에 숫자로 푸쉬
        else:                       # 연산자일 경우
            if char == '+':         # 경우에 맞춰 연산
                stack.append(stack.pop() + stack.pop())
            if char == '*':
                stack.append(stack.pop() * stack.pop())
    return stack[-1]                # 최종값 리턴


for t in range(1, 11):
    n = int(input())
    wrd = input()
    stack = []
    result = ''

    for chk in wrd:
        if chk in '(+*)':           # 연산자일 경우
            if not stack:           # 스택없으면 추가
                stack.append(chk)
            elif chk == '(':        # 여는괄호면 추가
                stack.append(chk)
            elif chk == '*':        # 곱셈은 다음 곱 전까지 팝한다음 추가
                while stack and stack[-1] == '*':
                    result += stack.pop()
                stack.append(chk)
            elif chk == '+':        # 덧셈은 여는괄호 전까지 팝한다음 추가
                while stack and stack[-1] != '(':
                    result += stack.pop()
                stack.append(chk)
            elif chk == ')':        # 괄호 닫으면 여는괄호 전까지 팝
                while stack and stack[-1] != '(':
                    result += stack.pop()
                stack.pop()         # 하고 나서 여는괄호도 팝

        else:
            result += chk           # 숫자는 걍 추가

    while stack:
        result += stack.pop()       # 남은 스택도 걍 추가

    res = cal(result, [])           # 완성된 후위연산을 연산돌림

    print(f'#{t} {res}')