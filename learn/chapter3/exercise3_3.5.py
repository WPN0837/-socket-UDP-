import time
def dec(func):
    def dec_func():
        start_time = time.time()
        func()
        print(time.time() - start_time)
    return dec_func
@dec
def fun1():
    time.sleep(1)
    print('%s' % fun1.__name__)
@dec
def fun2():
    time.sleep(2)
    print('%s' % fun2.__name__)
@dec
def fun3():
    time.sleep(3)
    print('%s' % fun3.__name__)

if __name__ == '__main__':
    fun1()
    fun2()
    fun3()