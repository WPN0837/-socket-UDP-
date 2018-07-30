'''
检查用户传入的对象的元素是否含有空内容
'''
def V(I):
    for i in I:
        if len(i) == 0:
            print('空')
        else:
            print('非空')
if __name__ == '__main__':
    V(['1', '2', ''])