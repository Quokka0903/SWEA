def gazua(nodes):
    visited = [0] * 101
    stack = []
    s = 0
    while True:

        for w in nodes[s]:
            if w == 99:
                return (1)
            if visited[w] == 0:
                stack.append(s)
                visited[w] = 1
                s = w
                break
        else :
            if stack:
                s = stack.pop()
            else:
                return (0)


for _ in range(10):
    t, gil = map(int, input().split())
    ssang = list(map(int, input().split()))
    nodes = [[] for _ in range(101)]
    
    for i in range(gil):
        nodes[ssang[i * 2]].append(ssang[i * 2 + 1])

    print(f'#{t} {gazua(nodes)}')