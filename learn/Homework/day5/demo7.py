goods = [
    {'name': '电脑', 'price': 1999},
    {'name': '鼠标', 'price': 10},
    {'name': '游艇', 'price': 20},
    {'name': '美女', 'price': 998}
]
#\ 033 [显示方式;字体色;背景色m ...... [\ 033 [0m]
session = {}#session
buyed = []#已购买商品
cart = []#购物车
money = -1#余额
info = {}
def verification(name, password):
    '''
    验证用户名、密码
    :param name:
    :param password:
    :return:
    '''
    global buyed, cart, money
    with open('a.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
        f.close()
    for line in lines:
        if line.find('|n:'+name+'|') >= 0 and line.find('|p:'+password+"|") >= 0:
            session['name'] = name
            session['password'] = password
            if line.split('|')[4] != '':
                buyed = line.split('|')[4].split(',')
            if line.split('|')[5] != '':
                cart = line.split('|')[5].split(',')
            if line.split('|')[3] != '':
                money = int(line.split('|')[3])
            return True
    return False

def show_goods():
    '''
    显示商品
    :return:
    '''
    for i, value in enumerate(goods):
        print('%d %s %d' % (i+1, value['name'], value['price']))

def add_cart(i):
    '''
    添加商品到购物车
    :param i:
    :return:
    '''
    cart.append(i)

def buy_goods():
    '''
    付款
    :param i:
    :return:
    '''
    global money
    num = 0
    for i in cart:
        num += goods[int(i)-1]['price']
    if num > money:
        #'\033[1;31;40m 余额不足！ \033[0m!'
        print('余额不足！')
    else:
        money -= num
        buyed.extend(cart)
        cart.clear()

def show_buyed():
    '''
    显示已购买商品
    :return:
    '''
    for i in buyed:
        print(goods[int(i)-1]['name'], goods[int(i)-1]['price'])

def show_cart():
    '''
    显示购物车内商品
    :return:
    '''
    for i in cart:
        print(goods[int(i)-1]['name'], goods[int(i)-1]['price'])

def register(info = {}):
    username = input('用户名：')
    password = input('密码：')
    password1 = input('重复密码：')
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
    else:
        '''|n:admin|p:123456|1000|1,1,3,2|1,1|'''
        register_info = '|n:%s|p:%s||||\n' % (username, password)
        with open('a.txt', 'a', encoding='utf-8') as info1:
            info1.write(register_info)

if __name__ == '__main__':
    with open('a.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            line_list = line.split('|')
            info[line_list[1]] = line_list
    falg = False
    while True:
        name = input('登录名：')
        password = input('密码：')
        if verification(name, password):
            falg = True
            print('登录成功！')
            if money == -1:
                money = int(input('输入工资：'))
            break
        else:
            print('登录失败！')
    while falg:
        print(
    '''
    0.退出
    1.显示商品
    2.购买商品
    3.我的购物车
    4.已购买商品
    ''')
        c = input('选择:')
        if c == '0':
            lines=[]
            with open('a.txt', 'r+', encoding='utf-8') as f:
                lines = f.readlines()
                f.close()
            for i, line in enumerate(lines):
                if line.find('|n:' + session['name'] + '|') >= 0:
                    str_cart = ','.join(cart)#保存购物车信息
                    str_buyed = ','.join(buyed)#保存已购买商品信息
                    str_line = '|n:%s|p:%s|%d|%s|%s|\n' % (session['name'], session['password'], money, str_buyed, str_cart)
                    #|name|password|money|buyed|cart|
                    lines[i] = str_line
                    break
            with open('a.txt', 'w', encoding='utf-8') as f:
                f.writelines(lines)
                f.close()
            print('信息保存成功！拜拜~~')
            break
        elif c == '1':
            show_goods()
        elif c == '2':
            show_goods()
            g = input('选择商品序号:')
            #应当加一个输入验证
            add_cart(g)
        elif c == '3':
            while True:
                show_cart()
                print(
    '''
    0.返回
    1.付款
    2.删除
    ''')
                c1 = input('选择:')
                if c1 == '0':
                    break
                elif c1 == '1':
                    buy_goods()
                    lines = []
                    with open('a.txt', 'r+', encoding='utf-8') as f:
                        lines = f.readlines()
                        f.close()
                    for i, line in enumerate(lines):
                        if line.find('|n:' + session['name'] + '|') >= 0:
                            str_cart = ','.join(cart)  # 保存购物车信息
                            str_buyed = ','.join(buyed)  # 保存已购买商品信息
                            str_line = '|n:%s|p:%s|%s|%s|%s|\n' % (
                            session['name'], session['password'], str(money), str_buyed, str_cart)
                            # |name|password|money|buyed|cart|
                            lines[i] = str_line
                            break
                    with open('a.txt', 'w', encoding='utf-8') as f:
                        f.writelines(lines)
                        f.close()
                elif c1 == '2':
                    g = input('选择商品序号:')
                    if g in cart:
                        cart.remove(g)
                    else:
                        print('输入错误！')
                else:
                    print('输入错误！')
        elif c == '4':
            show_buyed()
        else:
            print('输入错误！')