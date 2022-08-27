def my_len(a):
    leng = 0
    for x in a:
        leng += 1
    return leng


def gualho(list_a):
    my_stack = []
    dict = {')' : '('}

    for x in list_a:

        my_stack.append(x)

        if x in dict:
            
            if my_len(my_stack) > 1 and my_stack[-2] == dict[my_stack[-1]]:
                my_stack.pop()
                my_stack.pop()
            else :
                return -1
        
    
    return -1 if my_stack else 1


T = int(input())

for t in range(T):
    test = input()
    print(f'#{t + 1} {gualho(test)}')