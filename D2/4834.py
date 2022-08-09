T = int(input())

for t in range(T) :
    length = int(input())
    card = input()
    nums = [0] * 10
    max = nums[0]
    ans = 0

    for i in range(length) : # 카드 번호에 해당하는 숫자 카운팅
        nums[int(card[i])] += 1
    
    for j in range(10) : # 횟수 최댓값 (혹은 숫자 최댓값) 최신화
        if max <= nums[j] :
            max = nums[j]
            ans = j

    print(f'#{t+1} {ans} {nums[ans]}') #쁘린뜨!