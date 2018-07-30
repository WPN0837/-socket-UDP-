'''
对于字典 有多种方式可以删除一个键值对
		dic.pop("key")
		dic.remove("key")
		两种方法有什么不同
'''

# pop删除的元素必须存在，否则报错，返回删除的value
# del pop删除的元素必须存在，否则报错
# popitem()随机删除一个键值对
# update(dict)更新字典,重复的被覆盖   有则改之 无则加冕

dic = {1: 2, 2: 3}
dic.pop(1)
# print(dic)
print(dic)
dic.popitem()
print(dic)