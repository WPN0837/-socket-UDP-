'''
猜年龄游戏升级版
	要求：
	    允许用户最多尝试3次
	    每尝试3次后，如果还没猜对，就问用户是否还想继续玩，如果回答Y或y, 就继续让其猜3次，以此往复，如果回答N或n，就退出程序
	    如何猜对了，就直接退出
'''
import random
num = random.randint(1, 100)
print('**********猜数字小游戏**********')
count = 0
while count < 3:
    i = int(input('请输入你猜的数字：'))
    if i < num:
        print('你猜的数字小了。。。。')
    elif i > num:
        print('你猜的数字大了。。。。')
    else:
        print('恭喜你猜对了！！！！！')
        break
    count += 1
    if count == 3:
        while True:
            c = input('你还想玩吗？(Y/N)')
            if c == 'Y' or c == 'y':
                count = 0
                break
            elif c == 'N' or c == 'n':
                break
            else:
                print('请输入（Y/y或者N/n）')
print('数字是%d' % (num))
print('**********GAME OVER**********')