address = {}
a = address
p = [a]
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
    0.返回
    1.查看全部
    2.添加
    3.查找
    4.查看当前
    ''')
    c1 = input('请选择:')
    if c1 == '0':
        if len(p) == 1:
            break
        else:
            a = p.pop()
            show_keys(a)
    elif c1 == '1':
        show_all(address, 0)

    elif c1 == '2':
        key = input('请输入名称:')
        a = add(a, key)
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
    else:
        print('输入错误！')