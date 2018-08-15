import pickle
import configparser
import os, sys
path = os.path.dirname(os.path.dirname(__file__))
sys.path.append(path)
from config import setting
class school:
    def __init__(self, id = None, name = None , group_dic = None):
        self.id = id
        self.name = name
        self.group_dic = group_dic
    def __str__(self):
        return str(self.id) +' '+ self.name
    def get_school_dic(self):
        with open(setting.SCHOOL_DB_PATH, 'rb') as file:
            return pickle.load(file)
    def save_school_dic(self, school_dic):
        with open(setting.SCHOOL_DB_PATH, 'wb') as file:
            pickle.dump(school_dic, file)
    def create_school(self):
        while True:
            name = input('学校名：')
            school_dic = self.get_school_dic()
            conf = configparser.ConfigParser()
            conf.read(setting.CONFIG_PATH)
            gid = int(conf['SCHOOL']['id'])
            conf['SCHOOL']['id'] = str(gid + 1)
            conf.write(open(setting.CONFIG_PATH, 'w'))
            school_dic[name] = school(gid+1, name)
            self.save_school_dic(school_dic)
            return
    def delete_school(self, gid):
        school_dic = self.get_school_dic()
        for k, v in school_dic.items():
            if v.id == gid:
                school_dic.pop(k)
                break
        self.save_school_dic(school_dic)

# dic = {}
# with open(setting.SCHOOL_DB_PATH, 'wb') as file:
#     pickle.dump(dic, file)

# s = school()
# s.create_school()
# print(s.get_school_dic())
# s.delete_school(1)