P = int(input())

for i in range(2, P) :
    if P % i == 0 :
        return ("소수가 아닙니다.")
print("소수입니다.")