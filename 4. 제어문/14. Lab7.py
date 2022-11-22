'''
    사용자로부터 국어, 수학, 영어 성적이 입력됩니다.
    세 과목의 평균점수가 80이상이면 합격입니다
    하지만 프로그램의 오류가 발생했습니다
    80점 이상일 경우 불합격이 표시되도록 프로그램을 작성해보시오
    (단 , 0점에서 100점 사이의 숫자를 입력하지 않으면 "잘못입력했습니다"출력
'''

# korean = int(input("국어 >>> "))
# math = int(input("수학 >>> "))
# english = int(input("영어 >>> "))
# if 0 <= korean <= 100 and 0 <= math <= 100 and 0 <= english <= 100:
#     if (korean+math+english)/3 >= 80 :
#         print((korean+math+english)/3,"점 불합격")
#     else:
#         print((korean+math+english)/3,"점 합격")
# else:
#     print("잘못 입력하셨습니다")

subject = ["국어","수학","영어"]
sum = 0
success = True;
for i in subject:
    score = int(input(i +" >>> "))
    if 0 <= score <= 100:
        sum += score
    else:
        print("잘못 입력하셨습니다");
        success=False;
        break
if success :
    if sum/len(subject) >= 80:
        print(sum/len(subject),"점 불합격")
    else:
        print(sum/len(subject),"점 합격")

