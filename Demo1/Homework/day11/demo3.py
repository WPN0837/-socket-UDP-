'''
编写装饰器，为函数加上认证的功能
'''
session = {"name": 'egon'}
def zhuangshiqi(func):
    def wrapper(*args, **kwargs):
        res = ''
        if session:
            res = func(*args, **kwargs)
        else:
            print('未登录！')
        return res
    return wrapper
@zhuangshiqi
def func():
    print('程序功能！')
func()

