#!/usr/bin/env python3

import click
import logging
import sys
import traceback
import time
import asyncio
import concurrent.futures
import attr
from os import getenv
from importlib import import_module, reload
from wrdscli.common import get_wrds_engine, AsyncSafeRun, LOG_FORMAT
from sqlalchemy import MetaData
from sqlalchemy.engine import Engine, reflection
from sqlalchemy.schema import Index, Table
from wrdscli.equity.company import Company
from wrdscli.equity.security import Security
from typing import List

logging.shutdown()
reload(logging)
logging.basicConfig(format=LOG_FORMAT)
logger = logging.getLogger('wrdscli.equity')


@attr.s(auto_attribs=True)
class Equity:
    company: Company
    securities: List[Security] = []



class EquityLocator(object):
    def __init__(self, ticker):
        self.engine = get_wrds_engine()
    
    def locate_by_tic(self, tic):
        