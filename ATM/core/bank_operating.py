import time
def save(list):
    '''
    添加信息
    :param list:
    :return:
    '''
    with open('../db/bank_customer_db', 'a', encoding='utf-8') as file:
        file.write('|'.join(list) + '\n')
def delete(id):
    '''
    删除信息
    :param id:
    :return:
    '''
    lines = []
    with open('../db/bank_customer_db', 'r', encoding='utf-8') as file:
        lines = file.readlines()
    for line in lines:
        if line.split('|')[0] == str(id):
            lines.remove(line)
            break
    with open('../db/bank_customer_db', 'w', encoding='utf-8') as file:
        file.writelines(lines)
def update(list):
    '''
    更新信息
    :return:
    '''
    with open('../db/bank_customer_db', 'r', encoding='utf-8') as file:
        lines = file.readlines()
    for i in range(len(lines)):
        if list[1] in lines[i]:
            lines[i] = '|'.join(list)
            break
    with open('../db/bank_customer_db', 'w', encoding='utf-8') as file:
        file.writelines(lines)
def search(number):
    '''
    查找信息
    :param number:
    :return:
    '''
    lines = []
    info_dic = {}
    with open('../db/bank_customer_db', 'r', encoding='utf-8') as file:
        lines = file.readlines()
    for line in lines:
        if line.split('|')[1] == number:
            info_dic[number] = line.split('|')
            break
    return info_dic
def login(number, password, customer_state):
    '''
    登录验证
    :param number:
    :param password:
    :param customer_state:
    :return:
    '''
    login_info = search(number)
    if len(login_info) == 0:
        print('账户不存在!')
        return None
    else:
        now_date = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        if password == login_info[number][2]:
            if now_date > login_info[number][-1]:
                return login_info[number]
            else:
                print('此账户已经被锁定，今日不能再登录！')
                return None
        else:
            if customer_state.get(number) and customer_state[number] >= 1:
                login_info[number][-1] = now_date + '\n'
                update(login_info[number])
            print('密码错误！')
            return None