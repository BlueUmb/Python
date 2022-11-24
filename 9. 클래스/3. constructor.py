# 생성자 : 인스턴스를 만들때 호출되는 메서드

class Monster:
    def __init__(self,health,attack,speed):
        self.health = health
        self.attack = attack
        self.speed = speed

    def decrease_health(self,num):
        print(f"{num}데미지!")
        print(self.health,"-",num)
        self.health -= num

    def get_health(self):
        return self.health

goblin = Monster(800,120,300)
print(goblin.get_health())
goblin.decrease_health(100)
print(goblin.get_health())

wolf = Monster(1900, 220, 800)
wolf.decrease_health(600)
print(f"늑대의 남은 체력 {wolf.get_health()}")
