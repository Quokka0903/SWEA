def my_len(a):                                              # 배열 길이 구하는 메소드
    res = 0
    for _ in a:
        res += 1
    return res


T = int(input())

for t in range(T):
    N, M = map(int, input().split())
    pizza = list(map(int, input().split()))
    
    sunseo = []                                             # 피자 번호와 치즈 양
    for idx, unit in enumerate(pizza):
        sunseo.append([idx + 1, unit])

    hwadeok = [None] * N
    chulgu = 0                                              # 화덕 출입구 위치
    yamyam = []                                             # 나온 피자의 번호
    while True:
        if hwadeok[chulgu]:                                 # 출입구 위치일 때
            hwadeok[chulgu][1] = hwadeok[chulgu][1] // 2    # 치즈 녹이고
            if hwadeok[chulgu][1] == 0:                     # 다 녹았으면
                yamyam.append(hwadeok[chulgu][0])           # 냠냠하러가고
                if my_len(yamyam) == M:                     # 다 나왔으면
                    break                                   # 브레이크
                hwadeok[chulgu] = None                      # 빼낸 화구는 초기화

        if sunseo and not hwadeok[chulgu]:                  # 넣을 피자 있고 화구에 뭐가 없으면
            hwadeok[chulgu] = sunseo.pop(0)                 # 거기다 피자 넣기
        
        chulgu += 1                                         # 출구 이동
        if chulgu == N:
            chulgu = 0

    print(f'#{t + 1} {yamyam[-1]}')                         # 마지막 나온 피자 번호 출력