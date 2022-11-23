'''
    1. while 사용법
    초기식
    while 조건식 :
        반복할 명령
        증감식

    2. 무한루프와 break
    while True :
        반복할 명령

        if 조건식:
            break
'''

i =0
while i<10:
    print(i,"번째 다짐.")
    i += 2

while True:
    x = input("종료하려면 'exit'를 입력하세요 >>> ")
    if x=="exit":
        print("종료")
        break
    print(x)