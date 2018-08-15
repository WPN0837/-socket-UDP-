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


# 类的继承
# class Foo:
#     __name = 'Foo'
#     def __f1(self):
#         print('Foo_f1')
#     def f2(self):
#         print('Foo_f2')
#         self.__f1()
# class Foo1():
#     def __f1(self):
#         print('Foo1_f1')
#     def f2(self):
#         print('Foo1_f2')
#         self.__f1()
# class Foo2(Foo1):
#     def __f1(self):
#         print('Foo2_f1')
#     def f2(self):
#         print('Foo2_f2')
#         self.__f1()
# class Foo3(Foo2, Foo1):
#     # def __f1(self):
#     #     print('Foo3_f1')
#     # def f2(self):
#     #     print('Foo3_f2')
#     #     self.__f1()
#     pass
# class Foo4(Foo3):
#     def __f1(self):
#         print('Foo4_f1')
#     def f2(self):
#         print('Foo4_f2')
#         self.__f1()
#     pass
# f = Foo()
# print(Foo4.mro())
# f.f2()
# print(f._Foo__name)
# class Foo1(Foo,Foo2):
#     def f1(self):
#         print('Foo1_f1')
#         super().f1()
# print(Foo1.mro())
# F = Foo1()
# F.f1()

#抽象类
# import abc
# class A(metaclass = abc.ABCMeta):
#     name = 'A'
#     @abc.abstractmethod
#     def call(self):
#         pass
#     @abc.abstractmethod
#     def get_name(self):
#         pass
#     @abc.abstractmethod
#     def put(self):
#         print('AAAA')
# class B(A):
#     name = 'B'
#     def call(self):
#         print('this is B')
#     def get_name(self):
#         print(self.name)
#     def p(self):
#         print(super().name)
#     def put(self):
#         print('AAAA')
# b = B()
# b.p()
# b.get_name()
# b.put()



# class Foo:
#     __name = 'Foo'
#     # def __init__(self):
#     #     self.__name = 'Foo'
#     def __f1(self):
#         print('Foo_f1')
#     @property
#     def f2(self):
#         return self.__name
#     @f2.setter
#     def f2(self, value):
#         self.__name = value
#     @f2.getter
#     def f2(self):
#         return self.__name
#     @f2.deleter
#     def f2(self):
#         del self.__name
# f = Foo()
# print(f.f2)
# print(Foo._Foo__name)
# f.f2 = 'new'
# print(f.f2)
# print(Foo._Foo__name)
# f.name = 'new name'
# print(f.name)
# def put():
#     print('hello')
# f.put = put
# f.put()
# print(Foo().f2)
# del f.f2
# print(f.f2)



# class Foo:
#     name = 'Foo'
#     def set(self):
#         self.name = 'new Foo'
#     def put(self):
#         print(self.name)
# f = Foo()
# f.set()
# Foo.put(f)
# print(dir(Foo))
# print(Foo.__dict__)


# import random
# class MySQL:
#     _id_list = []
#     _id = ''
#     host = ''
#     port = ''
#     def __init__(self, host = '', port = ''):
#         if host and port:
#             self.host = host
#             self.port = port
#         else:
#             with open('', 'r', encoding='utf-8') as f:
#                 line = f.readline()
#             line_list = line.split('|')
#             self.host = line_list[0]
#             self.port = line_list[1]
#
#     def create_id(cls):
#         _id = random.randint(1, 1000)
#         cls._id_list.append(_id)



# def rangge(m = 0, n = 0):
#     if m and n:
#         while m < n:
#             yield  m
#             m += 1
#     elif not m and n:
#         while m < n:
#             yield  m
#             m += 1
# g = rangge(0, 10)
# for i in g:
#     print(i)

# def func(*args):
#     num = 0
#     stage = 1
#     if len(args) == 1:
#         while num < args[0]:
#             yield num
#             num += stage
#     elif len(args) == 2:
#         num = args[0]
#         while num < args[1]:
#             yield num
#             num += stage
#     elif len(args) == 3:
#         num = args[0]
#         stage = args[2]
#         while num < args[1]:
#             yield num
#             num += stage
#     else:
#         print('错误')
# for i in func(10):
#     print(i)

