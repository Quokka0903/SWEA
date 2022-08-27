N = int(input())
arr = list(map(int, input().split()))

# 카운팅 정렬
temp = [0] * N
c = [0] * 101
for i in range(N) : #카운트
    c[arr[i]] += 1

for j in range(1, 101) : #개수 누적
    c[j] += c[j-1]

for i in range(N-1, -1, -1) : #원본을 뒤에서부터 읽으면서 정렬 결과를 temp에 저장
    c[arr[i]] -= 1
    temp[c[arr[i]]] = arr[i]

print(temp)


# 버블 정렬
for i in range(N-1, 0, -1) : # 구간의 맨 끝 인덱스
    for j in range(i): # 인접원소 중 왼쪽 원소 인덱스
        if arr[j] > arr[j+1] : # 오름차순, 더 큰 수를 오른쪽으로
            arr[j], arr[j+1] = arr[j+1], arr[j]

print(arr)