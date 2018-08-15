'''
控制台模拟发送验证码
	提示：
	1）验证码为6位纯数字
	2）两次获取的间隔为60s
	3）倒计时为一秒减一次
	4）流程中的?是实际数字，#为临时填充字符
	流程：
	1）控制台提示用户是否发送验证码[1:是 0:否]
	2）取消发送验证码则提示"取消发送"并直接退出程序
	3）发送成功后，提示用户"验证码发送成功"，但3s后才可以获取到验证码
	4）一旦发送成功后，控制台会刷新打印倒计时多少秒后可以重新发送验证码
	5）未接收到验证码的前3s，控制台刷新打印的内容是：验证码:######，?s后可以重新发送
	6）验证码获取后，5中的打印内容会替换为：验证码:??????，?s后可以重新发送
	7）只有等"?s后可以重新发送"的?从60变到0，才可以重新执行整个过程
'''
import random,time
def make_Verification_code():
    l = [str(random.randint(0, 9)) for i in range(6)]
    return ''.join(l)
def countdown(s):# 倒计时
    for i in range(s+1):
        print('\r%sS'% i, end='')
        time.sleep(1)
    print()
if __name__ == '__main__':
    while True:
        cmd = input('是否发送验证码[1:是 0:否]')
        if cmd == '0':
            print('取消发送')
            break
        elif cmd == '1':
            print('验证码发送成功')
            s = '??????'
            for i in range(61)[::-1]:
                if i == 57:
                    s = make_Verification_code()
                print('\r验证码: %s , %s 秒后可以重新发送' % (s, i), end='')
                time.sleep(1)
            print()
        else:
            print('输入错误！')
