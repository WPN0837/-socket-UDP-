class A(type):
    def __call__(self,*args,**kwargs):
        obj = self.__new__(self)
        for k, v in kwargs.items():
            obj.__dict__[k] = v
        return obj
class B(metaclass=A):
    def walk(self):
        print('BBBBB')
b=B(name = '123')
print(b.name)
b.walk()