import pickle
import configparser
# import os, sys
# path = os.path.dirname(os.path.dirname(__file__))
# sys.path.append(path)
from config import setting
class teacher:
    def __init__(self, id = None, name = None, password = None, age = None):
        self.id = id
        self.name = name
        self.password = password
        self.age = age
    def __str__(self):
        return str(self.id) +' '+ self.name
    def get_teacher_dic(self):
        with open(setting.TEACHER_DB_PATH, 'rb') as file:
            return pickle.load(file)
    def save_teacher_dic(self, teacher_dic):
        with open(setting.TEACHER_DB_PATH, 'wb') as file:
            pickle.dump(teacher_dic, file)
    def create_teacher(self):
        while True:
            name = input('老师姓名:')
            password = input('密码：')
            password1 = input('重复密码：')
            if password != password1:
                print('两次密码不一样！')
            else:
                teacher_dic = self.get_teacher_dic()
                conf = configparser.ConfigParser()
                conf.read(setting.CONFIG_PATH)
                tid = int(conf['TEACHER']['id'])
                conf['TEACHER']['id'] = str(tid+1)
                conf.write(open(setting.CONFIG_PATH, 'w'))
                teacher_dic[name] = teacher(tid + 1, name, password)
                self.save_teacher_dic(teacher_dic)
                return
    def delete_teacher(self, tid):
        teacher_dic = self.get_teacher_dic()
        for k, v in teacher_dic.items():
            if v.id == tid:
                teacher_dic.pop(k)
                break
        self.save_teacher_dic(teacher_dic)