T = int(input())
for t in range(T) :
    N = int(input())
    noseon = [0] * 5000 # 버스 정류장 초기화
    for i in range(N) :
        a_left, a_right = map(int, input().split())
        for k in range(a_left - 1, a_right) : # 버스 정류장 카운팅
            noseon[k] += 1

    P = int(input())
    print(f'#{t+1}', end=' ')
    for j in range(P-1) : # 인풋받는 버스 정류장 번호별로 해당 밸류 반환
        print(f'{noseon[int(input()) - 1]}', end=' ')
    print(f'{noseon[int(input()) - 1]}')