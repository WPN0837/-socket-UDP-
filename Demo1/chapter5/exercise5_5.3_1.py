class student:
    count = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.count += 1
    def __str__(self):
        return self.name + ' ' + str(self.age)
s1 = student('','')
print(s1.__str__())
print(s1.count)
s2 = student('', '')
print(s1.count)
