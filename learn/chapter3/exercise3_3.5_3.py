V = False
info = {'alex':'abc123'}
def dec(func):
    def dec_func():
        if V:
            func()
        else:
            print('请登陆后查看！')
    return dec_func
@dec
def show():
    print('显示内容。。。。')
@dec
def category():
    print('显示分类。。。')
def login(username, password):
    global V
    if username in info:
        if password == info[username]:
            V = True
            return 1
        else:
            print('密码错误！')
            return 0
    else:
        print('用户名不存在！')
        return 0
if __name__ == '__main__':
    while True:
        print(
    '''
    0.退出
    1.登录
    2.显示内容
    3.显示分类
    '''
        )
        c = input('选择：')
        if c == '0':
            break
        elif c == '1':
            if not V:
                name = input('用户名：')
                password = input('密码：')
                login(name, password)
        elif c == '2':
            show()
        elif c == '3':
            category()
        else:
            print('输入错误！')
