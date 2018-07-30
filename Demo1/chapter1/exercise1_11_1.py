age = int(input('输入年龄:'))
age1 = 5
for i in range(0, 2):
    if age > age1:
        print('大了')
        age = int(input('输入年龄:'))
    elif age < age1:
        print('小了')
        age = int(input('输入年龄:'))
    else:
        print('恭喜你猜对了')
        break