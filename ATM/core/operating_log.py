import time
def logger(filename = '../log/ATM.log'):
    cmd = ''
    while True:
        datetime = time.strftime('%Y-%m-%d %X', time.localtime(time.time()))  # 格式化输出时间
        if cmd != '':
            with open(filename, 'a', encoding='utf-8')as f:
                f.write(str(datetime) + ' %s\n' % cmd)
        cmd = yield#send 函数传入的参数
