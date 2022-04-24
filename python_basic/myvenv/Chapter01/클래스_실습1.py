class item:
    def __init__(self, name, price,weight,isdropable):
        self.name = name
        self.price = price;
        self.weight = weight;
        self.isdropable = isdropable;
    def sale(self):
        print(f"{self.name} 판매가격은 {self.price}")
    def discard(self):
        if self.isdropable == True:
            print(f"{self.name}을 버렸습니다.")
        else:
            print(f"{self.name}을 버릴 수 없습니다")

class WearableItem(item):
    def __init__(self, name, price, weight, isdropable,effect):
        super().__init__(name, price, weight, isdropable)
        self.effect = effect
    def wear(self):
        print(f"{self.name}을 착용했다! {self.effect} 효과 적용되었다!")

class UsableItem(item):
    def __init__(self,name, price, weight, isdropable, effect):
        super().__init__(name,price,weight,isdropable)
        self.effect = effect;
    def use(self):
        print(f"{self.name}을 사용했다! {self.effect}효과가 활성화되었다!")


#인스턴스 생성

sword = WearableItem("기적의검", 30000, 5, True, "공격력 300증가")
sword.wear()
sword.sale()
sword.discard()

potion = UsableItem("체력물약", 2000, 1, False, "체력 100 회복")
potion.use()
potion.sale()
potion.discard()