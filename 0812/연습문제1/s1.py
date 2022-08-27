def chr_rev00(char):
    res = ''
    for i in range(len(char)):
        res += char[-i - 1]
    return res


def chr_rev01(char):
    res = list(char)
    for i in range(len(res) // 2):
        res[i], res[-i - 1] = res[-i - 1], res[i]
    return ''.join(res)


T = int(input())

for t in range(T):
    test = input()
    print(f'#{t+1} {chr_rev00(test)}')