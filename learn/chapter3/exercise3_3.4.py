'''

文件格式
|u:alex|p:abc123|a:24|po:Enginner|d:IT|

'''

state = {}
info = {}
#验证用户名、密码
def v(username = '', password = '', info = {}):
    '''

    :param username:
    :param password:
    :param info:
    :return:
    -1 密码错误
    0 用户名不存在
    1 登录成功
    2 用户被锁定
    '''
    if username in info.keys():
        if password == info[username][2]:
            if username in state and state[username] >= 3:
                print('用户被锁定!')
                return 2#用户锁定
            else:
                return 1#登陆成功
        else:
            if username in state:
                state[username] += 1
            else :
                state[username] = 0
            print('密码错误！')
            return -1#密码错误
    else:
        print('用户名不存在！')
        return 0#用户名不存在

#修改个人信息
def modify(list):
    print('Tips:不输入则不修改此项内容！')
    age = input('age:')
    if age != '':
        list[3] = age
    posistion = input('posistion:')
    if posistion != '':
        list[4] = posistion
    department = input('department:')
    if department != '':
        list[5] = department
    return list

#打印个人信息
def show(list):
    print(
    '''
    =======================
    username:%s
    age:%s
    posistion:%s
    department:%s
    =======================
    ''' % (list[1], list[3], list[4], list[5]))

#修改密码
def modify_pwd(list):
    old = input('旧密码：')
    new = input('新密码：')
    new1 = input('重复新密码：')
    if old != list[2]:
        print('密码错误！')
    elif old == new:
        print('新密码不能与旧密码相同！')
    elif new != new1:
        print('两次密码不一样！')
    else:
        list[2] = new
        print('修改成功！')
    return list

#保存信息
def save(info = {}):
    with open('info1', 'w', encoding='utf-8') as info1:
        for line in info.values():
            info1.write('|'.join(line))

#注册
def register(info = {}):
    username = input('用户名：')
    password = input('密码：')
    password1 = input('重复密码：')
    age = input('年龄：')
    posistion = input('职位：')
    department = input('部门：')
    if username == '':
        print('用户名不能为空！')
    elif username in info.keys():
        print('用户名已存在！')
    elif password == '':
        print('密码不能为空！')
    elif password1 == '':
        print('重复密码不能为空！')
    elif password != password1:
        print('两次密码不一样！')
    elif age == '':
        print('年龄不能为空！')
    elif posistion == '':
        print('职位不能为空！')
    elif department == '':
        print('部门不能为空！')
    else:
        register_info = '|%s|%s|%s|%s|%s|\n' % (username, password, age, posistion, department)
        with open('info1', 'a', encoding='utf-8') as info1:
            info1.write(register_info)


if __name__ == '__main__':
    with open('info1', 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            line_list = line.split('|')
            info[line_list[1]] = line_list
    # register(info)
    while True:
        username = input('用户名：')
        password = input('密码：')
        v_state = v(username, password, info)
        if v_state == 1:
            break

    while True:
        print(
    '''
    =======================
    1.修改个人信息
    2.打印个人信息
    3.修改密码
    =======================
    '''
        )
        c = input('选择：')
        if c == '1':
            info[username] = modify(info[username])
            save(info)
        elif c == '2':
            show(info[username])
        elif c == '3':
            info[username] = modify_pwd(info[username])
            save(info)
        elif c == '0':
            break
        else:
            print('输入错误！')