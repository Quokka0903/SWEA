def dfs(s, g, v, nodes):
    tracked = [0] * (v + 1)
    stack = []
    while True:
        tracked[s] = 1

        for w in nodes[s]:
            if w == g:
                return 1
            if tracked[w] == 0:
                stack.append(s)
                s = w
                break

        else :
            if stack:
                s = stack.pop()
            else :
                return 0



T = int(input())

for t in range(T):
    V, E = map(int, input().split())
    nodes = [[] for _ in range(V + 1)]

    for _ in range(E):
        a, b = map(int, input().split())
        nodes[a].append(b)

    S, G = map(int, input().split())

    print(f'#{t + 1} {dfs(S, G, V, nodes)}')