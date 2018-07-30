'''猜年龄游戏
	要求：
	允许用户最多尝试3次，3次都没猜对的话，就直接退出，如果猜对了，打印恭喜信息并退出
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
print('数字是%d' % (num))
print('**********GAME OVER**********')