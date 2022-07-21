T = int(input())

for test_case in range(1, T + 1):
    print(f'#{test_case}')
    money = int(input())
    list = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    for i in list :
        cnt = money // i
        print(cnt, end = ' ')
        money -= cnt * i
    print()