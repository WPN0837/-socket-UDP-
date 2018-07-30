# 同一个用户名累计登录3次密码错误  程序停止

info = {'seven': '123', 'alex': '123'}
state = {}
name = ''
password = ''
while True:
    name = input('登录名：')
    password = input('密码：')
    if name in info:
        if info[name] == password:
            print('登录成功！')
            break
        else:
            print('登录失败！')
            if name in state:
                state[name] += 1
                if state[name] >= 3:
                    break
            else:
                state[name] = 1
    else:
        print('登录失败！')
