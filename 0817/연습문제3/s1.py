def dfs(v, ans):
    top = -1

    visited[v] = 1
    ans.append(v + 1)
    while True:
        for w in adjList[v]:

            if visited[w] == 0:
                top += 1
                stack[top] = v
                v = w
                visited[w] = 1
                
                ans.append(v + 1)
                break

        else:
            if top != -1:
     
                v = stack[top]
                top -= 1
            else :
                break


V, E = map(int, input().split())
N = V

adjList = [[] for _ in range(N)]
inputList = list(map(int, input().split()))

for i in range(E):
    a, b = inputList[i * 2], inputList[i * 2 + 1]
    adjList[a - 1].append(b - 1)
    adjList[b - 1].append(a - 1)

visited = [0] * N
stack = [0] * N
ans = []

dfs(0, ans)
print(*ans)