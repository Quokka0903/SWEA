sunseo = {'+' : 1, '*' : 2}             # 연산 순서

for t in range(10):
    N = int(input())
    susik = input()
    stack_num = []                      # 숫자 스택
    stack_cal = []                      # 연산 스택
    for chk in susik:
        if ord(chk) >= 48 and ord(chk) <= 57:   # 숫자 스택에 푸쉬
            stack_num.append(chk)
        else :
            if stack_cal:                       # 연산 순서가 낮은 애 나올때까지 팝해서 연산
                if sunseo[stack_cal[-1]] >= sunseo[chk]:
                    while stack_cal and sunseo[stack_cal[-1]] >= sunseo[chk]:
                        if stack_cal.pop() == '+':
                            stack_num.append(int(stack_num.pop()) + int(stack_num.pop()))
                        else:
                            stack_num.append(int(stack_num.pop()) * int(stack_num.pop()))
                stack_cal.append(chk)
            else:                               # 아니면 연산 스택에 푸쉬
                stack_cal.append(chk)

    while stack_cal:                            # 남은 연산 스택에 있는 것들 팝해서 연산
        if stack_cal.pop() == '+':
            stack_num.append(int(stack_num.pop()) + int(stack_num.pop()))
        else:
            stack_num.append(int(stack_num.pop()) * int(stack_num.pop()))
    
    print(f'#{t + 1} {stack_num[0]}')           # 결과값 쁘린뜨