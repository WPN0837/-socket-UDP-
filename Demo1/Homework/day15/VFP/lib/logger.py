import time
from conf.setting import LOG_PATH
def logger(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        if res:
            with open(LOG_PATH, 'a', encoding='utf-8') as log:
                log.write('%s %s 执行了 %s\n' % (time.strftime('%Y-%m-%d %X', time.localtime(time.time())), res[0], res[1]))
    return wrapper