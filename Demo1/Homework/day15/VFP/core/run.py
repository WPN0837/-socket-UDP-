from core import dao_customer as dao
from lib import logger
session = {}
@logger.logger
def login():
    global session
    name = input('用户名:')
    password = input('密码:')
    dic = dao.search(name)
    if dic['password'] == password:
        session = dic
        return session['name'], '登录'
    else:
        print('账号或密码错误')
        return None

def run():
    while True:
        print(
'''
0.登录
'''
        )
        cmd = input('>>')
        if cmd == '0':
            login()
        else:
            break