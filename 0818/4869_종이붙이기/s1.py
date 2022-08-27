res = [0] * 51

res[1] = 1
res[2] = 3
res[3] = 5

for i in range(4, 51):
    res[i] = res[i - 1] + (2 * res[i - 2])

T = int(input())

for t in range(T):
    print(f'#{t + 1} {res[int(input())//10]}')
