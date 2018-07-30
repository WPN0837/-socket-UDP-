#银行用户个人信息文件 bank_customer_db
from ATM.core import bank_operating as O
from ATM.core import bank_controller as C
from ATM.core import operating_log
session = {}#存储当前登录用户信息
customer_state = {}
log = operating_log.logger()
log.send(None)
if __name__ == '__main__':#程序入口
    while True:
        number = input('账号:')
        password = input('密码:')
        customer_info = O.login(number, password, customer_state)
        if customer_info:
            session[number] = customer_info
            log.send('%s 登录成功' % number)
            break
        else:
            if number in customer_state:
                customer_state[number] += 1
            else:
                customer_state[number] = 0
            log.send('%s 登录失败'%number)
    C.controller(session[number])