#面试题 生成器在next()运行之前不会执行内部代码
# def add(n, i):
#     return n+i
# def test():
#     for i in range(4):
#         yield i
# g = test()
# for n in [1, 10]:
#     g = (add(n, i) for i in g)
# print(list(g))

# s = '你好'
# s1 = s.encode('utf-8')
# s2 = s1.decode('utf-8')
# print(s1, s2)


# list = [1, 2, 3, 4]
# def f(i):
#     return i-1
# def map(func, list):
#     for i in range(len(list)):
#         list[i] = func(list[i])
#     return list
# list = map(f, list)
# print(list)

# class A:
#     name = 'A'
#     def __setattr__(self, key ,value):
#         self.__dict__[key] = value
#         print('添加了%s值为%s' % (key, value))
#     def __getattr__(self, item):
#         print('huoqu')
#         # if item in self.__dict__:
#         #     return self.__dict__[item]
#     def __delattr__(self, item):
#         self.__dict__.pop(item)
# a = A()
# setattr(a, 'age', 20)
# getattr(a, 'ag')
# print(a.__dict__)
# del a.age
# print(a.__dict__)
# a.age

# i = '10000'
# print(int(i, base=2))


# class Str:
#     def __get__(self, instance, owner):
#         print('get')
#     def __set__(self, instance, value):
#         print('set')
#     def __delete__(self, instance):
#         print('del')
# class person:
#     name = Str()
#     def __init__(self, name):
#         self.name = name
#     def __str__(self):
#         return self.name
# p = person('老母鸡')
# p.name = '老扁嘴'
# person.name = '老母猪'
# print(person.name)
# del p.name
# print(p.name)
# print(person.__dict__)
# print(p.__dict__)
# print(type(p) == person)
# print(type(p).__dict__ == person.__dict__)


# #描述符Str
# class Str:
#     def __get__(self, instance, owner):
#         print('Str调用')
#     def __set__(self, instance, value):
#         print('Str设置...')
#     def __delete__(self, instance):
#         print('Str删除...')
#
# #描述符Int
# class Int:
#     def __get__(self, instance, owner):
#         print('Int调用')
#     def __set__(self, instance, value):
#         print('Int设置...')
#     def __delete__(self, instance):
#         print('Int删除...')
#
# class People:
#     name=Str()
#     age=Int()
#     def __init__(self,name,age): #name被Str类代理,age被Int类代理,
#         self.name=name
#         self.age=age
#
# #何地？：定义成另外一个类的类属性
#
# #何时？：且看下列演示
#
# p1=People('alex',18)
#
# #描述符Str的使用
# p1.name
# p1.name='egon'
# del p1.name
#
# #描述符Int的使用
# p1.age
# p1.age=18
# del p1.age
#
# #我们来瞅瞅到底发生了什么
# print(p1.__dict__)
# print(People.__dict__)
#
# #补充
# print(type(p1) == People) #type(obj)其实是查看obj是由哪个类实例化来的
# print(type(p1).__dict__ == People.__dict__)


# l=[1,[2,[3,[4,[5,[6,[7,[8,[9,[10,[11,]]]]]]]]]]]
# l1 = []
# def search(l):
#     for item in l:
#         if type(item) is not list:
#             # 不是列表直接打印
#             print(item)
#             l1.append(item)
#         else:
#             # 判断是列表则继续循环,判断...
#             search(item)
# search(l)
# l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# print(l1)
# l = []
# def put(l1):
#     if len(l1) == 1:
#         return l1
#     return [l1[0], put(l1[1:])]
# l = put(l1)
# print(l)


