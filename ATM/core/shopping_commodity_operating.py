# id|name|price
'''
对商品的增删改查
'''
def save(info = {}):#增
    info_list = [info.get('id'), info.get('name'), info.get('price')]
    info_str = '|'.join(info_list)
    with open('../db/shopping_commodity_db', 'a', encoding='utf-8') as info_file:
        info_file.write(info_str+'\n')
def delete(_id):#删
    with open('../db/shopping_commodity_db', 'r', encoding='utf-8') as info_file:
        lines = info_file.readlines()
    falg = False
    for line in lines:
        if _id == line.split('|')[0]:
            lines.remove(line)
            falg = True
            break
    if falg:
        with open('../db/shopping_commodity_db', 'w', encoding='utf-8') as info_file:
            info_file.writelines(lines)
    return falg
def update(info = {}):#改
    info_list = [info.get('id'), info.get('name'), info.get('price')]
    info_str = '|'.join(info_list)
    falg = False
    with open('../db/shopping_commodity_db', 'r', encoding='utf-8') as info_file:
        lines = info_file.readlines()
    for i in range(len(lines)):
        if info.get('id') == lines[i].split('|')[0]:
            lines[i] = info_str
            falg = True
            break
    if falg:
        with open('../db/shopping_commodity_db', 'w', encoding='utf-8') as info_file:
            info_file.writelines(lines)
    return falg
def search(name = ''):#查
    list = ['id', 'name', 'price']
    info_dic = {}
    with open('../db/shopping_commodity_db', 'r', encoding='utf-8') as info_file:
        lines = info_file.readlines()
    for line in lines:
        if name == line.split('|')[1]:
            return {line.split('|')[0]: dict(zip(list, line.split('|')))}
        info_dic[line.split('|')[0]] = dict(zip(list, line.split('|')))
    return info_dic

def search_buyed(id_list = []):#根据id查
    info_list = []
    list = ['id', 'name', 'price']
    with open('../db/shopping_commodity_db', 'r', encoding='utf-8') as info_file:
        lines = info_file.readlines()
    for _id in id_list:
        for line in lines:
            if _id == line.split('|')[0]:
                info_list.append(dict(zip(list, line.split('|'))))
    return info_list