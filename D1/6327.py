A = list(map(int, input().split(', ')))
for i in range(len(A)) :
    print("square({0}) => {1}".format(A[i], A[i]**2))