# class Str:
#     def __init__(self,name):
#         self.name=name
#         print(self.name)
#     def __get__(self, instance, owner):
#         print('get--->',instance,owner)
#         return instance.__dict__[self.name] # 返回值
#
#     def __set__(self, instance, value):
#         print('set--->',instance,value)
#         instance.__dict__[self.name]=value #修改值
#     def __delete__(self, instance):
#         print('delete--->',instance)
#         instance.__dict__.pop(self.name)# 删除值
#
#
# class People:
#     name=Str('name')
#     sex = Str('sex')
#     def __init__(self,name,age,salary):
#         self.sex = '男'
#         self.name=name
#         self.age=age
#         self.salary=salary
#
# p1=People('egon',18,3231.3)
#
# #调用
# print(p1.__dict__)
# print(p1.name)
# print(p1.sex)
#
# # 赋值
# print(p1.__dict__)
# p1.name='egonlin'
# print(p1.__dict__)
#
# #删除
# print(p1.__dict__)
# del p1.name
# print(p1.__dict__)

# class Str:
#     def __init__(self,name):
#         self.name=name
#     def __get__(self, instance, owner):
#         print('get--->',instance,owner)
#         return instance.__dict__[self.name]
#
#     def __set__(self, instance, value):
#         print('set--->',instance,value)
#         instance.__dict__[self.name]=value
#     def __delete__(self, instance):
#         print('delete--->',instance)
#         instance.__dict__.pop(self.name)
#
#
# class People:
#     name=Str('name')
#     def __init__(self,name,age,salary):
#         self.name=name
#         self.age=age
#         self.salary=salary
#
# #疑问:如果我用类名去操作属性呢
# People.name #报错,错误的根源在于类去操作属性时,会把None传给instance

#修订__get__方法
# class Str:
#     def __init__(self,name):
#         self.name=name
#     def __get__(self, instance, owner):
#         print('get--->',instance,owner)
#         if instance is None:  #与上面的区别
#             return self
#         return instance.__dict__[self.name]
#
#     def __set__(self, instance, value):
#         print('set--->',instance,value)
#         instance.__dict__[self.name]=value
#     def __delete__(self, instance):
#         print('delete--->',instance)
#         instance.__dict__.pop(self.name)
#
#
# class People:
#     name=Str('name')
#     def __init__(self,name,age,salary):
#         self.name=name
#         self.age=age
#         self.salary=salary
# print(People.name) #完美,解决

# class Str:
#     def __init__(self,name,expected_type):
#         self.name=name
#         self.expected_type=expected_type
#     def __get__(self, instance, owner):
#         print('get--->',instance,owner)
#         if instance is None:
#             return self
#         return instance.__dict__[self.name]
#
#     def __set__(self, instance, value):
#         print('set--->',instance,value)
#         if not isinstance(value,self.expected_type): #如果不是期望的类型，则抛出异常
#             raise TypeError('Expected %s' %str(self.expected_type))
#         instance.__dict__[self.name]=value
#     def __delete__(self, instance):
#         print('delete--->',instance)
#         instance.__dict__.pop(self.name)
#
#
# class People:
#     name=Str('name',str) #新增类型限制str
#     def __init__(self,name,age,salary):
#         self.name=name
#         self.age=age
#         self.salary=salary
#
# p1=People(123,18,3333.3)#传入的name因不是字符串类型而抛出异常


# class Typed:
#     def __init__(self,name,expected_type):
#         self.name=name
#         self.expected_type=expected_type
#     def __get__(self, instance, owner):
#         print('get--->',instance,owner)
#         if instance is None:
#             return self
#         return instance.__dict__[self.name]
#
#     def __set__(self, instance, value):
#         print('set--->',instance,value)
#         if not isinstance(value,self.expected_type):
#             raise TypeError('Expected %s' %str(self.expected_type))
#         instance.__dict__[self.name]=value
#     def __delete__(self, instance):
#         print('delete--->',instance)
#         instance.__dict__.pop(self.name)
#
#
# class People:
#     name=Typed('name',str)
#     age=Typed('name',int)
#     salary=Typed('name',float)
#     def __init__(self,name,age,salary):
#         self.name=name
#         self.age=age
#         self.salary=salary
#
# # p1=People(123,18,3333.3)
# # p1=People('egon','18',3333.3)
# # p1=People('egon',18,3333)
# p1=People('egon',18,3333.0)


