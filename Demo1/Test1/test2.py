# def decorator(func):
#     print('装饰器')
#     def function(info_dic = {}):
#         if len(info_dic) == 0:
#             print('当前未登陆，请登陆！')
#         else:
#             func(info_dic)
#     return function
# def decorator1(func):
#     print('装饰器1')
#     def function(*args, info_dic = {}):
#         if len(info_dic) == 0:
#             print('当前未登陆，请登陆！')
#         else:
#             func(*args, info_dic)
#     return function
# @decorator
# def func1(info_dic = {}):
#     print(info_dic)
#     print('hello')
#
# # func1({"nihao":"你好"})
#
#
# @decorator1
# def func2(*args, info_dic = {}):
#     print(info_dic)
#     print('122313')
#
#
# if __name__ == '__main__':
#     func1()
#     func2({"nihao":"你好"})

# def delete_cart():#从购物车删除商品
#     falg = False
#     for i in range(10):
#         falg = True
#         break
#     if falg:
#         print(str(falg)+'is True')
#     return falg
# print(delete_cart())

# def f():
#     return False
# print(f())

# import os
#
# with open('d.txt', 'rt', encoding='utf-8') as read_f, \
#         open('d.txt.x', 'wt', encoding='utf-8') as wirte_f:
#     for info in read_f:
#         wirte_f.write(info.replace('帅逼', 'Jack'))
#
# os.remove('d.txt')
# os.rename('d.txt.x', 'd.txt')

#汉诺塔
# def Hanno_Tower(x, y, z, n):
#     if n == 1:
#         print('%s -> %s' % (x, z))
#         #x->z
#     else:
#         Hanno_Tower(x, z, y, n-1)
#         Hanno_Tower(x, y, z, 1)
#         Hanno_Tower(y, x, z, n-1)
# Hanno_Tower('A', 'B', 'C', 3)


# import os, sys
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(BASE_DIR)
# sys.path.append(BASE_DIR)
# from Test1 import test
# print('hello')

# import os
# file = ''
#
# for i in os.listdir(r'C:\Users\WPN\PycharmProjects\Demo1'):
#     if os.path.isdir(r'C:\Users\WPN\PycharmProjects\Demo1'+'\\'+i):
#         print(i)


# import pickle
# dic = {'name': 'egon', 'password': 'abc123'}
# data = pickle.dumps(dic)
# print(data)
# with open('pickle', 'wb')as f:
#     pickle.dump(dic, f)
# with open('pickle', 'rb')as f:
#     dic2 = pickle.load(f)
# print(dic2)
# dic1 = pickle.loads(data)
# print(dic1)
# print(d)
# print(d1)



# import json
# dic = {"name": "egon", "password": "abc123"}
# str_dic = str(dic)
# str_dic1 = '{"name": "egon", "password": "abc123"}'
# print(json.loads(str_dic1))
# print(str_dic)
# print(type(json.dumps(dic)))
# def dic2student(dic):
#     s = student(dic['name'], dic['age'])
#     return s
# class student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
# s = student('egon', 22)
# dic1 = {"model": s}
# data = json.dumps(s, default=lambda obj: obj.__dict__)
# print(json.loads(data, object_hook=dic2student).name)
# print(data)
# with open('info.json', 'w')as info:
#     json.dump(s, info, default=lambda obj: obj.__dict__)
# with open('info.json', 'r')as info:
#     data = json.load(info,object_hook=dic2student)
# print(data.name)

# import shelve
# f = shelve.open('info.shelve', 'w')
# f['name'] = 'alex'
# f.close()
# f = shelve.open('info.shelve', 'r')
# print(f['name'])
# f.close()
# with shelve.open('info.shelve', 'r')as f:
#     print(f['name'])
# with shelve.open('info.shelve', 'w')as f:
#     f['name'] = 'egon'


# import json
# class student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    # def tostr(self):
#         print(self.name, self.age)
# s = student('bighead', 22)
# def student_to_dict(s):
#     return {'name': s.name, 'age': s.age}
# def dict_to_student(dic):
#     return student(dic['name'], dic['age'])
# data = json.dumps(s, default=student_to_dict)
# print(data)
# data = json.dumps(s, default=lambda obj:obj.__dict__)
# print(data)
# s = json.loads(data, object_hook=dict_to_student)
# print(type(s))
# s.tostr()
# dic = {"name": "egon", "password": "abc123"}
# with open('info.json', 'r') as file:
#     data = json.load(file)
#     print(type(data))
#     print(data)


# import time
# def index():
#     time.sleep(2)
#     print('hello world')
#
# def zhuangshi(func):
#     x = func
#     def w(x = func):
#         start = time.time()
#         func()
#         stop = time.time()
#         print('运行时间：%s' % (stop - start))
#     return w
# index = zhuangshi(index)
# index()


#用户登陆装饰器
# userstate = {}
# def zhuangshiqi(func):
#     def wrapper(username, password):
#         res = func(username, password)
#         if res:
#             if username in userstate and userstate[username] >= 2:
#                 print('账号被锁定！')
#                 res = False
#         else:
#             if username in userstate:
#                 userstate[username] += 1
#             else:
#                 userstate[username] = 0
#         return res
#     return  wrapper
# @zhuangshiqi
# def login(username, password):
#     if username == 'oldboy' and password == 'abc123':
#         return True
#     else:
#         return False
# tag = True
# while tag:
#     username = input('用户名：')
#     password = input('密码：')
#     if login(username, password):
#         tag = False


# l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# def func(i, l):
#     if not l:
#         return False
#     elif i == l[len(l)//2]:
#         return True
#     elif i < l[len(l)//2]:
#         return func(i, l[:len(l)//2])
#     else:
#         return func(i, l[len(l) // 2+1:])
# print(func(13, l))



# l = [1,2,3,4,5]
# l1 = ['a','b','c','d','e']
# dic = dict(zip(l1,l))
# print(dic)
# res = min(dic, key=lambda k: dic[k])
# print(res)


# class student:
#     def __init__(self, val):
#         self.__NAME = val
#         self.age = 20
#         pass
#     @classmethod
#     def show(cls):
#         print("show func%s"% cls.__name__)
#     @property
#     def name(self):
#         pass
#     # @name.setter
#     # def name(self, value):
#     #     self.__NAME = value
#     # @name.getter
#     # def name(self):
#     #     return self.__NAME
# s = student('v')
# # s.name = 't'
# # print(s.name)
# print(hasattr(s, 'age'))
# print(getattr(s, 'age', 404))
# print(getattr(s, 'a', 404))
# setattr(s, 'g', 'G')
# def func():
#     print('创建的func')
# # setattr(s, 'show', func)
# s.show()
# # def set_age(self, age):
# #     self.age = age
# #     print(s.age)
# # from types import MethodType
# # student.set_age = MethodType(set_age, student)
# # s.sex = 'man'
# # print(s.sex)