'''
    if

    if-else

    if-elif

    if-elif-else

'''
while True:
    money = int(input("현재 가진 금액 입력 >>>"))
    if money < 0:
        break;
    if money >= 20000:
        print("치킨")
    elif money >= 10000:
        print("떡볶이")
    elif money >= 3000:
        print("편의점 김밥")
    else:
        print("굶기")





