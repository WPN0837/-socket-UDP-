import pickle
import configparser
# import os, sys
# path = os.path.dirname(os.path.dirname(__file__))
# sys.path.append(path)
from config import setting
class course:
    def __init__(self, id = None, name = None, teacher = None):
        self.id = id
        self.name = name
        self.teacher = teacher
    def __str__(self):
        return str(self.id) +' '+ self.name
    def get_course_dic(self):
        with open(setting.COURSE_DB_PATH, 'rb') as file:
            return pickle.load(file)
    def save_course_dic(self, course_dic):
        with open(setting.COURSE_DB_PATH, 'wb') as file:
            pickle.dump(course_dic, file)
    def create_course(self):
        while True:
            name = input('课程名：')
            course_dic = self.get_course_dic()
            conf = configparser.ConfigParser()
            conf.read(setting.CONFIG_PATH)
            gid = int(conf['COURSE']['id'])
            conf['COURSE']['id'] = str(gid + 1)
            conf.write(open(setting.CONFIG_PATH, 'w'))
            course_dic[name] = course(gid + 1, name)
            self.save_course_dic(course_dic)
            return
    def delete_course(self, cid):
        course_dic = self.get_course_dic()
        for k, v in course_dic.items():
            if v.id == cid:
                course_dic.pop(k)
                break
        self.save_course_dic(course_dic)

# dic = {}
# with open(setting.COURSE_DB_PATH, 'wb') as file:
#     pickle.dump(dic, file)


# c = course()
# c.create_course()
# print(c.get_course_dic())
# c.delete_course(1)