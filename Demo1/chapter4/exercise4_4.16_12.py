import time
import json
# dic = {'expire_date': '2021-01-01', 'id': 1234, 'status': 0, 'pay_day': 22, 'password': 'abc'}
# with open('1234.json', 'w', encoding='utf-8') as f:
#     json.dump(dic, f)
# date = time.strftime('%Y-%m-%d', time.localtime())
user_state = {}
while True:
    name = input('>>')
    password = input('>>')
    date = time.strftime('%Y-%m-%d', time.localtime())
    with open('1234.json', 'r', encoding='utf-8') as f:
        info_dic = json.load(f)
    if info_dic:
        if name == str(info_dic['id']):
            if password == info_dic['password']:
                if info_dic['status'] == 1:
                    print('账户被锁定')
                elif date <= info_dic['expire_date']:
                    print('登录成功')
                    break
                else:
                    print('账户已过期')
            else:
                if name in user_state:
                    user_state[name] += 1
                else:
                    user_state[name] = 0
                if user_state[name] >= 2:
                    info_dic['status'] = 1
                    with open('1234.json', 'w', encoding='utf-8') as f:
                        json.dump(info_dic, f)
        else:
            print('用户不存在')