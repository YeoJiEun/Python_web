#print(f"{name}")  //fstring 출력
# class 이름 :
#   def 메서드 이름(self):
#       명령어 

# 인스턴스 = 클래스 이름()
# 인스턴스.메서드() 

#인스턴스 = 객체 
import random

class Monster: 
    def say(self):
        print('나는 몬스터입니다.')

instance = Monster()
instance.say()


#파이썬은 자료형도 클래스다. 

a = 10
b = "문자열"
c = True
print(type(a) )
print(type(b) )
print(type(c) )

print(b.__dir__()) #문자열 객체안의 메서드 리스트를 확인 할 수 있다.


#자식클래스 정의
class Wolf(Monster): # monster 클래스를 를 상속받음
    pass 

#monster상속 및 오버라이딩(재정의)
class Shark(Monster):
    def move(self):
        print('헤엄치기')


class Monster:
    max_num = 1000
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack
        Monster.max_num -= 1 #몬스터 한번 생성 할때마다 -1
    def move(self):
        print(f"[{self.name}] 지상에서 이동하기")

#자식 클래스
class wolf(Monster): 
    pass

class Shark(Monster):
    def move(self): # 메소드 오버라이딩
        print(f"[{self.name}] 헤엄치기!")

class Dragon(Monster):
    def __init__(self,name, health, attack, skill):
        super().__init__(name, health, attack) # 부모 (상속해준 클래스) 의 초기 init을 불러옴
        self.skill = skill

    #def __init__(self,name, health, attack):
    #    super().__init__(name, health, attack) # 부모 (상속해준 클래스) 의 초기 init을 불러옴
    #    self.skill = ('파이어볼','아이스볼','썬더볼')
    def move(self):
        print(f"[{self.name}] 날아오르기!")
    
    def useSkill(self):
        print(f"[{self.skill[random.randint(0,2)]}] 스킬을 사용함 !")

wolf = wolf("늑대", 3000, 200)
wolf.move()

shark = Shark("아기상어", 3400, 400)
shark.move()

dragon = Dragon("아기용", 2000,300, ("파이어볼", "아이스볼", "썬더볼"))
#dragon = Dragon("아기용", 2000,300)
dragon.move()
dragon.useSkill()

