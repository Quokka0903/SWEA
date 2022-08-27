for t in range(int(input())):
    N = int(input())
    noseon = [0] * (1001)
    for i in range(N):
        type, A, B = map(int, input().split())
        if type == 1:
            for j in range(A + 1, B):
                noseon[j] += 1
        elif type == 2:
            for j in range(A + 2, B, 2):
                noseon[j] += 1
        elif type == 3:
            if A % 2 == 0:
                for k in range(A + 1, B):
                    if k % 4 == 0:
                        noseon[k] += 1
            else:
                for k in range(A + 1, B):
                    if k % 3 == 0 and k % 10 != 0:
                        noseon[k] += 1
        noseon[A] += 1                        
        noseon[B] += 1

    max_noseon = 0
    for case in noseon:
        if case >= max_noseon:
            max_noseon = case
    
    print(f'#{t + 1} {max_noseon}')