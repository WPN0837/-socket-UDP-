import json
mean = \
'''
-------Luffy Bank-----
1. 账户信息
2. 转账
'''
# luffy_dic = {'name': 'luffy', 'banlance': 1000000}
# tesla_dic = {'name': 'tesla', 'banlance': 0}
# with open('../account/luffy.json', 'w', encoding='utf-8') as f:
#     json.dump(luffy_dic, f)
# with open('../account/tesla.json', 'w', encoding='utf-8') as f:
#     json.dump(tesla_dic, f)
def show_info():
    with open('../account/luffy.json', 'r', encoding='utf-8') as f:
        info_dic = json.load(f)
    print('余额', info_dic['banlance'])
def transfer():
    with open('../account/luffy.json', 'r', encoding='utf-8') as f:
        luffy_dic = json.load(f)
    if luffy_dic['banlance'] < 750000 * 1.05:
        print('余额不足')
        return
    with open('../account/tesla.json', 'r', encoding='utf-8') as f:
        tesla_dic = json.load(f)
    luffy_dic['banlance'] -= 750000 * 1.05
    tesla_dic['banlance'] += 750000
    with open('../account/luffy.json', 'w', encoding='utf-8') as f:
        json.dump(luffy_dic, f)
    with open('../account/tesla.json', 'w', encoding='utf-8') as f:
        json.dump(tesla_dic, f)
    print('转账成功，手续费 %s ' % (750000 * 0.05))
choice = {
    '1': show_info,
    '2': transfer
}
while True:
    print(mean)
    cmd = input('>>')
    if cmd in choice:
        choice[cmd]()
    else:
        print('输入错误')
