import attr
from typing import List
from async_lru import alru_cache
from wrdscli.common import get_logger
from wrdscli.lib.base import WRDSEntity, WRDSHelper
from wrdscli.entity.idx_fdmt import IdxFdmtAnn, IdxFdmtQrt, IdxMth, IdxDaily

import sys
if sys.version_info.minor < 8:
    from cached_property import cached_property
else:
    from functools import cached_property

logger = get_logger('index')

@attr.s(auto_attribs=True)
class Index(WRDSEntity, WRDSHelper):
  schema = 'comp'
  table = 'idx_index'
  ann_fdmt : List[IdxFdmtAnn] = None
  qrt_fdmt : List[IdxFdmtQrt] = None
  mth : List[IdxMth] = None
  daily : List[IdxDaily] = None
  conm : str = None  # Index Name
  gvkeyx : str = None  # Global Index Key - Index
  idx13key : str = None  # 13 Character Key
  idxcstflg : str = None  # Index Constituent Flag
  idxstat : str = None  # Index Active/Inactive Flag
  indexcat : str = None  # Index Category Code
  indexgeo : str = None  # Index Geographical Area
  indexid : str = None  # Index Identifier
  indextype : str = None  # Index Code Type
  indexval : str = None  # Index Code Value
  spii : str = None  # S&P Industry Index Identifier
  spmi : str = None  # S&P Major Index Identifier
  tic : str = None  # Ticker
  tici : str = None  # Issue Trading Ticker

  def _initialize(self):
    self.ann_fdmt = IdxFdmtAnn.from_gvkeyx(self.gvkeyx)
    self.qrt_fdmt = IdxFdmtQrt.from_gvkeyx(self.gvkeyx)
    self.mth = IdxMth.from_gvkeyx(self.gvkeyx)
    self.daily = IdxDaily.from_gvkeyx(self.gvkeyx)

  @staticmethod
  @alru_cache(maxsize=128)
  async def from_name(conm):
    res = await super(Index, Index).from_attr(Index, 'conm', conm)
    if len(res) == 1:
      res[0]._initialize()
      return res[0]
    elif len(res) > 1:
      logger.warning(f'Found {len(res)} indices with name {conm}:\n {[idx.conm for idx in res]}, return first one')
      res[0]._initialize()
      return res[0]
    else:
      logger.error(f'Found 0 indices with name {conm}')

  @cached_property
  def ann_fdmt_pd(self):
    return self._make_df(self.ann_fdmt)

  @cached_property
  def qrt_fdmt_pd(self):
    return self._make_df(self.qrt_fdmt)

  @cached_property
  def mth_pd(self):
    return self._make_df(self.mth)

  @cached_property
  def daily_pd(self):
    return self._make_df(self.daily)
