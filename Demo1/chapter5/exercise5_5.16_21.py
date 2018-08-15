class B:
    def handle(self):
        print('B', self.handle.__name__)
class A(B):
    def handle(self):
        B.handle(self)
        print('A', A.handle.__name__)
a = A()
a.handle()