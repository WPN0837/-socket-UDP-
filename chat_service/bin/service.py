from socket import *
from lib import common
from interface import service_interface

self_ip = common.get_host_ip()
print(self_ip)
user_info = {}


# 生存时钟


def run():
    mean_dic = {
        '1': service_interface.register,  # 注册
        '2': service_interface.login,  # 登录
        '3': service_interface.transmit,  # 转发
        '4': service_interface.logout,  # 注销
        '5': service_interface.add_friend, # 添加好友
        '0': service_interface.error  # 错误请求
    }
    sock_udp = socket(AF_INET, SOCK_DGRAM)
    sock_udp.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    sock_udp.bind((self_ip, 8888))
    while True:
        data_recv = sock_udp.recvfrom(1024)
        data_dic = service_interface.message_parsing(data_recv[0])
        if data_dic['o'] in mean_dic:
            falg, msg = mean_dic[data_dic['o']](data_dic['d'], data_recv[1], sock_udp)
        else:
            mean_dic['0'](data_dic['d'], data_recv[1], sock_udp)
