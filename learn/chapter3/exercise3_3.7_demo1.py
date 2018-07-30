'''
计算传入数字的和
'''
def f(*args):
    num = 0
    for i in args:
        num += int(i)
    return num
if __name__ == '__main__':
    print(f('1', 2, '3'))
