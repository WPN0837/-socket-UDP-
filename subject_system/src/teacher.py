'''
属性：学校
方法：上课选择班级、查看班级学员列表、修改管理学员的成绩
'''
from conf import setting
from lib import tool
from lib.dao import dao
d = dao(setting.TEACHER)


class teacher:
    '''

    '''
    group = None

    def __init__(self, name, password, school,):
        self.name = name
        self.password = password
        self.school = school
        self.id = tool.get_id(teacher.__name__)
        d.save(self)

    def choice_group(self, group):
        self.group = group
        d.save(self)

    def get_group_student(self):
        if self.group:
            return self.group.list
        return None

    def change_student_score(self, sid, score):
        pass
# t =teacher('name', 'p', 'p')
# print(t.__dict__)
# import configparser
# conf = configparser.ConfigParser()
# conf.read(setting.CONFIG)
# print(conf.sections())
# dic = d.read()
# print(dic)