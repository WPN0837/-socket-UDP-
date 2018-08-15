'''
根据3得到的列表,将每个人的信息中的名字映射成首字母大写的形式
'''
info_list = []
name_list = ['name', 'sex', 'age', 'salary']
with open('test.txt', 'r', encoding='utf-8') as info:
    for line in info:
        info_list.append(dict(zip(name_list, line.strip('\n').split(' '))))
def func(dic):
    dic['name'] = dic['name'].capitalize()
    return dic
res = list(map(func, info_list))
print(res)