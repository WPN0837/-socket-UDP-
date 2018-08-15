import configparser
conf = configparser.ConfigParser()
conf.read('my.cnf')
conf['mysqld']['default-time-zone'] = '+00:00'
conf.remove_option('mysqld', 'dd')
conf['DEFAULT']['character-set-server'] = 'utf8'
conf.write(open('my.cnf', 'w', encoding='utf-8'))
