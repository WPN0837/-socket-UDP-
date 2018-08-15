from conf import setting
from lib.dao import dao
from lib import tool

d = dao(setting.ADMIN)


class admin:

    def __init__(self, name, password):
        self.name = name
        self.password = password
        self.id = tool.get_id(admin.__name__)
        d.save(self)
