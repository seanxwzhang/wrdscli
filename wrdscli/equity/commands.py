#!/usr/bin/env python3

import click
import logging
import sys
import traceback
import time
import asyncio
import concurrent.futures
from os import getenv
from importlib import import_module, reload
from wrdscli.common import get_wrds_engine, AsyncSafeRun, LOG_FORMAT
from sqlalchemy import MetaData
from sqlalchemy.engine import Engine, reflection
from sqlalchemy.schema import Index, Table
        
logging.shutdown()
reload(logging)
logging.basicConfig(format=LOG_FORMAT)
logger = logging.getLogger('wrdscli.equity')


@click.group('equity')
@click.pass_context
def equity(ctx):
    pass

@equity.command()
@click.pass_context
@click.argument('ticker')
def show(ctx, ticker):
    gvkey = get_gvkey_by_ticker(ticker)