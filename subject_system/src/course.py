'''
属性：周期、价格
方法：
'''
from conf import setting
from lib.dao import dao
from lib import tool
d = dao(setting.COURSE)


class course:
    cycle = None
    price = None

    def __init__(self):
        pass