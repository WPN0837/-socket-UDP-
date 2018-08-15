import time
from bin import main
from lib import decorator, tool, dao
@decorator.log_decorator('ATM操作')
def login():#登录
    print("登录('quit'退出)")
    while True:
        account = input('账号:')
        if account == 'quit':
            break
        password = input('密码:')
        password = tool.md5(password)
        user_dic = dao.find_info_by_account(account)
        if user_dic:
            if password == user_dic['password']:
                if user_dic['freeze']:
                    print('账户被冻结')
                elif user_dic['date'] and time.time() - float(user_dic['date']) < 300:
                    print('账户被锁定，请 %s 后登录' % (time.strftime('%M:%S',\
                                                    time.localtime(300.0 - time.time() + float(user_dic['date'])))))
                else:
                    main.user_info = user_dic
                    return account, '登录'
            else:
                if account in main.user_state:
                    main.user_state[account] += 1
                else:
                    main.user_state[account] = 0
                if main.user_state[account] >= 2:
                    user_dic['date'] = str(time.time())
                    dao.update(user_dic)
                print('密码错误')
        else:
            print('账户不存在')
    return None

@decorator.user_state_decorator
@decorator.log_decorator('ATM操作')
def transfer():#转账
    print("转账('quit'退出)")
    while True:
        account = input('账户：')
        if account == 'quit':
            break
        if account == main.user_info['account']:
            print('不能转到自己的账户')
            continue
        amount = input('金额：')
        if amount.isdigit():
            if float(main.user_info['balance']) < float(amount):
                print('余额不足')
        else:
            print('输入整数')
            continue
        info_dic = dao.find_info_by_account(account)
        if info_dic:
            main.user_info['balance'] = str(float(main.user_info['balance']) - float(amount))
            info_dic['balance'] = str(float(info_dic['balance']) + float(amount))
            dao.update(main.user_info)
            dao.update(info_dic)
            return main.user_info['account'], '转账', info_dic['account'], amount
        else:
            print('账户不存在')
    return None

@decorator.user_state_decorator
@decorator.log_decorator('ATM操作')
def repayment():#还款
    print("还款('quit'退出)")
    while True:
        amount = input('金额：')
        if amount == 'quit':
            break
        if amount.isdigit():
            main.user_info['balance'] = str(float(main.user_info['balance']) + float(amount))
            dao.update(main.user_info)
            return main.user_info['account'], '还款', amount
        else:
            print('请输入整数')
    return None

@decorator.user_state_decorator
@decorator.log_decorator('ATM操作')
def withdraw(): #提现
    print("提现[%5的手续费]('quit'退出)")
    while True:
        amount = input('金额：')
        if amount == 'quit':
            break
        if amount.isdigit():
            if float(amount) * 1.05 <= float(main.user_info['balance']):
                main.user_info['balance'] = str(float(main.user_info['balance']) - float(amount) * 1.05)
                return main.user_info['account'], '取现', amount
            else:
                print('余额不足')
        else:
            print('输入整数')
    return None