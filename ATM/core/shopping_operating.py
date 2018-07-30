# id|name|password|cart|buyed|state|bank
'''
对用户信息的增删改查
'''
def save(info = {}):#增
    '''
    添加
    :param info: 字典类型的信息
    :return:
    '''
    info_list = [info.get('id'), info.get('name'), info.get('password'), \
                 info.get('cart'), info.get('buyed'), info.get('state'), info.get('bank')]
    info_str = '|'.join(info_list)
    with open('../db/shopping_customer_db', 'a', encoding='utf-8') as info_file:
        info_file.write(info_str+'\n')
def delete(_id):#删
    '''
    删除
    :param _id:
    :return: True 删除成功 False 不存在要删除的信息，删除失败
    '''
    with open('../db/shopping_customer_db', 'r', encoding='utf-8') as info_file:
        lines = info_file.readlines()
    falg = False
    for line in lines:
        if _id == line.split('|')[0]:
            lines.remove(line)
            falg = True
            break
    if falg:
        with open('../db/shopping_customer_db', 'w', encoding='utf-8') as info_file:
            info_file.writelines(lines)
    return falg
def update(info = {}):#改
    '''
    更新信息
    :param info:
    :return: True 信息更新成功  False 更新的信息不存在
    '''
    info_list = [info.get('id'), info.get('name'), info.get('password'), \
                 info.get('cart'), info.get('buyed'), info.get('state'), info.get('bank')]
    info_str = '|'.join(info_list)
    falg = False
    with open('../db/shopping_customer_db', 'r', encoding='utf-8') as info_file:
        lines = info_file.readlines()
    for i in range(len(lines)):
        if info.get('id') == lines[i].split('|')[0]:
            lines[i] = info_str
            falg = True
            break
    if falg:
        with open('../db/shopping_customer_db', 'w', encoding='utf-8') as info_file:
            info_file.writelines(lines)
    return falg
def search(name = ''):#查
    '''
    根据用户名查询用户信息
    匹配不到用户名或者没有参数返回全部用户的信息
    :param name:
    :return: [{}]
    '''
    list = ['id', 'name', 'password', 'cart', 'buyed', 'state', 'bank']
    info_list = []
    with open('../db/shopping_customer_db', 'r', encoding='utf-8') as info_file:
        lines = info_file.readlines()
    for line in lines:
        if name == line.split('|')[1]:
            return [dict(zip(list, line.split('|')))]
        info_list.append(dict(zip(list, line.split('|'))))
    return info_list