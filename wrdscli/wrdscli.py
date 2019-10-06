#!/usr/bin/env python3

import click
import logging
import sys
import traceback
import time
import asyncio
import concurrent.futures
from os import getenv
from os.path import abspath
from wrdscli.common import get_wrds_engine, AsyncSafeRun
from sqlalchemy import MetaData
from sqlalchemy.engine import Engine, reflection
from sqlalchemy.schema import Index, Table
from wrdscli.db.commands import db
from wrdscli.common import get_logger

logger = get_logger('wrdscli')

@AsyncSafeRun(logger)
async def _create_index(meta: MetaData, engine: Engine, table: Table,
                        column: str):
    logger.info(f'Creating index on {table.schema}.{table.name}')
    ts = time.time()
    idx_name = f'{table.name}_{column}_idx'
    index = Index(idx_name, table.columns[column])
    loop = asyncio.get_event_loop()
    with concurrent.futures.ThreadPoolExecutor() as executor:
        await loop.run_in_executor(executor, lambda: index.create(bind=engine))
    te = time.time()
    logger.info(f'Index {idx_name} created after {(te - ts):.2f} seconds')


@AsyncSafeRun(logger)
async def _create_indices(schema, tables, column):
    engine = get_wrds_engine()
    meta = MetaData(schema=schema)
    logger.info(f'Reflecting DB on schema {schema}...')
    meta.reflect(bind=engine)
    insp = reflection.Inspector.from_engine(engine)
    tasks, success, failure, skipped, total = [], 0, 0, 0, len(meta.tables)
    for table in meta.tables.values():
        if not tables or table.name in tables:
            indices = insp.get_indexes(table.name, schema=schema)
            idx_columns = {name for names in [
                index['column_names'] for index in indices] for name in names}
            if not indices or (column in table.columns.keys()
                               and column not in idx_columns):
                tasks.append(_create_index(meta, engine, table, column))
            elif column not in table.columns.keys():
                logger.info(
                    '{schema}.{table} doesn\'t have column {column}, '
                    f'skipping')
                skipped += 1
            elif column in idx_columns:
                logger.info(
                    'Index on {column} already present in {schema}.{table}, '
                    f'skipping')
                skipped += 1
    if tasks:
        results = await asyncio.gather(*tasks)
        failure = sum(results)
        success = len(results) - failure
    logger.info(
        'Schema {schema} has {total} tables, created {success} indices,'
        ' failed {failure} tables, skipped {skipped} tables, checked '
        f'{len(tables)} tables.')


@click.group()
@click.option('--debug/--no-debug', default=False)
@click.option('--config_path', default=abspath('wrdscli/config/default.ini'))
@click.pass_context
def wrdscli(ctx, debug, config_path):
    '''
    Tool for interacting with WRDS database
    '''
    ctx.ensure_object(dict)
    logger.setLevel('DEBUG' if debug else 'INFO')
    ctx.obj['DEBUG'] = debug
    config = ConfigParser()
    config.read(config_path)
    ctx.obj['raw_config'] = config
    ctx.obj['db'] = config['db']


wrdscli.add_command(db)

def __main__():
    wrdscli()  # pylint: disable=no-value-for-parameter

if __name__ == '__main__':
    __main__()