# 类的无参装饰器
# def decorate(cls):
#     print('类的装饰器开始运行啦------>')
#     return cls
#
# @decorate #无参:People=decorate(People)
# class People:
#     def __init__(self,name,age,salary):
#         self.name=name
#         self.age=age
#         self.salary=salary
#
# p1=People('egon',18,3333.3)

# 类的有参装饰器
# def typeassert(**kwargs):
#     def decorate(cls):
#         print('类的装饰器开始运行啦------>',kwargs)
#         return cls
#     return decorate
# @typeassert(name=str,age=int,salary=float) #有参:1.运行typeassert(...)返回结果是decorate,此时参数都传给kwargs 2.People=decorate(People)
# class People:
#     def __init__(self,name,age,salary):
#         self.name=name
#         self.age=age
#         self.salary=salary
#
# p1=People('egon',18,3333.3)



# class Typed:# 描述符类
#
#     def __init__(self, name, expected_type):
#         '''
#         :param name: 参数名
#         :param expected_type: 参数类型
#         '''
#         self.name = name
#         self.expected_type = expected_type
#
#     def __get__(self, instance, owner):
#         '''
#         :param instance:被代理的类的对象
#         :param owner:被代理的类
#         :return:
#         '''
#         print('get--->', instance, owner)
#         if instance is None:
#             return self
#         return instance.__dict__[self.name]
#
#     def __set__(self, instance, value):
#         '''
#         :param instance: 被代理的类的对象
#         :param value: 要赋的值
#         :return:
#         '''
#         print('set--->', instance, value)
#         if not isinstance(value, self.expected_type):
#             raise TypeError('Expected %s' % str(self.expected_type))
#         instance.__dict__[self.name] = value
#
#     def __delete__(self, instance):
#         '''
#         :param instance:
#         :return:
#         '''
#         print('delete--->', instance)
#         instance.__dict__.pop(self.name)
#
#
# def typeassert(**kwargs):
#     '''
#     :param kwargs: 类中定义的属性及类型
#     :return:
#     '''
#     def decorate(cls): # 返回一个新类，并在类中设置参数
#         '''
#         :param cls: 被装饰的类
#         :return:
#         '''
#         print('类的装饰器开始运行啦------>', kwargs)
#         for name, expected_type in kwargs.items():
#             setattr(cls, name, Typed(name, expected_type))# 在cls中设置属性
#         return cls
#     return decorate
#
# @typeassert(name=str, age=int, salary=float) #有参:1.运行typeassert(...)返回结果是decorate,此时参数都传给kwargs 2.People=decorate(People)
# class People:
#     def __init__(self, name, age, salary):
#         self.name = name
#         self.age = age
#         self.salary = salary
#
# print(People.__dict__)
# p1 = People('egon', 18, 3333.3)
# p1.name
# print(p1, People)


# property装饰器的使用示例
# class Room:
#     def __init__(self,name,width,length):
#         self.name=name
#         self.width=width
#         self.length=length
#
#     @property
#     def area(self):
#         return self.width * self.length
#
# r1=Room('alex',1,1)
# print(r1.area)


# class Lazyproperty:
#     def __init__(self,func):
#         self.func=func
#     def __get__(self, instance, owner):
#         print('这是我们自己定制的静态属性,r1.area实际是要执行r1.area()')
#         if instance is None:
#             return self
#         return self.func(instance) #此时你应该明白,到底是谁在为你做自动传递self的事情
#
# class Room:
#     def __init__(self,name,width,length):
#         self.name=name
#         self.width=width
#         self.length=length
#
#     @Lazyproperty #area=Lazyproperty(area) 相当于定义了一个类属性,即描述符
#     def area(self):
#         return self.width * self.length
#
# r1=Room('alex',1,1)
# print(r1.area)

