def r_p_c(x, y) :
    win = {"가위" : "보", "바위" : "가위", "보" : "바위"}
    if x == y :
        print("비겼습니다!")
    else :
        if win[x] == y :
            print ("{0}가 이겼습니다!".format(a))
        else :
            print ("{0}가 이겼습니다!".format(b))

user00, user01 = input(), input()
x, y = input(), input()
r_p_c (x, y)