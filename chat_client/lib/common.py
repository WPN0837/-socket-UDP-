from socket import *


def get_host_ip():
    try:
        s = socket(AF_INET, SOCK_DGRAM)
        s.connect(('2.2.2.2', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()

    return ip


def auth(func):
    def func1(*args, **kwargs):
        if client.user_info:
            res = func(*args, **kwargs)
            return res
        else:
            print('未登录')

    return func1


from bin import client
