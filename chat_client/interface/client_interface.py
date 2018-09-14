import time
import json
from socket import *
from threading import Event
from conf import settings
from bin import client
from modles.user import user
from db import db_handle
from lib import common

sock = socket(AF_INET, SOCK_DGRAM)
sock_chat = socket(AF_INET, SOCK_DGRAM)
sock_chat.bind((common.get_host_ip(), 9998))
service_addr = (settings.SERVICE_IP, 8888)
e = Event()


def register(account, password):
    data_dic = {'o': '1', 'd': {'a': account, 'p': password}}
    sock.sendto(message_encryption(data_dic), service_addr)
    data_dic = message_parsing(sock.recvfrom(1024)[0])
    return data_dic['f'], data_dic['m']


def login(account, password):
    data_dic = {'o': '2', 'd': {'a': account, 'p': password}}
    sock.sendto(message_encryption(data_dic), service_addr)
    data_dic = message_parsing(sock.recvfrom(1024)[0])
    if data_dic['f']:
        client.user_info = new_user(data_dic['u'])
        e.set()
    return data_dic['f'], data_dic['m']


def logout():
    data_dic = {'o': '4', 'd': {'a': client.user_info.account}}
    sock.sendto(message_encryption(data_dic), service_addr)
    e.clear()
    client.user_info = None
    return True, '注销成功'


def add_friend(account):
    data_dic = {'o': '5', 'd': {'a': client.user_info.account, 't': account}}
    sock.sendto(message_encryption(data_dic), service_addr)
    data_dic = message_parsing(sock.recvfrom(1024)[0])
    if data_dic['f']:
        client.user_info.friends.append(account)
    return data_dic['f'], data_dic['m']


def chat(account):
    print('开始聊天啦')
    while True:
        msg = input('>>').strip()
        if msg == 'q':
            return True, '结束聊天'
        if msg == '':
            continue
        data_dic = {'o': '3', 'd': {'a': client.user_info.account, 'm': msg, 't': account}}
        sock.sendto(message_encryption(data_dic), service_addr)
        data_dic = message_parsing(sock.recvfrom(1024)[0])
        db_handle.save(client.user_info.account, msg)
        if not data_dic['f']:
            print(data_dic['m'])


def conn_session():
    while True:
        time.sleep(300)
        e.wait()
        if client.user_info:
            sock.sendto(client.user_info.account.encode('utf-8'), (settings.SERVICE_IP, 9997))


def recv_chat():
    while True:
        e.wait()
        data = sock_chat.recvfrom(1024)[0]
        data_dic = message_parsing(data)
        print('\r%s: %s' % (data_dic['a'], data_dic['m']))
        db_handle.save(data_dic['a'], data_dic['m'])


def message_parsing(data_bytes):
    data = data_bytes.decode('utf-8')
    data_dic = json.loads(data)
    return data_dic


def message_encryption(data_dic):
    data = json.dumps(data_dic)
    return data.encode('utf-8')


def new_user(u_dict):
    account = u_dict['account']
    password = u_dict['password']
    friends = u_dict['friends']
    return user(account, password, friends)
