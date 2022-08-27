def max_self (list) : # max 구현
    res = 0
    for unit in list :
        if res < unit :
            res = unit
    return res

def min_self (list) : # min 구현
    res = list[0] # 리스트 내 아무 값이나 넣었음.
    for unit in list :
        if res > unit :
            res = unit
    return res


T = int(input())
for t in range(1, T + 1):
    idx = int(input())
    res = list(map(int, input().split()))
    print(f'#{t} {max_self(res) - min_self(res)}') # max - min