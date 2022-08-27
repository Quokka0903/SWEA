for t in range(1, 11):
    N = int(input())
    
    list_m = [list(map(int, input().split())) for _ in range(N)]

    sum_m = 0
    for i in range(N):
        stacks = [0] * (N**2)
        top = -1
        for j in range(N):

            if top == -1 and list_m[j][i] == 2:     # 꼭대기 N극은 스킵
                continue

            if list_m[j][i] != 0:
                if top >= 0 and stacks[top] == 1 and list_m[j][i] == 2:
                    sum_m += 1                      # S극과 N극이 모인 것 하나마다 카운트
                top += 1
                stacks[top] = list_m[j][i]

    print(f'#{t} {sum_m}')
