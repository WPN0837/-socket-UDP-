'''
3.编写购物车程序，实现以下功能(55分)
a)	实现注册
i.	用户名不可重复
ii.	密码至少6位
b)	登陆
i.	密码错误三次锁定5秒
c)	购物
i.	序号或商品名称均可购物
d)	查看购物车
i.	结算
ii.	清空
e)	账户信息
i.	修改密码
ii.	注销账号
f)	账户充值

g)	操作记录 使用装饰器完成

		以上功能中购物 查看购物车 账户信息 需要登录后再可以使用
		操作记录不是给用户使用的,而是会自动记录操作信息,写入文件中
		例如:
			2018-08-03 13:30:30  执行了登录,用户名为:
			2018-08-03 13:30:30  执行了注册,用户名为:
			2018-08-03 13:30:30  修改了密码,用户名为:
			2018-08-03 13:30:30  查看了购物车,用户名为:

'''
'''
用户信息存储格式
name|password|cart|money|lock


商品信息存储格式
id|name|price

'''
import time
session = []
userstate = {}
commodity_list = [
    {'id': '1', 'name': '电脑', 'price': 10000},
    {'id': '2', 'name': '手机', 'price': 5000},
    {'id': '3', 'name': '耳机', 'price': 200}
]
def logger1(func):
    def oper(*args, **kwargs):
        res = func(*args, **kwargs)
        if res:
            with open('operatinglog', 'a', encoding='utf-8') as log:
                log.write('%s %s 执行了 %s 操作\n' % (str(time.strftime('%Y-%m-%d %X', time.localtime(time.time()))),\
                                              res[0], res[1]))
        return res
    return oper
# def logger(filename = 'operatinglog'):
#     cmd = ''
#     while True:
#         datetime = time.strftime('%Y-%m-%d %X', time.localtime(time.time()))  # 格式化输出时间
#         if cmd != '':
#             with open(filename, 'a', encoding='utf-8')as f:
#                 f.write(str(datetime) + ' %s\n' % cmd)
#         cmd = yield#send 函数传入的参数
# log = logger()
# log.send(None)
def state(func):
    '''
    验证登录状态装饰器
    :return:
    '''
    def issession(*args, **kwargs):
        if session:
            res = func(*args, **kwargs)
            return res
        else:
            print('当前未登录，请登录')
            login()
    return issession
def find_info_by_name(name):
    '''
    根据用户名查找用户信息
    :param name:
    :return:
    '''
    with open('customer_info', 'r', encoding='utf-8') as info:
        lines = info.readlines()
    for line in lines:
        if name == line.strip('\n').split('|')[0]:
            return line.strip('\n').split('|')
    return None
def save(list):
    '''
    保存用户信息
    :param list:
    :return:
    '''
    with open('customer_info', 'a', encoding='utf-8') as info:
        info.write('|'.join(list) + '\n')
def update(list):
    '''
    更新用户信息
    :param list:
    :return:
    '''
    with open('customer_info', 'r', encoding='utf-8') as info:
        lines = info.readlines()
    for i in range(len(lines)):
        if lines[i].strip('\n').split('|')[0] == list[0]:
            lines[i] = '|'.join(list) + '\n'
            break
    with open('customer_info', 'w', encoding='utf-8') as info:
        info.writelines(lines)
def find_cart_list():
    '''
    查找用户购物车商品信息
    :return:
    '''
    cart_list = []
    if session[2]:
        cart = session[2].strip(',').split(',')
        for i in cart:
            for j in commodity_list:
                if j['id'] == i:
                    cart_list.append(j)
                    break
    return cart_list
@logger1
def resiger():
    '''
    注册
    用户名不可重复
    密码至少6位
    :return:
    '''
    print('用户注册(quit退出)')
    while True:
        name = input('用户名:')
        if name == 'quit':
            return False
        password = input('密码:')
        if password == 'quit':
            return False
        password1 = input('重复密码:')
        if password1 == 'quit':
            return False
        if find_info_by_name(name):
            print('该用户名已存在')
        elif len(password) < 6:
            print('密码至少6位')
        elif password != password1:
            print('两次密码不一样')
        else:
            save([name, password, '', '0.0', ''])
            # log.send('%s 执行了注册操作' % name)
            print('注册成功')
            return name, '注册'
@logger1
def login():
    '''
    登陆
    密码错误三次锁定5秒
    :return:
    '''
    global session
    print('登录(quit退出')
    while True:
        name = input('用户名:')
        if name == 'quit':
            break
        password = input('密码:')
        if password == 'quit':
            break
        user_info_list = find_info_by_name(name)
        if user_info_list:
            if password == user_info_list[1]:
                if not user_info_list[4] or time.time() - float(user_info_list[4]) > 5:
                    print('登录成功')
                    session = user_info_list
                    # log.send('%s 执行了登录操作' % session[0])
                    return session[0], '登录'
                else:
                    print('账户被锁定')
            else:
                print('密码不正确')
                if name not in userstate:
                    userstate[name] = 0
                else:
                    userstate[name] += 1
                if userstate[name] >= 2:
                    user_info_list[4] = str(time.time())
                    update(user_info_list)
                    print('账户被锁定，5秒后再登录')
        else:
            print('用户名不存在')
