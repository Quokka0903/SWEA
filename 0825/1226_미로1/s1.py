for _ in range(10):
    t = int(input())
    miro = [input() for _ in range(16)]                     # miro 생성
    visited = [[0] * 16 for _ in range(16)]                 # miro가 문자열이라 수정안되므로 따로 만듦

    s = ()          
    for y in range(16):         
        for x in range(16):         
            if miro[y][x] == '2':                           # 출발점 찾으면
                s = (y, x)                                  # 위치 튜플로 저장
                visited[y][x] = 1                           # 방문체크
                break           

    flag = 0                                                # 각 재기 선언
    stack = [s]         
    while stack:            
        s = stack.pop(0)                                    # 스택값 가져와서
        for i, j in [[1, 0], [-1, 0], [0, 1], [0, -1]]:     # 델타 탐색 중에 방문 안한 통로면
            if miro[s[0] + i][s[1] + j] == '0' and visited[s[0] + i][s[1] + j] == 0:
                stack.append((s[0] + i, s[1] + j))          # 스택에 넣고
                visited[s[0] + i][s[1] + j] = 1             # 방문체크
            elif miro[s[0] + i][s[1] + j] == '3':           # 도착지점이면
                flag = 1                                    # 각 세우고 탈출
                break
        
        if flag:                                            # 각 세워졌으면 탈출
            break

    print(f'#{t} {flag}')                                   # 결과값 출력