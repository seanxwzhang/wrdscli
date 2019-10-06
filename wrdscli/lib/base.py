'''
Base Classes for WRDSCLI
'''
import logging

LOG_FORMAT = "%(asctime)s [%(filename)s] [%(levelname)s]: %(message)s"

class Loggable(object):
    def __init__(self, ctx, *args, **kwargs):
        self.logger = logging.getLogger(self.__class__)
        self.logger.setLevel(ctx.obj['DEBUG'])
    
    def ok(self, msg, *args, **kwargs):
        self.logger.info(msg, *args, **kwargs)
    
    def warning(self, msg, *args, **kwargs):
        self.logger.warning(msg, *args, **kwargs)

    def debug(self, msg, *args, **kwargs):
        self.logger.debug(msg, *args, **kwargs)

    def error(self, msg, *args, **kwargs):
        self.logger.error(msg, *args, **kwargs)

    def critical(self, msg, *args, **kwargs):
        self.logger.critical(msg, *args, **kwargs)


class WRDSEntity(object):
    pass