'''
在使用字典存储你和你左右同学的信息然后将它们存储在一个列表中最后循环输出所有信息
'''
l = [{'name': '邵帅', 'sex': '男'},
{'name': '张胜祥', 'sex': '男'},
{'name': '张胜祥', 'sex': '男'}]
for i in l:
    for key, value in i.items():
        print(key, value)
