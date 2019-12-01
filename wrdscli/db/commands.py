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
logger = logging.getLogger('wrdscli.db')

@AsyncSafeRun(logger)
async def _create_index(meta: MetaData, engine: Engine, table: Table, column: str):
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
            idx_columns = {name for names in [index['column_names'] for index in indices] for name in names}
            if not indices or (column in table.columns.keys() and column not in idx_columns):
                tasks.append(_create_index(meta, engine, table, column))
            elif column not in table.columns.keys():
                logger.info(f'{schema}.{table} doesn\'t have column {column}, skipping')
                skipped += 1
            elif column in idx_columns:
                logger.info(f'Index on {column} already present in {schema}.{table}, skipping')
                skipped += 1
    if tasks:
        results = await asyncio.gather(*tasks)
        failure = sum(results)
        success = len(results) - failure
    logger.info(f'Schema {schema} has {total} tables, created {success} indices, failed {failure} tables, skipped {skipped} tables, checked {len(tables)} tables.')
        

@click.group('db')
@click.pass_context
def db(ctx):
    pass

@db.command()
@click.pass_context
@click.argument('schema')
@click.option('-t', '--table', multiple=True)
@click.option('-k', '--column', default='gvkey')
def create_index(ctx, schema, table, column):
    asyncio.run(_create_indices(schema, table, column))