# 用类作装饰器
# class Lazyproperty:
#     def __init__(self,func):
#         self.func=func
#     def __get__(self, instance, owner):
#         print('这是我们自己定制的静态属性,r1.area实际是要执行r1.area()')
#         if instance is None:
#             return self
#         else:
#             print('--->')
#             value=self.func(instance)
#             setattr(instance,self.func.__name__,value) #计算一次就缓存到实例的属性字典中
#             return value
#
# class Room:
#     def __init__(self,name,width,length):
#         self.name=name
#         self.width=width
#         self.length=length
#
#     @Lazyproperty #area=Lazyproperty(area) 相当于'定义了一个类属性,即描述符'
#     def area(self):
#         return self.width * self.length
#
# r1=Room('alex',1,1)
# print(r1.area) #先从自己的属性字典找,没有再去类的中找,然后出发了area的__get__方法
# print(r1.area) #先从自己的属性字典找,找到了,是上次计算的结果,这样就不用每执行一次都去计算


# class Lazyproperty:
#     def __init__(self,func):
#         self.func=func
#     def __get__(self, instance, owner):
#         print('这是我们自己定制的静态属性,r1.area实际是要执行r1.area()')
#         if instance is None:
#             return self
#         else:
#             value=self.func(instance)
#             instance.__dict__[self.func.__name__]=value
#             return value
#         # return self.func(instance) #此时你应该明白,到底是谁在为你做自动传递self的事情
#     def __set__(self, instance, value):
#         print('hahahahahah')
#
# class Room:
#     def __init__(self,name,width,length):
#         self.name=name
#         self.width=width
#         self.length=length
#
#     @Lazyproperty #area=Lazyproperty(area) 相当于定义了一个类属性,即描述符
#     def area(self):
#         return self.width * self.length
#
# print(Room.__dict__)
# r1=Room('alex',1,1)
# print(r1.area)
# print(r1.area)
# print(r1.area)
# print(r1.area) #缓存功能失效,每次都去找描述符了,为何,因为描述符实现了set方法,它由非数据描述符变成了数据描述符,数据描述符比实例属性有更高的优先级,因而所有的属性操作都去找描述符了



# class Foo:
#     def get_AAA(self):
#         print('get')
#
#     def set_AAA(self,value):
#         print('set')
#
#     def delete_AAA(self):
#         print('del')
#     AAA=property(get_AAA, set_AAA, delete_AAA) #内置property三个参数与get,set,delete一一对应
#
# f1=Foo()
# f1.AAA
# f1.AAA='aaa'
# del f1.AAA


# class Str:
#     def __init__(self, name, parameter):
#         self.name = name
#         self.parameter = parameter
#     def __get__(self, instance, owner):
#         if instance == None:
#             return self
#         else:
#             return instance.__dict__[self.name]
#     def __set__(self, instance, value):
#         if not isinstance(value, self.parameter):
#             raise TypeError('Expected %s' % str(self.parameter))
#         instance.__dict__[self.name] = value
#     def __delete__(self, instance):
#         del instance.__dict__[self.name]
#
# def typeassert(**kwargs):
#     def decorate(cls):
#         for name, value in kwargs.items():
#             setattr(cls, name, Str(name, value))
#         return cls
#     return decorate
# @typeassert(name = str, age = int)
# class girl:
#     # name = Str('name', str)
#     # age = Str('age', int)
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def __str__(self):
#         return self.name + str(self.age)
# if __name__ == '__main__':
#     zhangchengxiang = girl('李铁蛋', 18)
#     print(zhangchengxiang)
#     shaoshuai = girl('oldergou', 111)
#     print(shaoshuai)
#     shaoshuai.name = '老二狗'
#     print(shaoshuai)
#     print(girl.__dict__)
#     print(zhangchengxiang.__dict__)


# class Lazyproperty:
#     def __init__(self,func):
#         self.func=func
#     def __get__(self, instance, owner):
#         print('这是我们自己定制的静态属性,r1.area实际是要执行r1.area()')
#         if instance is None:
#             return self
#         return self.func(instance) #此时你应该明白,到底是谁在为你做自动传递self的事情
#
# class Room:
#     def __init__(self,name,width,length):
#         self.name=name
#         self.width=width
#         self.length=length
#
#     @Lazyproperty #area=Lazyproperty(area) 相当于定义了一个类属性,即描述符
#     def area(self):
#         return self.width * self.length
#
# r1=Room('alex',1,1)
# print(r1.area)#调用r1.area会调用area的__get__(),但是在这之前会把area当作参数传入Lazyproperty中，并返回实例化后的对象，
# # 然后再调用Lazyproperty中的__get__()


