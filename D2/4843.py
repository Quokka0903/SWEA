T = int(input())
for t in range(1, T + 1):
    idx = int(input())
    left, right = 0, idx - 1
    nums = list(map(int, input().split()))
    nums.sort()
    ans = []
    while left < 5 and  right > idx - 6:
        ans.append(nums[right])
        ans.append(nums[left])
        
        left += 1
        right -= 1
    
    ans = ' '.join(map(str, ans))
    print(f'#{t} {ans}')