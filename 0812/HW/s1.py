dict = {'ZRO': 0, 'ONE': 1, 'TWO': 2, 'THR': 3, 'FOR': 4, 'FIV': 5, 'SIX': 6, 'SVN': 7, 'EGT': 8, 'NIN': 9}

def my_sort(list_in):
    leng = 0
    for i in list_in:
        leng += 1
    
    for j in range(leng - 1, 0, -1):
        for k in range(j):
            if list_in[k] > list_in[k + 1]:
                list_in[k], list_in[k + 1] = list_in[k + 1], list_in[k]
    return list_in

def to_num(str_in):
    return dict[str_in]

def to_oigye(num):
    for key, value in dict.items():
        if value == num:
            return key

T = int(input())

for t in range(T):
    head, leng = map(str, input().split())
    list_num = my_sort(list(map(to_num, input().split())))
    
    res = []
    for i in list_num:
        res.append(to_oigye(i))

    print(f'{head}', end=' ')
    print(*res)