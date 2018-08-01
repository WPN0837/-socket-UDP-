'''
编写用户验证函数，实现功能
		1、用户输入账号，密码，然后与文件中存放的账号密码验证
		2、同一账号输错密码三次则锁定

		3、这一项为选做功能：锁定的账号，在五分钟内无法再次登录
			提示：一旦用户锁定，则将用户名与当前时间写入文件,例如: egon:1522134383.29839
				实现方式如下：

				import time

				current_time=time.time()
				current_time=str(current_time) #当前的时间是浮点数，要存放于文件，需要转成字符串
				lock_user='%s:%s\n' %('egon',current_time)

				然后打开文件
				f.write(lock_user)

				以后再次执行用户验证功能，先判断用户输入的用户名是否是锁定的用户，如果是，再用当前时间time.time()减去锁定的用户名后
				的时间，如果得出的结果小于300秒，则直接终止函数，无法认证，否则就从文件中清除锁定的用户信息，并允许用户进行认证
'''
import time
# username|password|time
userstate = {}
def login():
    while True:
        now_time = time.time()
        info_number = -1
        username = input('用户名：')
        password = input('密码：')
        with open('login_info', 'r', encoding='utf-8') as info:
            lines = info.readlines()
            for i in range(len(lines)):
                if lines[i].split('|')[0] == username:
                    info_number = i
        if info_number != -1:
            if lines[info_number].split('|')[1] == password:
                if lines[info_number].split('|')[2].strip('\n') == '' or \
                        now_time - float(lines[info_number].split('|')[2].strip('\n')) > 300:
                    print('登陆成功！')
                    return True
                else:
                    print('账号被锁定！')
            else:
                print('密码不正确！')
                if username in userstate:
                    userstate[username] += 1
                else:
                    userstate[username] = 0
                if userstate[username] >= 2:
                    line_list = lines[info_number].split('|')
                    line_list[2] = str(now_time) + '\n'
                    lines[info_number] = '|'.join(line_list)
                    with open('login_info', 'w', encoding='utf-8') as info:
                        info.writelines(lines)
login()