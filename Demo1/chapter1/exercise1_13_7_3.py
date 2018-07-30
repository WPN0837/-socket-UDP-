'''
name={'seven': '123', 'alex': '123'}
for i in range(0, 3):
    n = input('用户名：')
    p = input('密码：')
    if(n in name and p==name[n]):
        print('登陆成功')
        break
    else:
        print('登陆失败')
'''

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