for _ in range(10):
    t = int(input())
    nums = list(map(int, input().split()))
    
    while True:
        flag = 0
        for x in range(1, 6):
            nums[0] -= x
            nums.append(nums.pop(0))
            if nums[-1] <= 0:
                nums[-1] = 0
                flag = 1
                break
        
        if flag:
            print(f'#{t}', end = ' ')
            print(*nums)
            break