T = int(input())

for t in range(T):
    str1 = input()
    str2 = input()

    cnt = {}
    max = 0
    for text1 in str1:
        cnt[text1] = 0
        for text2 in str2:
            if text1 == text2:
                cnt[text1] += 1
        if max < cnt[text1]:
            max = cnt[text1]
    
    print(f'#{t + 1} {max}')
