def sum_of_interval (list) :
    
    len, sum = 0, 0
    for num in list : # 리스트 원소 총합과 리스트 길이 구함
        len += 1
        sum += num

    for i in range(len-1, 0, -1) : # 리스트 버블정렬
        for j in range(i) :
            if list[j] > list[j+1] :
                list[j], list[j+1] = list[j+1], list[j]

    left, right = 0, len-1 # 투포인터 초기화

    while left < right :
        if sum == 0 : # 합이 0이면 리턴
            return 1
        else :  # 0보다 큰 값일 경우, 보다 큰 값을 제하는 쪽으로 이동
            if sum > 0 :
                if list[left] > list[right] :
                    sum -= list[left]
                    left += 1
                else :
                    sum -= list[right]
                    right -= 1
                # 0보다 작은 값일 경우, 보다 작은 값을 제하는 쪽으로 이동
            else :
                if list[left] < list[right] :
                    sum -= list[left]
                    left += 1
                else :
                    sum -= list[right]
                    right -= 1
    return 0 # 투포인터가 만날 때까지 값이 나오지 않으면 0 리턴

T = int(input())

for t in range(T) :
    list_test = list(map(int, input().split()))
    print(f'#{t+1} {sum_of_interval(list_test)}')
