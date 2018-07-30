# id|name|price
# id|name|password|cart|buyed|state|bank
import time
from ATM.core import operating_log
from ATM.core import shopping_operating as O
from ATM.core import shopping_commodity_operating as OC
from ATM.core import pay_interface as Pay
log = operating_log.logger('../log/shopping.log')
log.send(None)
user_state = {}
def login_interface():
    while True:
        username = input('账号:')
        password = input('密码:')
        if username == 'quit':
            break
        customer_info = login(username, password, user_state)
        if customer_info:
            return customer_info
            log.send('%s 登录成功' % username)
            break
        else:
            if username in user_state:
                user_state[username] += 1
            else:
                user_state[username] = 0
            log.send('%s 登录失败' % username)
    return {}
def decorator(func):
    def function(info_dic = {}):
        if len(info_dic) == 0:
            print('当前未登陆，请登陆！')
        else:
            return func(info_dic)
    return function

def decorator1(func):
    def function(_id, info_dic = {}):
        if len(info_dic) == 0:
            print('当前未登陆，请登陆！')
        else:
            return func(_id, info_dic)
    return function
@decorator1
def add_cart(_id, info_dic):#加入购物车
    info_dic['cart'] += '%s,' % _id
    log.send('%s 商品 %s 加入购物车' % (info_dic['name'], _id))
    O.update(info_dic)

@decorator1
def delete_cart(_id, info_dic):#从购物车删除商品
    falg = False
    list = info_dic['cart'].split(',')
    for i in range(len(list)):
        if list[i] == _id:
            list.pop(i)
            falg = True
            break
    if falg:
        info_dic['cart'] = ','.join(list)
        log.send('%s 商品 %s 删除' % (info_dic['name'], _id))
        O.update(info_dic)
    return falg

def pay(amount = 0.0, info_dic = {}):#支付
    #id|name|password|cart|buyed|state|bank
    if info_dic['bank'] == '\n' or info_dic['bank'] == None:
        info_list = Pay.login_bank()
        if info_list:
            info_dic['bank'] = info_list[1] + '\n'
            O.update(info_dic)
    else:
        info_list = [info_dic['id'], info_dic['name'], info_dic['password'], info_dic['cart'], info_dic['buyed'],
                     info_dic['state'], info_dic['bank']]
        if Pay.pay(amount, info_list):
            info_dic['buyed'] += info_dic['cart']
            info_dic['cart'] = ''
            log.send('%s 支付 %s 清空购物车' % (info_dic['name'], str(amount)))
            O.update(info_dic)

def show(commodity_dic = OC.search()):#显示商品列表
    # commodity_list = OC.search()
    for commodity in commodity_dic.values():
        print('%s %s %s' % (commodity['id'], commodity['name'], commodity['price'].strip('\n')))

@decorator
def show_buyed(info_dic = {}):#显示已购买商品列表
    id_list = info_dic['buyed'].split(',')
    info_list = OC.search_buyed(id_list)
    for i in info_list:
        print(f'{i["id"]} {i["name"]} {i["price"]}\n')

def cart_commodity_dic(info_dic):#显示购物车商品列表
    commodity_dic = OC.search()#所有商品列表
    cart_show_dic = {}#购物车里的商品列表
    cart = info_dic['cart']
    cart_list = cart.split(',')#购物车商品id列表
    num = 1
    for i in cart_list:
        if len(i) == 0:
            break
        cart_show_dic[num] = commodity_dic[i]
        num += 1
    return cart_show_dic

@decorator
def cart(info_dic):
    while True:
        cart_show_dic = cart_commodity_dic(info_dic)
        show(cart_show_dic)
        print(
    '''
    0.付款
    1.删除
    ''')
        cmd = input('>>')
        if cmd == '0':
            if len(cart_show_dic) == 0:
                print('请先购买商品！')
                continue
            amount = 0.0
            for value in cart_show_dic.values():
                amount += float(value['price'])
            pay(amount, info_dic)
            # info_dic = O.search(info_dic['name'])
        elif cmd == '1':
            _id = input('选择商品:')
            if not delete_cart(_id, info_dic):
                print('购物车里没有这个商品.')
        elif cmd == 'quit':
            break
        else:
            print('命令错误！')

def register():
    username = input('用户名：')
    password = input('密码：')
    password1 = input('重复密码:')
    if O.search(username)[0]['name'] == username:
        print('用户名已存在！')
        return 0
    if password != password1:
        print('两次密码不一样！')
        return 0
    _id = len(O.search()) + 1
    info = {'id': str(_id), 'name': username, 'password': password, 'cart': '', 'buyed': '', 'state': '', 'bank': ''}
    O.save(info)
    log.send('%s 注册成功' % username)
    print('注册成功')
    return 1

def login(username, password, user_state = {}):#登录
    '''
    登录成功返回用户信息 字典形式
    登录失败返回None
    :param username:
    :param password:
    :param user_state: 字典类型参数，登录密码错误的用户名和对应的次数
    :return:
    '''
    login_info = O.search(username)
    if len(login_info) > 1:
        print('账户不存在!')
        return None
    else:
        now_date = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        if password == login_info[0]['password']:
            if now_date > login_info[0]['state']:
                return login_info[0]
            else:
                print('此账户已经被锁定，今日不能再登录！')
                return None
        else:
            if user_state.get(username) and user_state.get(username) >= 1:
                login_info[0]['state'] = now_date
                O.update(login_info[0])
                log.send('%s 被锁定' % username)
            print('密码错误！')
            return None