# g={
#     'x':1,
#     'y':2
# }
# l={}
#
# exec('''
# global x,z
# x=100
# z=200
#
# m=300
# n = 200
# ''',g,l)
#
# print(g) #{'x': 100, 'y': 2,'z':200,......}
# print(l) #{'m': 300}


# class Mymeta(type): #只有继承了type类才能称之为一个元类，否则就是一个普通的自定义类
#     pass
#
# class OldboyTeacher(object,metaclass=Mymeta): # OldboyTeacher=Mymeta('OldboyTeacher',(object),{...})
#     school='oldboy'
#
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#
#     def say(self):
#         print('%s says welcome to the oldboy to learn Python' %self.name)
# print(type(OldboyTeacher))


# class Mymeta(type): #只有继承了type类才能称之为一个元类，否则就是一个普通的自定义类
#     def __init__(self,class_name,class_bases,class_dic):
#         # print(self) #<class '__main__.OldboyTeacher'>
#         # print(class_bases) #(<class 'object'>,)
#         # print(class_dic) #{'__module__': '__main__', '__qualname__': 'OldboyTeacher', 'school': 'oldboy', '__init__': <function OldboyTeacher.__init__ at 0x102b95ae8>, 'say': <function OldboyTeacher.say at 0x10621c6a8>}
#         super(Mymeta, self).__init__(class_name, class_bases, class_dic)  # 重用父类的功能
#
#         if class_name.islower():
#             raise TypeError('类名%s请修改为驼峰体' %class_name)
#
#         if '__doc__' not in class_dic or len(class_dic['__doc__'].strip(' \n')) == 0:
#             raise TypeError('类中必须有文档注释，并且文档注释不能为空')
#     def __call__(self, *args, **kwargs):
#         print('OldBoy')
#         print(args)
#         print(kwargs)
#
# class OldboyTeacher(object,metaclass=Mymeta): # OldboyTeacher=Mymeta('OldboyTeacher',(object),{...})
#     """
#     类OldboyTeacher的文档注释
#     """
#     school='oldboy'
#
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#
#     def say(self):
#         print('%s says welcome to the oldboy to learn Python' %self.name)
#     # def __call__(self, *args, **kwargs):
#     #     print('oooooooo')
#     #     print(args)
#     #     print(kwargs)
# egon = OldboyTeacher('egon',77)
# # egon(123,2,4,A = egon)
# OldboyTeacher('a',A = egon)


# 元类中定义__call__()函数，则实例化的对象不能使用__init__()构造函数

# class Mymeta(type): #只有继承了type类才能称之为一个元类，否则就是一个普通的自定义类
#     def __call__(self, *args, **kwargs):
#         print(self) #<class '__main__.OldboyTeacher'>
#         print(args) #('egon', 18)
#         print(kwargs) #{}
#         obj = self.__new__(self)
#         self.__init__(obj, *args, **kwargs)
#         return obj
#
# class OldboyTeacher(object,metaclass=Mymeta):
#     school='oldboy'
#
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#
#     def say(self):
#         print('%s says welcome to the oldboy to learn Python' %self.name)

# 调用OldboyTeacher就是在调用OldboyTeacher类中的__call__方法
# 然后将OldboyTeacher传给self,溢出的位置参数传给*，溢出的关键字参数传给**
# 调用OldboyTeacher的返回值就是调用__call__的返回值
# t1=OldboyTeacher('egon',18)
# print(t1) #123


# import time
# l = 70
# for i in range(l + 1):
#     time.sleep(0.6)
#     print('\r%s>%s %.2f%%' %('=' * i,' '*(l-i), i/float(l)*100),end='')
#


