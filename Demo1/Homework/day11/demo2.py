'''
编写装饰器，为函数加上统计时间的功能
'''
import time
import random
def zhuangshiqi(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        res = func(*args, **kwargs)
        print('运行了%s秒'% (time.time() - start_time))
        return res
    return wrapper
@zhuangshiqi
def func():
    print('开始')
    time1 = random.randint(1, 10)
    time.sleep(time1)
    print('结束')
func()