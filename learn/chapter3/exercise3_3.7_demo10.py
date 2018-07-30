import time
def logger(filename = '', channel = 'file'):

    cmd = 'test log db backup 3'
    num = 1
    while cmd != 'quit':
        datetime = time.strftime('%Y-%m-%d %X', time.localtime(time.time()))  # 格式化输出时间
        if channel == 'file' or channel == 'both':
            with open(filename, 'a', encoding='utf-8')as f:
                f.write(str(datetime) + '[%d] %s\n' % (num, cmd))
        if channel == 'both' or channel == 'terminal':
            print(datetime, '[%d] %s' % (num, cmd))
        cmd = yield num#send 函数传入的参数
        num += 1

f = logger('info2', 'both')
f.__next__()
f.send('user alex login success')
f.send('user egon login success')