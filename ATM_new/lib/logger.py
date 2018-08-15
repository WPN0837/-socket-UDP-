import logging.config
from conf import settings
logging.config.dictConfig(settings.LOGGING_DIC)

def logger(Type, event):
    log = logging.getLogger(Type)
    log.info(event)