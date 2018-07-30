age1=5
age=int(input('请输入年龄:'))
for i in range(0,2):
    if age>age1:
        print('大了')
    elif age<age1:
        print('小了')
    else:
        print('恭喜你答对了')
        break
    s=input('是否想继续玩(Y/N)？')
    if(s=='Y' or s=='y'):
        age = int(input('请输入年龄:'))
    else:
        break