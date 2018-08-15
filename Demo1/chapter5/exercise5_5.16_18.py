class A(type):
    def __new__(cls, name, bases, attrs):
        Attrs = {}
        for k, v in attrs.items():
            Attrs[k.upper()] = v
        return type.__new__(cls, name, bases, Attrs)
class person(metaclass=A):
    name = 'person'
    tag = 'legend'
    def walk(self):
        print('kkkk')
p = person()
print(p.__dict__)
print(person.__dict__)