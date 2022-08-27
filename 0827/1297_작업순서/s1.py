for t in range(1, 11):
    V, E = map(int, input().split())
    ans = []
    cnt = [0] * V                                   # 방문횟수 노드
    visited = [0] * V                               # 방문한 노드
    nodes = [[] for _ in range(V + 1)]              
    temp = list(map(int, input().split()))

    for i in range(E):
        nodes[temp[2 * i]].append(temp[2 * i + 1])  # 노드 세팅
        cnt[temp[2 * i + 1] - 1] += 1
    
    start_stack = []                                # 시작점 노드
    stack = []                                      # 방문할 노드
    wait_stack = []                                 # 선결조건 남은 노드
    for i in range(len(cnt)):                       # 선결조건 없는 애들 시작점 설정
        if cnt[i] == 0:
            start_stack.append(i + 1)

    while start_stack:
        stack.append(start_stack.pop())             # 시작점 스택 제일 앞에 푸쉬

    while stack or wait_stack:                      # 스택들 남아있는지 확인
        if stack:
            s = stack.pop()                         # 스택 있으면 먼저
        else:
            s = wait_stack.pop()                    # 스택 없으면 대기 스택부터

        cnt[s - 1] -= 1                             # 현재 노드 카운트 차감
        if cnt[s - 1] > 0:                          # 선결조건 남았으면 대기 스택에 넣고 다른 스택 탐색
            wait_stack.append(s)
            continue
        visited[s - 1] = 1                          # 방문 체크

        ans.append(s)                               # 답안에 추가
        if len(ans) == V:                           # 방문노드 다 차면
            break                                   # 탈출
        for w in nodes[s]:                          # 노드에 하위 노드 있으면
            if visited[w - 1] == 0:                 # 방문한 앤지 체크하고
                stack.append(w)                     # 스택에 추가

    print(f'#{t}', end=' ')
    print(*ans)