import logging.config
standard_format = '%(asctime)s - acess - %(levelname)s - account [%(name)s] %(message)s'
fh_path = 'log'
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
            'class': 'logging.StreamHandler',  # 保存到文件
            'formatter': 'standard',
        },
    },
    'loggers': {
        '日志': {
            'handlers': ['fh', 'fh2'],
            'level': 'DEBUG',
        },
        '终端': {
            'handlers': ['fh2'],
            'level': 'DEBUG',
        },
    },
}
logging.config.dictConfig(LOGGING_DIC)
log = logging.getLogger('日志')
log.info('too many login attempts')