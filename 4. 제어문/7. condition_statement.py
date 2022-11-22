origin_pass = "0111"
pwd = input("비밀번호를 입력하세요>>> ")
if(pwd == origin_pass):
    print("로그인 성공!")
elif(pwd == ""):
    print("아무것도 입력하지 않았습니다")
else:
    print("로그인 실패")