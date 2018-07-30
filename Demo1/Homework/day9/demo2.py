'''
1、写函数，，用户传入修改的文件名，与要修改的内容，执行函数，完成批了修改操作
2、写函数，计算传入字符串中【数字】、【字母】、【空格] 以及 【其他】的个数

3、写函数，判断用户传入的对象（字符串、列表、元组）长度是否大于5。

4、写函数，检查传入列表的长度，如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。

5、写函数，检查获取传入列表或元组对象的所有奇数位索引对应的元素，并将其作为新列表返回给调用者。

6、写函数，检查字典的每一个value的长度,如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。
dic = {"k1": "v1v1", "k2": [11,22,33,44]}
PS:字典中的value只能是字符串或列表
'''
import os
def change(filename, old_str, new_str):
    with open(filename, 'r', encoding='utf-8')as old, open('newfile', 'w', encoding='utf-8')as new:
        for line in old:
            new.write(line.replace(old_str, new_str))
    os.remove(filename)
    os.rename('newfile', filename)
def count(s = ''):
    dic = {'数字': 0, '字母': 0, '空格': 0, '其他': 0}
    for i in s:
        if i.isnumeric():
            dic['数字'] += 1
        elif i.isalpha():
            dic['字母'] += 1
        elif i == ' ':
            dic['空格'] += 1
        else:
            dic['其他'] += 1
    print(dic)
def judge_len(m):
    if len(m) > 5:
        return True
    return False
def len2(m):
    if len(m) > 2:
        return m[0:2]
    return m
def method(m):
    return m[1::2]
def method1(dic):
    for i, value in dic.items():
        if len(value) > 2:
            dic[i] = value[0:2]
    return dic
if __name__ == '__main__':
    # change('a', '函数', '方法')
    print(judge_len({"name": "武则天", "number": "sh02", "math": '40', "english": '97', "chinese": '67'}))
    count("with open(filename, 'r', encoding='utf-8')as old, open('newfile', 'w', encoding='utf-8')as new:")
    print(method1({"name": "武则天", "number": "sh02", "math": '40', "english": '97', "chinese": '67'}))
    pass