class A:
    def __init__(self, life, attack):
        self.life = life
        self.attack = attack
    def Attack(self, a):
        a.cut_life(self.attack)
    def cut_life(self,num):
        self.life -= num
class person(A):
    def __init__(self, name, life, attack):
        self.name = name
        super().__init__(life, attack)
class dog(A):
    def __init__(self, name, life, attack):
        self.name = name
        super().__init__(life, attack)
p1 = person('张胜祥', 220 , 20)
p2 = person('袁天凯', 200 , 40)
d1 = dog('二哈', 100, 40)
d2 = dog('金毛', 120, 50)
d3 = dog('柯基', 90, 35)
