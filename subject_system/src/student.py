'''
属性：学校、班级
方法：注册、交学费、选择班级
'''
from conf import setting
from lib.dao import dao
from lib import tool
d = dao(setting.STUDENT)


class student:
    tuition = None
    group = None

    def __init__(self, name, password, school, group):
        self.name = name
        self.password = password
        self.school = school
        self.group = group
        self.id = tool.get_id(student.__name__)
        d.save(self)

    def register(self, name, school, group):
        return student(name, school, group)

    def pyment(self, tuition):
        self.tuition = tuition
        d.save(self)

    def choice_group(self, group):
        self.group = group
        d.save(self)