menu = {
    '北京': {
        '海淀': {
            '五道口': {
                'soho': {},
                '网易': {},
                'google': {}
            },
            '中关村': {
                '爱奇艺': {},
                '汽车之家': {},
                'youku': {}
            },
            '上地': {
                '百度': {}
            }
        },
        '昌平': {
            '沙河': {
                '老男孩': {},
                '北航': {}
            },
            '天通苑': {},
            '回龙观': {}
        },
        '朝阳': {},
        '东城': {}
    },
    '上海': {
        '闵行': {
            '人民广场': {
                '炸鸡店': {}
            }
        },
        '闸北': {
            '火车站': {
                '携程': {}
            }
        },
        '浦东':{}
    },
    '山东': {}
}
a = menu
p = []
def show_keys(address):#显示当前一级
    if len(address) == 0:
        print('空')
        return
    for i in address.keys():
        print(i)


def show_all(address, n):#显示全部
    if len(address) == 0:
        return
    else:
        for key, value in address.items():
            print('\t'*n+str(key))
            show_all(value, n+1)
show_keys(a)
while True:
    print(
'''
0.直接退出
1.进入下一级
2.返回上一级
3.全部
''')
    c = input('请选择功能:')
    if c == '0':
        break
    elif c == '1':
        key = input('输入地名:')
        if key in a:
            p.append(a)
            a = a[key]
            show_keys(a)
        else:
            print('输入错误！')
            show_keys(a)
    elif c == '2':
        if len(p) == 0:
            print('已经是最上级！')
            show_keys(a)
        else:
            a = p.pop()
            show_keys(a)
    elif c == '3':
        show_all(menu, 0)
    else:
        print('输入错误！')