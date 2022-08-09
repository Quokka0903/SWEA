def min_max_index (list) :
    idx, max_i, min_i = 0, 0, 0 # 전달받은 리스트의 최댓값과 최솟값 인덱스 반환하는 함수
    for i in list :
        if list[max_i] < i :
            max_i = idx
        elif list[min_i] > i :
            min_i = idx
        idx += 1
    return (max_i, min_i)


def flat (dumps, list) : # 평탄화 후 최댓값과 최솟값 차를 반환하는 함수
    
    for _ in range(dumps) :
        max_i, min_i = min_max_index(list)
        list[max_i] -= 1
        list[min_i] += 1

    max_ans, min_ans = min_max_index(list)
    return list[max_ans] - list[min_ans]
        

for t in range(10) :
    dumps = int(input())
    boxes = list(map(int, input().split()))
    
    print(f'#{t+1} {flat(dumps, boxes)}') # 함수 호출하여 출력
