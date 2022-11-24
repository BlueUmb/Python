'''
    상속의 업그레이드
        - 클래스 변수 (인스턴스들이 모두 공유하는 변수)

        -예
            드래곤 클래스에 인스턴스 속성을 추가하기
            부모클래스에 클래스변수 추가하기
'''

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


goblin = Monster("goblin",200,10)
goblin.print_count()
goblin.move()

shark = Monster("shark",200,10)
shark.print_count()
shark.move()