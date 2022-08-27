T = int(input())

for t in range(T):
    N, K = map(int, input().split())
    quiz = [list(map(int, input().split())) for _ in range(N)]

    cnt = 0
    for i in range(N):
        garo, sero = 0, 0
        for j in range(N):

            if quiz[i][j] == 1:                 # 가로 체크
                garo += 1
            if quiz[i][j] == 0 or j == N - 1 :  # 0이 나오거나 끝일 때
                if garo == K:                   # 카운팅된 가로 갯수가 K와 맞으면
                    cnt += 1                    # 카운트 +1
                garo = 0

            if quiz[j][i] == 1:                 # 세로 체크
                sero += 1
            if quiz[j][i] == 0 or j == N - 1:   # 0이 나오거나 끝일 때
                if sero == K:                   # 카운팅된 세로 갯수가 K와 맞으면
                    cnt += 1                    # 카운트 +1
                sero = 0
            

    print(f'#{t + 1} {cnt}')