'''
打印省、市、县三级菜单
可返回上一级
可随时退出程序
'''
address = {}
a = address
p = []
def show_keys(address):
    for i in address.keys():
        print(i)

def add(address, key = ''):
    address[key] = {}
    return address


def show_all(address, n):
    if len(address) == 0:
        return
    else:
        for key, value in address.items():
            print('\t'*n+str(key))
            show_all(value, n+1)

while True:
    print('''
    0.返回上一等级
    1.查看全部
    2.添加
    3.进入下一等级
    4.查看当前等级
    quit  退出
    ''')
    c1 = input('请选择:')
    if c1 == '0':
        if len(p) == 0:
            break
        else:
            a = p.pop()
            show_keys(a)
    elif c1 == '1':
        show_all(address, 0)

    elif c1 == '2':
        key = input('请输入名称:')
        a.setdefault(key, {})

        # a = add(a, key)
    elif c1 == '3':
        key = input('请输入查找的名称:')
        if key not in a:
            print('查找的名称不存在！')
        else:
            p.append(a)
            a = a[key]
            show_keys(a)
    elif c1 == '4':
        show_keys(a)
    elif c1 == 'quit':
        break
    else:
        print('输入错误！')