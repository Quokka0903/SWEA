def my_len(a):
    res = 0
    for i in a:
        res += 1
    return res

T = int(input())

for t in range(T):
    str1 = input()
    str2 = input()

    res = 0
    for i in range(my_len(str2)):
        if str2[i:i + my_len(str1)] == str1:
            res = 1
            break
        res = 0

    print(f'#{t + 1} {res}')