'''
编写用户登录装饰器，在登录成功后无需重新登录，同一账号重复输错三次密码则锁定5分钟
'''
import time
session = {}
userstate = {}
def A(func):
    def wrapper(*args, **kwargs):
        res = None
        if session:
            res = func(*args, **kwargs)
        else:
            print('当前未登录！')
            username = input('用户名：')
            password = input('密码：')
            if username == 'alex' and password == 'abc123':
                if username not in userstate or time.time() - userstate[username][1] > 300:
                    session[username] = time.time()
                    print('登陆成功')
                    res = func(*args, **kwargs)
            else:
                print('用户名或密码错误！')
                if username not in userstate:
                    userstate[username] = [0, 0]
                elif userstate[username][0] < 2:
                    userstate[username][0] += 1
                else:
                    userstate[username][1] = time.time()
        return res
    return wrapper
@A
def func():
    print('功能')
    input('>>')
func()
func()