'''
自定义生成器 实现 range功能
'''
def func(*args):
    num = 0
    stage = 1
    if len(args) == 1:
        while num < args[0]:
            yield num
            num += stage
    elif len(args) == 2:
        num = args[0]
        while num < args[1]:
            yield num
            num += stage
    elif len(args) == 3:
        num = args[0]
        stage = args[2]
        while num < args[1]:
            yield num
            num += stage
    else:
        print('错误')
for i in func(10):
    print(i)