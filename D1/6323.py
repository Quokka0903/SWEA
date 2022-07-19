N = int(input())
L = [0] * N
L[0], L[1] = 1, 1
for i in range(2, N) :
    L[i] = L[i - 1] + L[i - 2]
print(L)