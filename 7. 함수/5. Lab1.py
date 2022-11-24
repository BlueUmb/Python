'''
    세개의 정수를 인자로 받아
    합계와 평균을 출력해주는 함수를 만드시오
    예) 합계 :     평균:
'''
# def calculate(a,b,c):
#     print("합계 :",a+b+c,"평균 :",(a+b+c)/3)
#
# a = int(input(">>>"))
# b = int(input(">>>"))
# c = int(input(">>>"))
#
# calculate(a,b,c)


def calculate(num):
    sum=0
    for i in num:
        sum+=i
    avg=sum/len(num)
    print(f"합계:{sum} 평균:{avg}")


num = []
print("음수를 입력하면 입력종료")
while True:
    input_num = int(input(">>>"))

    if input_num < 0:
        break

    num.append(input_num)

calculate(num)
