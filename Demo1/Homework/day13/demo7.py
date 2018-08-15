'''
根据3得到的列表,过滤掉名字以a开头的人的信息
'''
info_list = []
name_list = ['name', 'sex', 'age', 'salary']
with open('test.txt', 'r', encoding='utf-8') as info:
    for line in info:
        info_list.append(dict(zip(name_list, line.strip('\n').split(' '))))
# res = filter(lambda i: False if i['name'].startswith('a') else True, info_list)
res = filter(lambda i: not i['name'].startswith('a'), info_list)
for i in res:
    print(i)