list_adj = [[1, 2], [0, 3, 4], [0, 4], [1, 5], [1, 2, 5], [3, 4, 6], [5]]
'''
6 8
0 1
0 2
1 3
1 4
2 4
3 5
4 5
5 6
'''

def dfs(v, N):
    visited = [0] * N
    stack = [0] * N
    top = -1
    
    print(v)
    visited[v] = 1
    
    while True:
        for w in adjList[v]:
            if visited[w] == 0:
                top += 1
                stack[top] = v
                v = w
                visited[w] = 1
                
                print(v)
                break
            
        else:
            if top != -1:
                v = stack[top]
                top -= 1
            else :
                break

V, E = map(int, input().split())
N = V + 1
adjList = [[] for _ in range(N)]
for _ in range(E):
    a, b = map(int, input().split())
    adjList[a].append(b)
    adjList[b].append(a)

visited = [0] * N
stack = [0] * N

dfs(0, N)