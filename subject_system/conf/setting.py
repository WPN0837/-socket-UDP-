import os
# path = os.path.dirname(__file__)
SCHOOL = '../db/school.db'#学校
TEACHER = '../db/teacher.db'#讲师
COURSE = '../db/course.db'#课程
STUDENT = '../db/student.db'#学员
ADMIN = '../db/admin.db'#管理员
GROUP = '../db/group.db'#班级
CONFIG = '../conf/subject.config'#配置文件

#初始化
# import pickle
# import configparser
# dic = {}
# l = [SCHOOL,TEACHER,COURSE,STUDENT,ADMIN,GROUP,CONFIG]
# for i in l:
#     with open(i,'wb') as f:
#         pickle.dump(dic,f)
# conf = '[SCHOOL]\nid = 0\n[TEACHER]\nid = 0\n[COURSE]\nid = 0\n[STUDENT]\nid = 0\n[ADMIN]\nid = 0\n[GROUP]\nid = 0\n'
# with open('subject.config', 'w', encoding='utf-8') as f:
#     f.write(conf)