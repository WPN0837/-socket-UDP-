from ATM.core import bank_controller as C
from ATM.core import bank_operating as O
from ATM.core import operating_log
seller_info = ['1', '6216610800000000001', '123456', '150.0', '1000.0', '2018-07-21\n']#收款账户信息
customer_state = {}
log = operating_log.logger()
log.send(None)
def login_bank():
    while True:
        number = input('账号:')
        password = input('密码:')
        if number == 'quit' or password == 'quit':
            return None
        customer_list = O.login(number, password, customer_state)
        if customer_list:
            log.send('%s 登录成功 支付接口' % number)
            return customer_list
        else:
            if number in customer_state:
                customer_state[number] += 1
            else:
                customer_state[number] = 0
            log.send('%s 登录失败 支付接口'%number)
            return None
def get_info(number):
    info_dic = O.search(number)
    if len(info_dic) == 0:
        return None
    else:
        return info_dic[number]
def pay(amount = 0.0, info_list = []):
    buy_info = get_info(info_list[6].strip('\n'))
    if C.mobile_pay(amount, buy_info, seller_info):
        print('支付成功！金额：%.2f' % amount)
        return True
    else:
        print('余额不足！')
        return False