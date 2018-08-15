import json
mean = \
'''
-------Luffy Bank-----
1. 账户信息
2. 提现
'''
# luffy_dic = {'name': 'luffy', 'banlance': 1000000, 'amount': 0}
# tesla_dic = {'name': 'tesla', 'banlance': 0}
# with open('../account/luffy1.json', 'w', encoding='utf-8') as f:
#     json.dump(luffy_dic, f)
# with open('../account/tesla1.json', 'w', encoding='utf-8') as f:
#     json.dump(tesla_dic, f)
def show_info():
    with open('../account/luffy1.json', 'r', encoding='utf-8') as f:
        info_dic = json.load(f)
    print('余额：', info_dic['banlance'], '额度：', info_dic['amount'])
# def transfer():
#     with open('../account/luffy.json', 'r', encoding='utf-8') as f:
#         luffy_dic = json.load(f)
#     if luffy_dic['banlance'] < 750000 * 1.05:
#         print('余额不足')
#         return
#     with open('../account/tesla.json', 'r', encoding='utf-8') as f:
#         tesla_dic = json.load(f)
#     luffy_dic['banlance'] -= 750000 * 1.05
#     tesla_dic['banlance'] += 750000
#     with open('../account/luffy.json', 'w', encoding='utf-8') as f:
#         json.dump(luffy_dic, f)
#     with open('../account/tesla.json', 'w', encoding='utf-8') as f:
#         json.dump(tesla_dic, f)
#     print('转账成功，手续费 %s ' % (750000 * 0.05))
def withdraw():
    amount = input('输入提现金额：')
    if amount.isdigit():
        amount = int(amount)
    else:
        print('请输入数字')
        return
    with open('../account/luffy1.json', 'r', encoding='utf-8') as f:
        luffy_dic = json.load(f)
    money = luffy_dic['banlance']
    if money < amount:
        print('余额不足')
        return
    luffy_dic['banlance'] -= amount
    with open('../account/luffy1.json', 'w', encoding='utf-8') as f:
        json.dump(luffy_dic, f)
    print('取现成功,金额', amount)
choice = {
    '1': show_info,
    '2': withdraw
}
while True:
    print(mean)
    cmd = input('>>')
    if cmd in choice:
        choice[cmd]()
    else:
        print('输入错误')
