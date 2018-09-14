import os
from conf import settings
import time


def save(account, msg):
    path = os.path.join(settings.DB_DIR, account)
    date = time.strftime('%Y-%m-%d %X', time.localtime())
    with open(path, 'a', encoding='utf-8') as file:
        file.write('%s | %s: %s\n' % (date, account, msg))
