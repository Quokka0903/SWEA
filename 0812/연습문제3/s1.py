def self_find(pat, tar):
    P = len(pat)
    T = len(tar)

    pi, ti = 0, 0
    cnt = 0

    while ti < T:
    
        if pat[pi] != tar[ti]:
            ti = ti - pi
            pi = 0
        

        else :
            pi += 1
            if pi == P:
                cnt += 1
                pi = 0

        ti += 1 

    return cnt

for _ in range(10):
    t = int(input())
    pat = input()
    tar = input()
    print(f'#{t} {self_find(pat, tar)}')
