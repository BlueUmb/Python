# 기본형
# 정의하기
def printHello():
    print("Hello Ezen!")

# 호출하기
printHello()

# 매개변수가 있는 함수
def sum(a, b):
    print(a+b)

sum(1,4)

# 반환값이 있는 함수
import random as ran

def getRandomnumber():
    return ran.randint(1,10)

print(getRandomnumber())


def add(a,b):
    return a+b

print(add(5,6))