'''
属性：
方法：创建课程、创建班级
'''
from conf import setting
from lib.dao import dao
from lib import tool
from src.course import course
from src.group import group
d = dao(setting.SCHOOL)


class school:
    group_list = []
    course_list = []

    def __init__(self, name):
        self.name = name
        self.id = tool.get_id(school.__name__)
        d.save(self)

    def create_group(self, name):
        self.group_list.append(group(name))
        d.save(self)

    def create_course(self, name):
        self.course_list.append(course(name))
        d.save(self)