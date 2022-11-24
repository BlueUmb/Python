'''
    로또 예상 번호 추출 프로그램을 구현
    다음 조건에 따라 프로그램을 완성해 보시오
        1) 로또 번호 6개 생성
        2) 로또 번호는 1~45까지의 랜덤수
        3) 6개의 숫자중 중복되는 번호는 없어야함
        4) get_random_number() 함수를 사용하여 구현한다

        출력 예) 1 8 11 13 26 42
        정렬, 중복체크
'''

import random as ran

def get_Lotto_number():
    return ran.randint(1,45)

# def check_overlap(ranNum,num):
#     if ranNum not in num:
#         num.append(ranNum)

#while len(lottoNum) < 6:
#     check_overlap(get_Lotto_number(),lottoNum)
# lottoNum.sort()
# print(lottoNum)


def check_overlap(ranNum,num,index):
    if ranNum not in num[index]:
        num[index].append(ranNum)

lottoNum = []
for i in range(5):
    lottoNum.append([])

index=0
while True:
    check_overlap(get_Lotto_number(),lottoNum,index)
    if len(lottoNum[index])==6:
        index+=1
    if len(lottoNum[index]) and index ==6:
        break


for i in range(5):
    print(lottoNum[i])


