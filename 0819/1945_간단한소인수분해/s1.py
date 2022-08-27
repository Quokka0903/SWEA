soinsu = [2, 3, 5, 7, 11]               # 나눌 친구들

T = int(input())

for t in range(T):
    test = int(input())
    res = [0, 0, 0, 0, 0]               # 카운팅할 리스트

    for i in range(5):
        while test % soinsu[i] == 0:    # 나눌 친구들로 나눠지면!
            res[i] += 1                 # 카운팅하고!
            test = test // soinsu[i]    # 숫자를 줄이고!

    print(f'#{t + 1}', end=' ')
    print(*res)