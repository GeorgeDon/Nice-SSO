# coding= utf-8

import logging
import logging.handlers

LOG_FILE = 'sso.log'

handler = logging.handlers.RotatingFileHandler(LOG_FILE, maxBytes=1024 * 1024, backupCount=5)  # 实例化handler
fmt = '%(asctime)s - %(levelname)s - %(filename)s:%(lineno)s - %(name)s - %(message)s'

formatter = logging.Formatter(fmt)  # 实例化formatter
handler.setFormatter(formatter)  # 为handler添加formatter

logger = logging.getLogger('sso')  # 获取名为sso的logger
logger.addHandler(handler)  # 为logger添加handler
logger.setLevel(logging.DEBUG)

# logger.info('first info message')
# logger.debug('first debug message')
# 'DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'