'''
编写装饰器，为多个函数加上认证的功能（用户的账号密码来源于文件），要求登录成功一次，后续的函数都无需再输入用户名和密码
注意：从文件中读出字符串形式的字典，可以用eval('{"name":"egon","password":"123"}')转成字典格式
'''
session = {}
def zhuangshiqi(func):
    def wrapper(*args, **kwargs):
        res = ''
        if session:
            res = func(*args, **kwargs)
        else:
            print('未登录！')
            username = input("username:")
            password = input('password:')
            login(username, password)
        return res
    return wrapper
def login(username, password):
    global session
    user_info_dic = {}
    with open('login.db', 'r', encoding='utf-8') as login_db:
        for line in login_db.readlines():
            if username in line:
                user_info_dic = eval(line.strip('\n'))
                break
    if user_info_dic:
        if password == user_info_dic['password']:
            session = user_info_dic
            return True
        else:
            return False
    return False
@zhuangshiqi
def func1():
    print('func1')
@zhuangshiqi
def func2():
    print('func2')
@zhuangshiqi
def func3():
    print('func3')
@zhuangshiqi
def func4():
    print('func4')
mean = {
    '1': func1,
    '2': func2,
    '3': func3,
    '4': func4
}
def resiger():
    username = input("username:")
    password = input('password:')
    dic = {'username': username, 'password': password}
    with open('login.db', 'a', encoding='utf-8') as login_db:
        login_db.write(str(dic)+'\n')
# resiger()
while True:
    cmd = input('>>')
    if cmd == '0':
        break
    elif cmd in mean:
        mean[cmd]()
    else:
        print("ERROR")