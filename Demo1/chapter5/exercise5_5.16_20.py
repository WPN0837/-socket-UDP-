class student:
    count = 0
    def __init__(self, name):
        self.name = name
        student.count += 1
s = student('张胜祥')
print(student.count)