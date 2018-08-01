'''
编写用户注册函数，实现功能
		1、在函数内接收用户输入的用户名、密码、余额
			要求用户输入的用户名必须为字符串，并且保证用户输入的用户名不与其他用户重复
			要求用户输入两次密码，确认输入一致
			要求用户输入的余额必须为数字
		2、要求注册的用户信息全部存放于文件中
'''

#Demo1/Homework/day10/customer_info
def resiger():
    username = input('用户名：')
    password = input('密码：')
    password1 = input('重复密码：')
    balance = input('余额：')
    if not username.isalnum():
        print('用户名必须为字母和数字！')
        return False
    with open('customer_info', 'r', encoding='utf-8')as info:
        lines = info.readlines()
        for line in lines:
            if username == line.split('|')[0]:
                print('用户名已存在！')
                return False
    if password !=password1:
        print('两次密码不一样！')
        return False
    if not balance.isnumeric():
        print('密码必须全为数字')
        return False
    with open('customer_info', 'a', encoding='utf-8')as info:
        info.write(f'{username}|{password}|{balance}\n')
    return True
resiger()