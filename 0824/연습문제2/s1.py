def bfs(s, N):

    visited = [0] * (N + 1)
    q = []
    q.append(s)
    visited[s] = 1

    while q:
        s = q.pop(0)
        print(s, end= ' ')
        for w in dir[s]:
            if visited[w] == 0:
                q.append(w)
                visited[w] = visited[s] + 1

N, V = map(int, input().split())
nodes = list(map(int, input().split()))

dir = [[] for _ in range(N + 1)]
for i in range(V):
    dir[nodes[2 * i]].append(nodes[2 * i + 1])
    dir[nodes[2 * i + 1]].append(nodes[2 * i])

bfs(1, N)