'''
Base Classes for WRDSCLI
'''
import logging
from abc import ABC, abstractmethod
from wrdscli.common import engine, LOG_FORMAT, get_logger
from sqlalchemy import text

logger = get_logger('base')

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


class abstractstatic(staticmethod):
    __slots__ = ()
    def __init__(self, function):
        super(abstractstatic, self).__init__(function)
        function.__isabstractmethod__ = True
    __isabstractmethod__ = True

class WRDSEntity(ABC, Loggable):
    engine = engine

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.schema = self.get_schema()
        self.table = self.get_table()

    def get_schema(self):  # override this if need be
        return self.schema  # pylint: disable=no-member

    def get_table(self):  # override this if need be
        return self.table  # pylint: disable=no-member

    @classmethod
    def execute(cls, sql):
        connection = cls.engine.connect()
        logger.info('Executing sql: {}'.format(sql))
        res = connection.execute(text(sql))
        connection.close()
        return res

    @classmethod
    def from_attr(cls, attr, val, limit=None):
        sql = f'SELECT * from {cls.schema}.{cls.table} WHERE {attr} LIKE \'%{val}%\''  # pylint: disable=no-member
        sql += ';' if not limit else f' LIMIT {limit};'
        return cls.execute(sql)

