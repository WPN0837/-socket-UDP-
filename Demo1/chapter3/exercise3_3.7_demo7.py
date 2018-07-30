def area(*args):
    def 圆形(r):
        print(3.14 * r**2)
    def 正方形(r):
        print(r**2)
    def 长方形(c, k):
        print(c * k)
    if args[0] =='圆形':
        圆形(int(args[1]))
    elif args[0] == '正方形':
        正方形(int(args[1]))
    elif args[0] == '长方形':
        长方形(int(args[1]), int(args[2]))
    else:
        print('参数错误！')
if __name__ == '__main__':
    area('圆形', 5)
    area('正方形', 5)
    area('长方形', 3, 5)