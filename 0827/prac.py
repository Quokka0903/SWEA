T = int(input())

for test_case in range(1, T+1):
    graph_sero, graph_garo = map(int,input().split())

    arr = [list(map(int, input().split())) for _ in range(graph_sero)]
    if graph_garo > graph_sero:
        for i in range(graph_garo - graph_sero):
            arr.append([0] * graph_garo)
    elif graph_garo < graph_sero:
        for i in range(len(arr)):
            arr[i] = arr[i] + [0] * (graph_sero - graph_garo)
    print(arr)
    max_len = 0
    # 가로일 때
    for i in range(graph_sero):
        count_garo = 0
        for j in range(graph_garo):
            # 가로일 때
            if arr[i][j] == 1:
                count_garo += 1
            else:
                max_len = max(max_len, count_garo)
                count_garo = 0
        max_len = max(max_len, count_garo)

    # 세로일 때
    for i in range(graph_garo):
        count_sero = 0
        for j in range(graph_sero):
            # 세로일때
            if arr[j][i] == 1:
                count_sero += 1
            else:
                max_len = max(max_len, count_sero)
                count_sero = 0
        max_len = max(max_len, count_sero)

    print(f'#{test_case} {max_len}')