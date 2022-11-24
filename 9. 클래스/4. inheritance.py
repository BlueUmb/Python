'''
    1. 상속 : 클래스들에 중복된 코드를 제거하고 유지보수를 편하게 하기 위해서 사용

                    몬스터
        땅몬스터    물몬스터    공중몬스터

    2. 부모클래스 정의
        - 속성
            - 이름, 체력, 공격력
        - 함수
            - 이동하기(move)

'''
class Monster:
    def __init__(self,name,health,attack):
        self.name = name
        self.health = health
        self.attack = attack

    def move(self):
        print(f"[{self.name}] 이동하기")

goblin = Monster("goblin",200,10)
goblin.move()

class Wolf(Monster):
    pass

class Shark(Monster):
    def move(self):
        print(f"[{self.name}] 헤엄치기")

class Dragon(Monster):
    def move(self):
        print(f"[{self.name}] 날아가기")

shark = Shark("shark",100,10)
shark.move()

dragon = Dragon("dragon",100,10)
dragon.move()

wolf = Wolf("wolf",6500,210)
wolf.move()