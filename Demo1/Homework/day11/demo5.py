'''
编写装饰器，为多个函数加上认证功能，要求登录成功一次，在超时时间内无需重复登录，超过了超时时间，则必须重新登录
'''
import time
session = {}
def zhuangshiqi(func):
    def wrapper(*args, **kwargs):
        res = None
        if session:
            if time.time() - session['login_time'] > 3:#30min
                print('超过时间，请重新登陆。')
                session.clear()
                login()
            else:
                res = func(*args, **kwargs)
                session['login_time'] = time.time()
        else:
            print('未登陆')
            login()
        return res
    return wrapper
@zhuangshiqi
def func():
    print('程序功能!')

def login():
    while True:
        username = input('用户名：')
        password = input('密码：')
        if username == 'egon' and password == 'abc123':
            session['name'] = username
            session['login_time'] = time.time()
            print('登陆成功')
            return True
        else:
            print('用户名或者密码不对')

mean = {
    '1': func
}
while True:
    cmd = input('>>')
    if cmd == '0':
        break
    elif cmd in mean:
        mean[cmd]()
    else:
        print("ERROR")