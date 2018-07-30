# with open('a.txt', 'r+', encoding='utf-8') as f:
# #     print(f.tell())
# #     f.seek(3, 0)
# #     f.truncate(6)
# s = 'bilibili'
# s.replace('i', 'l')
# print(s)



# def f():
#     global name
#     name = '456'3
#     # print(name)
# def f1():
#     global name
#     print(type(name))
#
# f()
# f1()

#高阶函数调用
# name = 'xiaoming'
# def change(s):
#     def change1(str):
#         print('内函数', str)
#     change1('change()调用')
#     print('外函数', s)
#     return change1
#
# f = change('外部调用')
# f('外部调用')

# i = 1
# while i < 8:
#     if i ==4:
#         continue
#     print(i)
#     i += 1


# level = 'l0'
# n = 22
#
# def func():
#     level = 'l1'
#     n = 33
#     print(locals())
#
#     def outer():
#         level = 'l2'
#         print(locals(), n)
#
#         def inner():
#             level = 'l3'
#             print(locals(), n)
#         inner()
#     outer()
#
# func()

#闭包
# def func(str = 'func'):
#     name = str
#     def toString(str = 'toString'):
#         nonlocal name
#         print(name)
#         name = 'new'
#         print(name)
#         print(str)
#     return toString
#
# f = func()
# f()


#装饰器
#无参
# import time
# def dec(func):
#     def wrapper():
#         start_time = time.time()
#         func()
#         over_time = time.time()
#         print(over_time - start_time)
#     return wrapper
#
# @dec
# def func():
#     print('hello world')
#
# f = func
# f()

# 装饰器
# 多个装饰器
#  多参数
# import time
# def dec1(func):#装饰器1  参数为被装饰的函数func
#     print('dec1', func.__name__)#打印装饰器的名字及被装饰的函数名
#     def wrapper1(*args, **kwargs):
#         start_time = time.time()
#         func(*args, **kwargs)#可同时传入多个参数，是具体函数而定
#         end_time = time.time()
#         print('dec1', end_time - start_time)
#     return wrapper1
#
# def dec2(func):#装饰器2
#     print('dec2', func.__name__)
#     def wrapper2(*args, **kwargs):
#         start_time = time.time()
#         func(*args, **kwargs)#可同时传入多个参数，是具体函数而定
#         end_time = time.time()
#         print('dec2', end_time - start_time)
#     return wrapper2
#
# def dec3(func):#装饰器3
#     print('dec3', func.__name__)
#     def wrapper3(*args, **kwargs):
#         start_time = time.time()
#         func(*args, **kwargs)#可同时传入多个参数，是具体函数而定
#         end_time = time.time()
#         print('dec3', end_time - start_time)
#     return wrapper3
#
# @dec1
# @dec2
# @dec3
# def func(a, b):#函数func，同时被3个装饰器装饰
#     print(a, b)
#
#
# @dec2
# def func1(a, b, c):#函数func1   与函数func 对比 二者参数的个数不同
#     print(a, b, c)
#
# if __name__ == '__main__':
#     func('1', '2')
#     func1(1, 2, 3)

#生成器
# import time
# def consumer(name):
#     print('%s准备吃包子啦！' % name)
#     while True:
#         baozi = yield
#         print('包子[%s]来了，被[%s]吃了！' % (baozi, name))
# def produce(name):
#     c = consumer('A')
#     c2 = consumer('B')
#     c.__next__()
#     c2.__next__()
#     print('老子开始准备做包子啦！')
#     for i in range(10):
#         time.sleep(1)
#         print('做了2个包子！')
#         c.send(i)
#         c2.send(i)
# produce('alex')



'''
ABBA
12ABBA
A
ABAKK
51233214
abaaab


'''
# def func(str):
#     if str == str[::-1]:
#         return len(str)
#     else:
#         return -1
#
# def func1(str):
#     for i in list(range(1, len(str) + 1))[::-1]:
#         for j in range(0, len(str)):
#             if i + j <= len(str):
#                 if func(str[j:j+i]) > 0:
#                     return func(str[j:j+i])
#             else:
#                 break
#     return -1
#
# if __name__ == '__main__':
#     while True:
#         c = input(':')
#         if c == '':
#             break
#         print(func1(c))



# s ='hello alex alex say hello sb sb'
# l = s.split()
# d = {}
# for i in l:
#     d[i] = l.count(i)
# print(d)



# import time
# import codecs
# import os
# root = r"C:\Users\WPN\PycharmProjects\ATM"#root代表你放作业的文件夹
# list1=[]
# dict_time={}
# timeset={}
# dict_code={}
# dict_time_code={}
# def TimeStampToTime(timestamp):
#     timeStruct = time.localtime(timestamp)
#     return time.strftime('%Y-%m-%d',timeStruct)
# for dirpath, dirnames, filenames in os.walk(root):
#     for filepath in filenames:
#         if str(filepath).endswith(".py"):
#             str1=str(os.path.join(dirpath, filepath))
#             list1.append(str1)
# for i in list1:
#     dict_time[i]=TimeStampToTime(os.path.getctime(i))
# for i in list1:
#     dict_code[i]=int(len(codecs.open(i, 'rU', 'utf-8').readlines()))
#     #print(dict_code[i])
# timeset=set(dict_time.values())
# for i in iter(timeset):
#     dict_time_code[i]=0
# for i in iter(timeset):
#     for j in list1:
#         if dict_time[j]==i:
#             dict_time_code[i]+=dict_code[j]
# for (key,value) in dict_time_code.items():
#        print(key+':写了'+str(value)+"行代码！")
# T=True if input("是否显示你的作业(Y/n)")=='Y' else False
# if T:
#     print("你的作业文件")
#     for i in list1:
#         print(i)


#监听文件改动
# path = 'a.txt'
# with open(path, 'rb') as file:
#     file.seek(0, 2)
#     while True:
#         line = file.readline()
#         if len(line) != 0:
#             print(line.decode('utf-8'), end='')


# from Demo1.Test1 import test

# list = [1,2,3]
# def foo(m, l = list):
#     print(m, l)
# list.append(4)
# foo(1)

# def foo(x, y, z):
#     print(x, y, z)
# foo(1, *(1, 2, 3)[0:2])