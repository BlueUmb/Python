'''
    순신은 lily라는 이름의 교환학생과 친해지게 되었습니다.
    영어를 잘하지못하는 순신은 lily에게 한국어를 가르쳐 주기 위해
    한국어 연습 프로그램을 만들게 되었습니다.
        - 연습할 한국어가 담긴 리스트를 만든다
        - 리스트에서 순서대로 단어를 가져와 화면에 출력
        - 프로그램 사용자는 단어를 그대로 입력하고
        - 맞추면 다음 단어를 가져온다 , 틀리면 프로그램 종료
'''
def Learning (wrong_count):
    # for문 이용
    for i in word_list:
        print(i)
        answer = input(">>> ")
        if answer != i:
            print("Wrong!!")
            # break
            wrong_count += 1
    print("전체 문제 개수 :", str(len(word_list)) + "개")
    print("맞힌 문제 개수 :", str(len(word_list) - wrong_count) + "개")
    print("틀린 문제 개수 :", str(wrong_count) + "개")

word_list = ["사랑해","귀엽다","고마워","행복해"]
print("Let's Learning Korean")

wrong_count = 0

Learning(wrong_count)
# while문이용

# i = 0
# while word_list:
#     if i>=len(word_list):
#         i=0
#     print(word_list[i])
#     answer = input(">>> ")
#     if answer != word_list[i]:
#         print("Wrong!!")
#         break
#     i+=1


