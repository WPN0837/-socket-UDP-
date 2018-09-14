from socket import *


def get_host_ip():
    try:
        s = socket(AF_INET, SOCK_DGRAM)
        s.connect(('2.2.2.2', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()

    return ip
