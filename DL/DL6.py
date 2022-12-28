'''
    1. 클래스는 딥러닝 프로그램을 작성할때 자주 사용됨.

    2. self
        - 인스턴스(instance) 자기 자신을 의미함
'''


class Human:
    def __init__(self):
        self.age = 0

    def old(self):
        self.age += 1


# 인스턴스 생성
human1 = Human()  # 기본생성자 __init__ 호출
human2 = Human()

for i in range(10):
    human1.old()

print(human1.age)

for i in range(20):
    human2.old()

print("human2의 나이는 : ", human2.age)

print()


class Student:
    def __init__(self, id, name, age, gender, department):
        self.id = id
        self.name = name
        self.age = age
        self.gender = gender
        self.department = department

    def show(self):
        print("=====학생 정보=====")
        print(f"학번 : {self.id}")
        print(f"이름 : {self.name}")
        print(f"나이 : {self.age}")
        print(f"성별 : {self.gender}")
        print(f"학과 : {self.department}")

    def add_age(self, offset):
        self.age += offset


student1 = Student("20221228", "이순신", 20, "남성", "컴퓨터공학")
student2 = Student("20221229", "신사임당", 30, "여성", "디자인공학")
student3 = Student("20221230", "진도준", 37, "남성", "법학")

student1.show()
student2.show()
student3.show()

print()

student1.add_age(5)
student1.show()

print()
class Client:
    client_cnt = 0

    def __init__(self, id, name, age, gender, point):
        self.id = id
        self.name = name
        self.age = age
        self.gender = gender
        self.point = point
        Client.client_cnt +=1

    def show(self):
        print("=====고객 정보=====")
        print(f"고객 번호 : {self.id}")
        print(f"고객 이름 : {self.name}")
        print(f"고객 나이 : {self.age}")
        print(f"고객 성별 : {self.gender}")
        print(f"고객 점수 : {self.point}")
        # print(f"현재 총 고객수 : {self.client_cnt}")

client1 = Client(1, "이순신", 20, "남성", 1000)
client2 = Client(2, "이도", 21, "남성", 500)
client3 = Client(3, "신사임당", 23, "여성", 2000)

client1.show()
client2.show()
client3.show()

print()
print(f"현재 총 고객수 : {Client.client_cnt}")