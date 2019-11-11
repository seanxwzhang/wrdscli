#!/usr/bin/env python

import logging
import traceback
import sys
import errno
from configparser import ConfigParser
from importlib import reload
from os import path, walk, makedirs, getenv
from sqlalchemy import create_engine

LOG_FORMAT = "%(asctime)s [%(filename)s] [%(levelname)s]: %(message)s"

def get_logger(name, level=getenv('LOG_LEVEL', 'INFO')):
    logging.basicConfig(format=LOG_FORMAT)
    logger = logging.getLogger(name)
    logger.setLevel(level)
    return logger

def load_config():
    '''
    Load wrdscli config
    '''
    script_path = path.abspath(__file__)
    config_path = path.realpath(path.join(script_path, '../config/default.ini'))
    config = ConfigParser()
    config.read(config_path)
    return config

def get_wrds_engine():
    config = load_config()
    section_name = 'db'
    user = config[section_name]['PGUSER']
    pw = config[section_name]['PGPASS']
    host = config[section_name]['PGHOST']
    db = config[section_name]['PGDATABASE']
    return create_engine(f'postgresql://{user}:{pw}@{host}/{db}', pool_size=20, max_overflow=10, connect_args={'connect_timeout': 60})

def open_wp(file_path):
    directory = path.dirname(file_path)
    if not path.exists(directory):
        try:
            makedirs(directory)
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise
    return open(file_path, 'w+')

class SafeRun(object):

    def __init__(self, logger):
        self.logger = logger

    def __call__(self, func, *args, **kwargs):
        def func_wrapper(*args, **kwargs):
            try:
                func(*args, **kwargs)
                return 0
            except (KeyboardInterrupt, SystemExit):
                self.logger.error('Exiting')
                raise
            except:
                self.logger.error(f"Exception happened during safe run")
                self.logger.error(traceback.format_exception(*(sys.exc_info())))
                return 1
        return func_wrapper

class AsyncSafeRun(object):

    def __init__(self, logger):
        self.logger = logger

    def __call__(self, func, *args, **kwargs):
        async def func_wrapper(*args, **kwargs):
            try:
                await func(*args, **kwargs)
                return 0
            except (KeyboardInterrupt, SystemExit):
                self.logger.error('Exiting')
                raise
            except:
                self.logger.error(f"Exception happened during safe run")
                self.logger.error(traceback.format_exception(*(sys.exc_info())))
                return 1
        return func_wrapper

engine = get_wrds_engine()