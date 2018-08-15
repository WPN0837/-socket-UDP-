import pickle
import configparser
# import os, sys
# path = os.path.dirname(os.path.dirname(__file__))
# sys.path.append(path)
from config import setting
class group:
    def __init__(self, id = None, name = None, student_dic = None, teacher_dic = None):
        self.id = id
        self.name = name
        self.student_dic = student_dic
        self.teachser_dic = teacher_dic
    def __str__(self):
        return str(self.id) +' '+ self.name
    def get_group_dic(self):
        with open(setting.GROUP_DB_PATH, 'rb') as file:
            return pickle.load(file)
    def save_group_dic(self, group_dic):
        with open(setting.GROUP_DB_PATH, 'wb') as file:
            pickle.dump(group_dic, file)
    def create_group(self):
        while True:
            name = input('班级名：')
            group_dic = self.get_group_dic()
            conf = configparser.ConfigParser()
            conf.read(setting.CONFIG_PATH)
            gid = int(conf['GROUP']['id'])
            conf['GROUP']['id'] = str(gid + 1)
            conf.write(open(setting.CONFIG_PATH, 'w'))
            group_dic[name] = group(gid+1, name)
            self.save_group_dic(group_dic)
            return
    def delete_group(self, gid):
        group_dic = self.get_group_dic()
        for k, v in group_dic.items():
            if v.id == gid:
                group_dic.pop(k)
                break
        self.save_group_dic(group_dic)