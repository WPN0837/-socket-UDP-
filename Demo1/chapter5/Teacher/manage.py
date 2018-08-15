import os, sys
path = os.path.dirname(__file__)
sys.path.append(path)
import configparser
if __name__ == '__main__':
    pass
    # config = configparser.ConfigParser()
    # config.read('config/config')
    # i = config['TEACHER']['ID']
    # print(i, type(i))
    # print(config.sections())
    # config['TEACHER']['ID'] = '2'
    # # config.set('TEACHER', 'name', 'alex')
    # config.write(open('config/config','w'))