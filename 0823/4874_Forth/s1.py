def lets_cal():                     # 계산해주는 함수
    chk = stack_cal.pop()
    if my_len(stack_num) >= 2:      # 숫자스택 쌓인 게 2개 이상일때 연산
        if chk == '+':
            stack_num.append(stack_num.pop() + stack_num.pop())
        elif chk == '-':
            a = stack_num.pop()
            b = stack_num.pop()
            stack_num.append(b - a)
        elif chk == '*':
            stack_num.append(stack_num.pop() * stack_num.pop())
        elif chk == '/':
            a = stack_num.pop()
            b = stack_num.pop()
            stack_num.append(b // a)
    else:
        return 1                    # 오류발생 시 flag = 1 
    return 0                        # 정상종료 시 flag = 0

def my_len(a):                      # 배열 길이 함수 설정
    res = 0
    for _ in a:
        res += 1
    return res
                                    # 연산 우선순위 설정
cal = {'+' : 1, '-' : 1, '*' : 2, '/' : 2}

T = int(input())

for t in range(T):
    case = list(input().split())
    stack_num = []
    stack_cal = []
    flag = 0
    for unit in case:
        if unit == '.':             # 마무리
            break
        if unit in cal:             # 연산기호일 경우
            while stack_cal and cal[stack_cal[-1]] <= cal[unit]:
                flag = lets_cal()   # 우선순위 정렬 될 때까지 계산
            stack_cal.append(unit)  # 하고 나서 푸쉬
        else:                       # 숫자일 경우
            if stack_cal:           # 연산 할 게 있을 때
                flag = lets_cal()   # 일단 연산
            stack_num.append(int(unit))
                                    # 하고 나서 푸쉬
        if flag == 1:               # 오류 있으면 바로 탈출
            break
    
    if flag != 1:                   # 오류 없을 때
        while stack_cal:            # 연산
            flag = lets_cal()
        if my_len(stack_num) != 1:  # 오류 있으면 flag = 1
            flag = 1
    
    print(f'#{t + 1}', end=' ')
    if flag == 0:
        print(stack_num[0])         # 오류 없을 시 결과값 출력
    else:
        print('error')