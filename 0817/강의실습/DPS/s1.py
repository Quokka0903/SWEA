list_adj = [[1, 2], [0, 3, 4], [0, 4], [1, 5], [1, 2, 5], [3, 4, 6], [5]]

def dfs(v, N):
    visited = [0] * N
    stack = [0] * N
    top = -1
    
    print(v)
    visited[v] = 1
    
    while True:
        for w in list_adj[v]:

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

dfs(0, 7)