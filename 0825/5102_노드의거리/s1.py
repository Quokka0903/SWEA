def bfs(s, g, e):                           # 시작, 도착, 간선 수
    visited = [0] * (V + 1)
    q = [s]                                 # 큐에 시작점 추가
    visited[s] = 1                          # 시작점 1
    
    while q:
        s = q.pop(0)
        for w in nodes[s]:                  # 큐 팝값과 연결된 노드 탐색
            if visited[w] == 0:
                q.append(w)                 # 안갔으면 큐에 넣고 거리 1 더해서 할당
                visited[w] = visited[s] + 1
            if w == g:                      # 찾았으면
                return (visited[w] - 1)     # 리턴

    return 0


T = int(input())
for t in range(T):
    V, E = map(int, input().split())
    nodes = [[] for _ in range(V + 1)]
    for _ in range(E):
        i, j = map(int, input().split())
        nodes[i].append(j)
        nodes[j].append(i)
    
    S, G = map(int, input().split())

    print(f'#{t + 1} {bfs(S, G, E)}')       # 결과값 출력