# !/usr/bin/env python
# -*- coding:utf-8 -*-

# from PIL import Image
# import argparse
#
# # 命令行输入参数处理
# parser = argparse.ArgumentParser()
#
# parser.add_argument('file')  # 输入文件
# parser.add_argument('-o', '--output')  # 输出文件
# parser.add_argument('--width', type=int, default=50)  # 输出字符画宽
# parser.add_argument('--height', type=int, default=50)  # 输出字符画高
#
# # 获取参数
# args = parser.parse_args()
#
# IMG = args.file
# WIDTH = args.width
# HEIGHT = args.height
# OUTPUT = args.output
#
# # 字符画使用的字符集
# ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
#
#
# def get_char(r, g, b, alpha=256):
#     """将256灰度映射到70个字符上"""
#
#     if alpha == 0:
#         return ' '
#
#     length = len(ascii_char)
#     # 计算灰度的公式
#     gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
#     unit = (256.0 + 1) / length
#     index = int(gray / unit)
#     return ascii_char[index]
#
#
# if __name__ == '__main__':
#
#     im = Image.open(IMG)
#     im = im.resize((WIDTH, HEIGHT), Image.NEAREST)
#
#     txt = ""
#
#     # 获取每个像素点对应的字符
#     for i in range(HEIGHT):
#         for j in range(WIDTH):
#             txt += get_char(*im.getpixel((j, i)))
#         txt += '\n'
#
#     print(txt)
#
#     # 字符画输出到文件
#     if OUTPUT:
#         with open(OUTPUT, 'w') as f:
#             f.write(txt)
#     else:
#         with open("output.txt", 'w') as f:
#             f.write(txt)



# import Email
# from PIL import Image

# ascii_char  =list("/\|()1{}$@B%8&WM#ZO0QLCJUYX*hkbdpqwmoahkbdpqwmzcvunxrjft[]?-_+~<>i!lI;:,\"^`'. ")
# imgname = r"C:\Users\WPN\Desktop\A.jpg"
# output =r"C:\Users\WPN\Desktop\a.txt"
# width =60
# height=35
#
# def get_char(r,g,b,alpha= 256):
#     length = len(ascii_char)
#     gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
#     unitcount  = (256.0+1)/length
#     return  ascii_char[int(gray/unitcount)]
#
# img  = Image.open(imgname)
# img  = img.resize((width,height),Image.NEAREST)
#
# txt = ""
#
# for i in range(height):
#     for j in range(width):
#       txt += get_char(*img.getpixel((j,i)))
#     txt += '\n'
# txt = "老母鸡"
# # with open(output,'w') as f:
# #     f.write(txt)
# # print(txt)
# for i in range(10):
#     Email.set_email_text(txt)
#     Email.run()


# import time
# print(time.strftime('%Y-%m-%d %X'))

# import logging
# logger1 = logging.getLogger('日志')
# fh1 = logging.FileHandler('a.log', encoding='utf-8')
# fmt = logging.Formatter(fmt = '%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s', datefmt='%Y-%m-%d %X %p')
# logger1.setLevel(10)
# fh1.setLevel(10)
# logger1.addHandler(fh1)
# fh1.setFormatter(fmt)
# logger1.info('hahahha')

# import hashlib
# m = hashlib.md5('老母鸡'.encode('utf-8'))
# print(m.hexdigest())

