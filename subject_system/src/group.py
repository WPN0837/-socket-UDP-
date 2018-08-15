from conf import setting
from lib.dao import dao
from lib import tool

d = dao(setting.GROUP)


class group:
    student_list = []

    def __init__(self, name):
        self.name = name
        self.id = tool.get_id(group.__name__)
        d.save(self)
