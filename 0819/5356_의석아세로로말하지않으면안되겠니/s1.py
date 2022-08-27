def my_len(a):
    res = 0
    for i in a:
        res += 1
    return res

T = int(input())

for t in range(T):
    sero = [[] for _ in range(15)]
    for _ in range(5):
        text = input()

        for i in range(my_len(text)):
            sero[i].append(text[i])
    
    print(f'#{t + 1}', end = ' ')
    for res in sero:
        print(''.join(res), end = '')
    print()