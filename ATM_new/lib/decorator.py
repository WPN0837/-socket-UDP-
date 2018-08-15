from bin import main

from lib import logger

def log_decorator(Type):#日志
    def decorator(func):
        def function(*args, **kwargs):
            res = func(*args, **kwargs)
            if res:
                event = ' '.join(res)
                logger.logger(Type,event)
            return res
        return function
    return decorator

def user_state_decorator(func):#检验用户登录状态
    def function(*args, **kwargs):
        res = None
        if main.user_info:
            res = func(*args, **kwargs)
        else:
            print('当前未登录，请登陆')
        return res
    return function

