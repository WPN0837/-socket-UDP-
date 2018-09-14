import json
from threading import Lock
import time
from modles.user import user
from bin import service
from socket import *
from lib import common

session = {}
L = Lock()


def register(request, addr, sock):
    u = user.get_user_by_account(request['a'])
    if u:
        sock.sendto(message_encryption({'f': False, 'm': '用户已存在'}), addr)
        return False, '用户已存在'
    else:
        user.register(request['a'], request['p'])
        sock.sendto(message_encryption({'f': True, 'm': '注册成功'}), addr)
        return True, '注册成功'


def login(request, addr, sock):
    u = user.get_user_by_account(request['a'])
    if u:
        if request['p'] == u.password:
            service.user_info[request['a']] = (u, (addr[0], 9998))
            L.acquire()
            session[request['a']] = (addr[0], 9997, time.time())
            L.release()
            sock.sendto(message_encryption({'f': True, 'm': '登录成功', 'u': u.__dict__}), addr)
            return True, '登录成功'
        else:
            sock.sendto(message_encryption({'f': False, 'm': '密码错误'}), addr)
            return False, '密码错误'
    else:
        sock.sendto(message_encryption({'f': False, 'm': '用户不存在'}), addr)
        return False, '用户不存在'


def detect_session():
    sock = socket(AF_INET, SOCK_DGRAM)
    sock.bind((common.get_host_ip(), 9997))
    while True:
        account = sock.recvfrom(1024)[0].decode('utf-8')
        L.acquire()
        if account in session:
            session[account][2] = time.time()
        L.release()


def delete_session():
    while True:
        L.acquire()
        for s in session:
            if time.time() - session[s][2] >= 600:
                session.pop(s)
                service.user_info.pop(s)
        L.release()


def transmit(request, addr, sock):
    t = request['t']
    if t in service.user_info:
        sock.sendto(message_encryption(request), service.user_info[t][1])
        sock.sendto(message_encryption({'f': True, 'm': '转发成功'}), addr)
        return True, '转发成功'
    else:
        sock.sendto(message_encryption({'f': False, 'm': '对方不在线'}), addr)
        return False, '对方不在线'


def logout(request, addr, sock):
    service.user_info.pop(request['a'])
    return True, '注销成功'


def add_friend(request, addr, sock):
    u = user.get_user_by_account(request['t'])
    if u:
        self = user.get_user_by_account(request['a'])
        self.add_friend(request['t'])
        u.add_friend(request['a'])
        sock.sendto(message_encryption({'f': True, 'm': '添加成功'}), addr)
        return True, '添加成功'
    else:
        sock.sendto(message_encryption({'f': False, 'm': '账号不存在'}), addr)
        return False, '账号不存在'


def error(request, addr, sock):
    sock.sendto(message_encryption({'f': False, 'm': '服务器无法处理'}), addr)


def message_parsing(data_bytes):
    data = data_bytes.decode('utf-8')
    data_dic = json.loads(data)
    return data_dic


def message_encryption(data_dic):
    data = json.dumps(data_dic)
    return data.encode('utf-8')
