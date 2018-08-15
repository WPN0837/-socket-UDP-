'''
根据3得到的列表,取出薪资最高的人的信息
'''
info_list = []
name_list = ['name', 'sex', 'age', 'salary']
with open('test.txt', 'r', encoding='utf-8') as info:
    for line in info:
        info_list.append(dict(zip(name_list, line.strip('\n').split(' '))))
res = max(info_list, key=lambda i: int(i['salary']))
print(res)