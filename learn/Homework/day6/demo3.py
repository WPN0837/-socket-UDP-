'''
使用三种不同的语法 创建内容包含name和age的字典
'''
dic1 = {'name': None, 'age': None}
dic2 = dict((['name', None], ['age', None]))
dic3 = dict(name = None, age = None)
print(dic1)
print(dic2)
print(dic3)