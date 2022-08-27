def my_itoa01(n, out):
    chk = ''
    if n < 0:
        chk += '-'
        n = -n

    res = ''
    while n > 0:
        res += chr(48 + n % 10)
        n = n // 10

    res += chk

    for i in range(len(res)):
        out += res[-i - 1]

    return (out)

T = int(input())

for t in range(T):
    res = ''
    ans = my_itoa01(int(input()), res)
    print(f'#{t+1} {ans} {type(ans)}')