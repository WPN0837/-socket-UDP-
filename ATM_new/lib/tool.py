import pickle
import configparser
import hashlib
from conf import settings
def get_id_and_account():
    conf = configparser.ConfigParser()
    conf.read(settings.CONF_PATH)
    id = int(conf['ATM']['id'])
    account = int(conf['ATM']['account'])
    conf['ATM']['id'] = str(id + 1)
    conf['ATM']['account'] = str(account + 1)
    conf.write(open(settings.CONF_PATH, 'w', encoding='utf-8'))
    return str(id + 1), str(account + 1)

def md5(Str):
    md5 = hashlib.md5()
    md5.update(Str.encode('utf-8'))
    return md5.hexdigest()

def init():
    conf = '[ATM]\nid = 0\naccount = 6216610800000000000\n'
    with open(settings.CONF_PATH, 'w', encoding='utf-8') as file:
        file.write(conf)
    dic = {}
    with open(settings.DB_PATH, 'wb') as file:
        pickle.dump(dic, file)
    with open(settings.ATM_LOG_PATH, 'w', encoding='utf-8') as file:
        file.write()
    with open(settings.CONSUM_LOG_PATH, 'w', encoding='utf-8') as file:
        file.write()