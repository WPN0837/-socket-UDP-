import datetime
info = {'seven': '123', 'alex': '123'}
state = {}
name = ''
password = ''
falg = False
while True:
    name = input('登录名：')
    password = input('密码：')
    time = str(datetime.date.today())
    with open('a.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
        f.close()
    for line in lines:
        if line.find('%s,%s\n' % (name, time)) >= 0:
            print('禁止登录！')
            falg = True
            break
    if falg:
        break
        # info1 = f.read()
        # if info1.find(name + ',') >= 0:
        #     print('禁止登录！')
        #     break
    if name in info:
        if info[name] == password:
            print('登录成功！')
            break
        else:
            print('登录失败！')
            if name in state:
                state[name] += 1
                if state[name] >= 3:
                    with open('a.txt', 'a', encoding='utf-8') as f:
                        f.write('%s,%s\n' % (name, time))
                    break
            else:
                state[name] = 1
    else:
        print('登录失败！')