@state
@logger1
def add_to_cart():
    '''
    添加到购物车
    :return:
    '''
    for i in commodity_list:
        print(i['id'], i['name'], i['price'])
    name_or_id = input('选择商品：')
    if name_or_id == 'quit':
        return
    for i in commodity_list:
        if name_or_id == i['id'] or name_or_id == i['name']:
            session[2] += i['id'] + ','
            update(session)
            print('%s 添加到购物车成功' % i['name'])
            return session[0], '购买'
    else:
        print('%s  商品不存在' % name_or_id)
@state
@logger1
def cart():
    '''
    查看购物车
    结算
    清空
    :return:
    '''
    # log.send('%s 执行了查看购物车操作' % session[0])
    cart_list = find_cart_list()
    if cart_list:
        for i in cart_list:
            print(i['id'], i['name'], i['price'])
    else:
        print('购物车是空的，去购物吧')
    while True:
        print(
'''
0.结算
1.清空
2.退出
'''
        )
        cmd = input('>>')
        if cmd == '0':
            payment()
        elif cmd == '1':
            clear_cart()
        elif cmd == '2':
            break
        else:
            print('输入错误')
    return session[0], '查看购物车'
@logger1
def payment():
    '''
    结算
    :return:
    '''
    cart_list = find_cart_list()
    num = 0
    if not cart_list:
        print('购物车是空的，去购物吧')
        return
    for i in cart_list:
        num += float(i['price'])
    balance = float(session[3])
    if balance > num:
        balance -= num
        session[3] = str(balance)
        session[2] = ''
        update(session)
        print('支付成功')
        # log.send('%s 执行了结算操作' % session[0])
        return session[0], '充值'
    else:
        print('余额不足，请充值')
@logger1
def clear_cart():
    '''
    清空购物车
    :return:
    '''
    session[2] = ''
    update(session)
    return session[0], '清空购物车'
    # log.send('%s 执行了清空购物车操作' % session[0])
@state
@logger1
def show_info():
    '''
    显示账户信息
    修改密码
    :return:
    '''
    # name|password|cart|money|lock
    # log.send('%s 执行了查看账户信息操作' % session[0])
    cart_list = find_cart_list()
    print('用户名:' + session[0] +'\n购物车:')
    for i in cart_list:
        print(i['id'], i['name'], i['price'])
    print('余额:' + session[3])
    return session[0], '查看账户信息'
@state
@logger1
def change_password():
    '''
    修改密码
    :return:
    '''
    print('修改密码(quit退出)')
    while True:
        old_password = input('旧密码:')
        if old_password == 'quit':
            break
        new_password = input('新密码:')
        if new_password == 'quit':
            break
        new_password1 = input('新密码:')
        if new_password1 == 'quit':
            break
        if old_password != session[1]:
            print('旧密码错误')
        elif len(new_password) < 6:
            print('新密码长度不能小于6位')
        elif new_password != new_password1:
            print('两次新密码不一样')
        elif new_password == old_password:
            print('新密码与旧密码重复')
        else:
            session[1] = new_password
            update(session)
            print('密码修改成功')
            # log.send('%s 执行了修改密码操作' % session[0])
            return session[0], '修改密码'
@state
@logger1
def logout():
    '''
    注销账户
    :return:
    '''
    # log.send('%s 执行了注销操作' % session[0])
    name = session[0]
    session.clear()
    return name, '注销'
@state
@logger1
def recharge():
    '''
    账户充值
    :return:
    '''
    balance = float(session[3])
    amount = input('输入金额:')
    if amount.isdigit():
        balance += float(amount)
        session[3] = str(balance)
        update(session)
        print('充值成功')
        return session[0], '充值'
        # log.send('%s 执行了充值操作，金额：%s' % (session[0], str(amount)))
    else:
        print('请输入正确金额')

if __name__ == '__main__':
    cmd_dic = {
        '0': add_to_cart,
        '1': cart,
        '2': recharge,
        '3': show_info,
        '4': change_password,
        '5': logout,
        '6': resiger,
        '7': login
    }
    while True:
        if session:
            print(
'''
0.购物
1.查看购物车
2.充值
3.账户信息
4.修改密码
5.注销
'''
            )
        else:
            print(
'''
0.购物
1.查看购物车
2.充值
3.账户信息
4.修改密码
5.注销
6.注册
7.登录
'''
            )
        cmd = input('>>(quit退出)')
        if cmd == 'quit':
            break
        if cmd in cmd_dic:
            if session:
                if cmd < '6':
                    cmd_dic[cmd]()
                else:
                    print('输入错误')
            else:
                cmd_dic[cmd]()
        else:
            print('输入错误')