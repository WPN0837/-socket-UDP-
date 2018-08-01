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
# with open('pickle', 'wb')as f:
#     pickle.dump(dic, f)
# with open('pickle', 'rb')as f:
#     d = pickle.load(f)
# d1 = pickle.loads(data)
#
# print(d)
# print(d1)



# import json
# dic = {"name": "egon", "password": "abc123"}
# str_dic = str(dic)
# str_dic1 = '{"name": "egon", "password": "abc123"}'
# print(json.loads(str_dic1))
# print(str_dic)
# print(json.dumps(dic))
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

import shelve
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

