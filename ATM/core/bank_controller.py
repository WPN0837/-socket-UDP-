from ATM.core import operating_log
from ATM.core import bank_operating as O
log = operating_log.logger()
log.send(None)
list = []

def view_account_info(list = []):
    '''
    查看账户信息
    :param list: 账户信息List
    :return:
    '''
    # 1|6216610800000000001|123456|0.0|1000.0|2018-07-24
    print(
    '''
    账号:%s
    余额:%s
    总透支额度:%s
    ''' % (list[1], list[3], list[4]))

def with_draw(consume = 0.0, list= []):
    '''
    取现/消费
    :param consume: 消费金额
    :param list: 账户信息List
    :return: True 取现或消费成功
    '''
    balance = float(list[3])
    overdraft = float(list[4])
    if balance + overdraft >= consume:
        balance -= consume
        list[3] = str(balance)
        O.update(list)
        log.send('%s 消费 %.2f元' % (list[1], consume))
        return True
    else:
        print('余额不足！')
        return False

def pay_back(return_money = 0.0, list = []):
    '''
    存款/还款
    :param return_money:存款/还款 金额
    :param list:账户信息
    :return:
    '''
    balance = float(list[3])
    balance += return_money
    list[3] = str(balance)
    O.update(list)
    log.send('%s 还款%.2f元' % (list[1], return_money))

def transfer(list = []):
    '''
    转账
    :param list: 账户信息
    :return:True 转账成功
    '''
    balance = float(list[3])
    if balance <= 0:
        print('余额不足！余额:%s' % list[3])
        return False
    account = input('账号:')
    info = O.search(account)
    if account in info:
        amount = float(input('金额:'))
        if amount > balance:
            print('余额不足！余额:%s' % list[3])
            return False
        else:
            balance -= amount
            balance_ = float(info[account][3])
            balance_ += amount
            list[3] = str(balance)
            info[account][3] = str(balance_)
            O.update(list)
            O.update(info[account])
            print('转账成功！%s已经收到转账' % account)
            log.send('%s 转账 %s 金额 %.2f元' % (list[1], info[account][1], amount))
            return True
    else:
        print('账号%s不存在！' % account)
        return False

def mobile_pay(amount = 0.0, buy = [], sell = []):
    '''
    移动支付
    :param Amount:
    :param buy:
    :param sell:
    :return:
    '''
    balance_buy = float(buy[3]) + float(buy[4])
    balance_sell = float(sell[3])
    if balance_buy <= 0.0 or amount > balance_buy:
        return False
    balance_buy -= amount
    balance_sell += amount
    buy[3] = str(balance_buy)
    sell[3] = str(balance_sell)
    O.update(buy)
    O.update(sell)
    log.send('%s 消费 金额 %.2f元' % (buy[1], amount))
    return True

def change_password(list = []):
    old_password = input('旧密码：')
    new_password = input('新密码：')
    new_password1 = input('重复新密码：')
    if old_password != list[2]:
        print('旧密码错误！')
        return False
    if new_password != new_password1:
        print('两次新密码不一样！')
        return False
    if old_password == new_password:
        print('新密码不能和旧密码相同')
        return False
    list[2] = new_password
    O.update(list)
    log.send('%s 修改密码' % list[1])
    return True
def controller(list1 = []):
    global list
    list = list1
    while True:
        print(
        '''
        0.查看账户信息
        1.取现
        2.还款
        3.转账
        4.修改密码
        5.
        6.
        '''
        )
        cmd = input('>>')
        if cmd == 'quit':
            break
        elif cmd == '0':
            view_account_info(list)
        elif cmd == '1':
            consume = float(input('输入取现金额：'))
            if with_draw(consume, list):
                list = O.search(list[1])[list[1]]
        elif cmd == '2':
            return_money = float(input('输入还款金额:'))
            pay_back(return_money, list)
            list = O.search(list[1])[list[1]]
            print('还款成功！')
        elif cmd == '3':
            if transfer(list):
                list = O.search(list[1])[list[1]]
        elif cmd == '4':
            change_password(list)
            list = O.search(list[1])[list[1]]
        else:
            print('命令错误！')