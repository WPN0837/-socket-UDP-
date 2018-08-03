'''
求文件a.txt中总共包含的字符个数？思考为何在第一次之后的n次sum求和得到的结果为0？（需要使用sum函数）
'''
def f():
    with open('a.txt', 'r', encoding='utf-8')as info:
        res = info.read()
    return res
if __name__ == '__main__':
    print(len(f()))