from interface import client_interface
from lib import common

user_info = None


def register():
    if user_info:
        print('已登录，不能注册')
        return
    while True:
        account = input('账号：')
        if account == 'q':
            return
        password = input('密码：')
        password1 = input('重复密码:')
        if password == password1:
            falg, msg = client_interface.register(account, password)
            print(msg)
            if falg:
                return
        else:
            print('两次密码不一样')


def login():
    if user_info:
        print('已登录，不能登录')
        return
    while True:
        account = input('账号：')
        if account == 'q':
            return
        password = input('密码：')
        falg, msg = client_interface.login(account, password)
        print(msg)
        if falg:
            return


def show_friends():
    if user_info.friends:
        for i in range(len(user_info.friends)):
            print(i + 1, user_info.friends[i])
        return True
    else:
        print('空')


@common.auth
def chat():
    if not show_friends():
        return
    while True:
        choice = input('选择好友(编号)：')
        if choice == 'q':
            return
        if choice.isdigit():
            choice = int(choice)
            if choice <= len(user_info.friends):
                falg, msg = client_interface.chat(user_info.friends[choice - 1])
                print(msg)
                if falg:
                    return
            else:
                print('编号错误，重新输入')
        else:
            print('请输入数字')


def recv_chat():
    client_interface.recv_chat()


@common.auth
def add_friend():
    while True:
        account = input('输入好友账号：')
        if account == 'q':
            return
        falg, msg = client_interface.add_friend(account)
        print(msg)
        if falg:
            return


@common.auth
def logout():
    falg, msg = client_interface.logout()
    print(msg)


def conn_session():
    client_interface.conn_session()


def run():
    mean_dic = {
        '1': register,
        '2': login,
        '3': chat,
        '4': logout,
        '5': add_friend,
    }
    while True:
        print(
            '''
            1: 注册
            2: 登录
            3: 聊天
            4: 注销
            5：加好友
            '''
        )
        cmd = input('>>')
        if cmd == 'q':
            return
        elif cmd in mean_dic:
            mean_dic[cmd]()
        else:
            print('命令错误')
