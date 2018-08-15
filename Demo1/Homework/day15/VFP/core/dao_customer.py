import json

def read():
    with open('../db/customer.json', 'r') as info:
        return json.load(info)

def write(customer_dic):
    with open('../db/customer.json', 'w') as info:
        json.dump(customer_dic, info)

def save(dic):
    customer_dic = read()
    customer_dic[dic['name']] = dic
    write(customer_dic)

def search(name):
    customer_dic = read()
    if name in customer_dic:
        return customer_dic[name]
    return None

def update(dic):
    customer_dic = read()
    customer_dic[dic['name']] = dic
    write(customer_dic)