# {'id':id, 'account':account, 'password':password, 'name': name ,'date':date, 'balance': balance,
# 'overdraft': overdraft, 'freeze': freeze}
import pickle
from conf import settings

def read():
    with open(settings.DB_PATH, 'rb') as file:
        return pickle.load(file)

def write(info_dic):
    with open(settings.DB_PATH, 'wb') as file:
        pickle.dump(info_dic, file)

def find_info_by_account(account):
    info_dic = read()
    for v in info_dic.values():
        if account == v['account']:
            return v
    return None

def find_info_by_id(id):
    info_dic = read()
    if id in info_dic:
        return info_dic[id]
    return None

def save(user_dic):
    info_dic = read()
    info_dic[user_dic['id']] = user_dic
    write(info_dic)

def update(user_dic):
    info_dic = read()
    if user_dic['id'] in info_dic:
        info_dic[user_dic['id']] = user_dic
        write(info_dic)
        return True
    return False
