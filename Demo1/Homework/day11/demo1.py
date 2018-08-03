'''
编写函数，（函数执行的时间是随机的）
'''
import random
import time
def func():
    print('开始')
    time1 = random.randint(1,10)
    time.sleep(time1)
    print('结束')
func()