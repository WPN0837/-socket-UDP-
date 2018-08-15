CONF_PATH = r'conf/atm.config'
DB_PATH = r'data/atm_user_db'
ATM_LOG_PATH = r'log/operating.log'
CONSUM_LOG_PATH = r'log/consumption.log'


standard_format = '%(asctime)s - task:%(name)s - %(levelname)s : [%(message)s]'

fh_path = ATM_LOG_PATH
fh2_path = CONSUM_LOG_PATH

# log配置字典
LOGGING_DIC = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': standard_format
        },
    },
    'filters': {},
    'handlers': {
        #打印到operating.log文件的日志
        'fh': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',  # 保存到文件
            'formatter': 'standard',
            'filename': fh_path,  # 日志文件的路径
            'encoding': 'utf-8',  # 日志文件的编码，再也不用担心中文log乱码了
        },
        'fh2': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',  # 保存到文件
            'formatter': 'standard',
            'filename': fh2_path,  # 日志文件的路径
            'encoding': 'utf-8',  # 日志文件的编码，再也不用担心中文log乱码了
        },
    },
    'loggers': {
        'ATM操作': {
            'handlers': ['fh'],
            'level': 'DEBUG',
        },
        '消费流水': {
            'handlers': ['fh2'],
            'level': 'DEBUG',
        },
    },
}
