class hero:
    def __init__(self, name, attack, life_value):
        pass
    def attack_value(self, hero):
        pass
class dema(hero):
    def __init__(self, attack, life_value, name = 'dema'):
        self.name = name
        self.attack = attack
        self.life_value = life_value
    def attack_value(self, hero):
        hero.life_value -= self.attack
    def __str__(self):
        return self.name, self.life_value
class rui_wen(hero):
    def __init__(self, attack, life_value, name = 'ruiwen'):
        self.name = name
        self.attack = attack
        self.life_value = life_value
    def attack_value(self, hero):
        hero.life_value -= self.attack
    def __str__(self):
        return self.name, self.life_value
DM = dema(50, 100)
RW = rui_wen(70, 80)
DM.attack_value(RW)
print(DM.__str__())
print(RW.__str__())