# {'id':id, 'account':account, 'password':password, 'name': name ,'date':date, 'balance': balance,
# 'overdraft': overdraft, 'freeze': freeze}
import re
import hashlib
from lib import tool, dao, decorator
t = re.compile('[0-9A-Za-z]{6,10}')

@decorator.log_decorator("ATM操作")
def register():#注册
    print("添加账户('quit'退出)")
    while True:
        name = input("用户名：")
        if name == 'quit':
            break
        password = input('密码：')
        password1 = input('重复密码：')
        res = t.findall(password)
        if not res or len(res[0]) != len(password):
            print('密码长度必须为6位以上10位以下的字母或数字')
        elif password != password1:
            print('两次密码不同')
        else:
            password = tool.md5(password)
            id, account = tool.get_id_and_account()
            user_dic = {'id': id, 'account': account, 'password': password, 'name': name, 'date': None, \
                             'balance': 0.0, 'overdraft': 0.0, 'freeze': False}
            dao.save(user_dic)
            return account, '注册'
    return None

def user_amount(id, amount = 0.0):#用户额度管理
    user_info = dao.find_info_by_id(id)
    if user_info and amount % 100.0 == 0:
        user_info['overdraft'] = amount
        return user_info['name'], '修改额度', str(amount)
    return None


def set_freeze(id ,freeze_state):
    user_info = dao.find_info_by_id(id)
    if user_info:
        user_info['freeze'] = freeze_state
        return user_info['name'], '冻结状态', str(freeze_state)
    return None