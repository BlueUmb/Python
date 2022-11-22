print("BMI 계산기 입니다.")
height = int(input("신장 : "))
weight = int(input("몸무게 : "))
bmi = round(weight / (height/100)**2,2)
print("BMI지수 : ",bmi)
if bmi<=18.5:
    print("저체중")
elif bmi<=22.9:
    print("정상")
elif bmi<=24.9 :
    print("과체중")
else:
    print("비만")