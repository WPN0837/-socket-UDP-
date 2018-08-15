import configparser
from conf import setting
def get_id(obj_name):
    '''
    返回指定类型的id
    :param obj_name:
    :return:
    '''
    conf = configparser.ConfigParser()
    conf.read(setting.CONFIG)
    id = int(conf[obj_name]['id'])
    conf[obj_name]['id'] = str(id + 1)
    conf.write(open(setting.CONFIG, 'w'))
    return id + 1