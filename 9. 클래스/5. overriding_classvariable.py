'''
    상속의 업그레이드
        - 클래스 변수 (인스턴스들이 모두 공유하는 변수)

        -예
            드래곤 클래스에 인스턴스 속성을 추가하기
            부모클래스에 클래스변수 추가하기
'''

import random as ran

class Monster:
    max_num = 1000

    def __init__(self,name,health,attack):
        self.name = name
        self.health = health
        self.attack = attack
        Monster.max_num -= 1

    def move(self):
        print(f"[{self.name}] 지상에서 이동하기")

    def print_count(self):
        print(self.max_num)


class Wolf(Monster):
    pass

class Shark(Monster):
    def move(self):
        print(f"[{self.name}] 헤엄치기")

class Dragon(Monster):
    #생성자 오버라이딩
    def __init__(self,name,health,attack):
        super().__init__(name,health,attack)
        self.skills = ("불뿜기","꼬리치기", "날개치기")

    def move(self):
        print(f"[{self.name}] 날아가기")

    def skill(self):
        print(f"{self.name} 스킬사용 {self.skills[ran.randint(0,2)]}")

wolf = Wolf("울프",1500,200)
wolf.move()
print(wolf.max_num)

shark = Shark("샤크", 3000, 400)
shark.move()
print(shark.max_num)

dragon = Dragon("드래곤", 8000, 800)
dragon.move()
dragon.skill()
print(dragon.max_num)