# import re
#
# print(re.findall('^d*', 'ldazxcadaz'))
# print(re.findall('www\.[a-z]*', 'www.baidu'))
#
#
# import re
# t = re.compile('\([^()]*\)')
# s = input('>>')
# def f(s):
#     t_res = t.search(s)
#     if t_res:
#         res = str(eval(t_res.group()))
#         s = t.sub(res, s)
#         return f(s)
#     else:
#         return eval(s)
# print(f(s))
#
#
# def decorator(parameter):#有参装饰器
#     def dec1(func):#装饰器1  参数为被装饰的函数func
#         print('dec1', func.__name__)#打印装饰器的名字及被装饰的函数名
#         def wrapper1(*args, **kwargs):  #可以调用decorator传入的参数parameter
#             start_time = time.time()
#             res = func(*args, **kwargs)#可同时传入多个参数，是具体函数而定
#             end_time = time.time()
#             print('dec1', end_time - start_time)
#             return res#对于有返回值的函数要加返回值
#         return wrapper1
#     return dec1
#
#
# while rentsubscript<len(rent):
#     #下级目录
#     subordinatepath = currentpath + '\\' + rent[rentsubscript]
#     #循环遍历开始
#     filename = []
#     for root,dirs,files in os.walk(subordinatepath):
#         for file in files:
#             #去除后4个字符后赋值给文件名列表
#             filename.append(file[:-4])
#         #生成statements
#         n=1
#         statements = filename[0]
#         while n<len(filename):
#             statements +=' 、'+filename[n]
#             n+=1
#         #清洗文件名，去掉文件名中(1)(2)(3)等
#         washed = []
#         for wash in filename:
#             #如果文件名中有（则去掉文件名后三位
#             findb=wash.find(b)
#             if findb!=-1:
#                 washed.append(wash[:-3])
#             else:
#                 washed.append(wash)
#         #获取各类型数量
#         A = 0
#         B = 0
#         #看第十一位是A还是B然后计算
#         for i in washed:
#             if i[10]=='A':
#                 A+=int(i[11:])
#             elif i[10]=='B':
#                 B+=int(i[11:])
#     #判断，如果不是协会，就计算和赋值给数量列表和地址列表
#     if rent[rentsubscript][0:2] !='中国':
#         address.append(rent[rentsubscript][0:2])
#         counts.append(A + B)
#     #字符化输入的快递单号
#     trackingnumber=str(inputnumber)
#     #赋值给快递单列表
#     knumbers.append(trackingnumber)
#     makedocx(rent[rentsubscript],statements,A,B,trackingnumber)
#     inputnumber+=1
#     rentsubscript+=1
#
#
# import re
# res = re.findall('.+', 'hello\nworld', flags=re.DOTALL)
# print(res)
# res = re.findall('.+', 'hello\rworld')
# print(res)
# res = re.findall('^wor+', 'hello\nworld', flags = re.MULTILINE)
# res = re.search('^wor+', 'hello\nworld').group()
# print(res)
# res = re.search('(?P<name>\d+)', 'abcd1234abcd1234')
# print(res.groupdict('name'))
# print(res.group('name'))
# print(re.findall('(?P<name>.+)', '21ewafd334rg333'))
# reobj = re.compile('\d+')
# reobj.findall()
# reobj.search()
# reobj.sub()
# reobj.match()
# reobj.split()
# reobj.finditer()
# reobj.fullmatch()
# reobj.subn()
# res = re.match('\d+', '123asda1')
# print(res, type(res))
# res = re.search('\d+', 'asa123sda')
# print(res, type(res))
# flags=re.MULTILINE
# flags=re.DOTALL
# flags=re.IGNORECASE
# flags=re.VERBOSE
#
# res = re.findall('\d+', 'asasda')
# print(res, type(res))
#
# res = re.split('\d+', 'a1s2a3s4da', maxsplit=3)
# print(res, type(res))
#
# res = re.sub('\d+', 'a', 'a1s2a3s4da')
# print(res, type(res))
#
# res = re.fullmatch('\w+', 'a1s2a3s4da..')
# print(res, type(res))
#
#
# res = re.finditer('\d+','a1s2a3s4da')
# print(res, type(res))



#加密
# import hashlib
# md5 = hashlib.md5()
# md5.update('张胜祥小鸡炖蘑菇'.encode('utf-8'))
# print(md5.hexdigest())

# import hmac
# res = hmac.new('张胜祥'.encode('utf-8'), '小鸡炖蘑菇'.encode('utf-8'), digestmod='md5')
# print(res.hexdigest())
# res1 = hmac.new('张胜祥'.encode('utf-8'), '小鸡炖蘑菇'.encode('utf-8'))
# print(res1.hexdigest())