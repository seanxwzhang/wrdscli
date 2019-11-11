import asyncio
import attr
import pandas as pd
from async_lru import alru_cache
from typing import List
from functools import lru_cache
from wrdscli.entity.company import Company
from wrdscli.entity.security import Security
from wrdscli.entity.fdmt import Fdmt, FdmtAnn
from wrdscli.entity.footnote import FootnoteA, FootnoteQ
from wrdscli.entity.shortint import ShortInt
from wrdscli.entity.secd import Secd
from wrdscli.entity.estimate import Estimate
from wrdscli.entity.actualeps import ActualEPS
from wrdscli.entity.ptarget import PriceTarget
from wrdscli.lib.base import WRDSHelper
from wrdscli.common import get_logger

import sys
if sys.version_info.minor < 8:
  from cached_property import cached_property
else:
  from functools import cached_property

logger = get_logger('equity')

@attr.s(auto_attribs=True)
class Equity(WRDSHelper):
  company: Company
  securities: List[Security] = []
  fdmts: List[Fdmt] = []
  fdmts_ann: List[FdmtAnn] = []
  afootnotes: List[FootnoteA] = []
  qfootnotes: List[FootnoteQ] = []
  shortints: List[ShortInt] = []
  secds: List[Secd] = []
  estimates: List[Estimate] = []
  actualeps: List[ActualEPS] = []
  pricetargets: List[PriceTarget] = []

  @staticmethod
  @alru_cache(maxsize=128)
  async def from_tic(tic):
    securities = await Security.from_tic(tic)
    if not securities:
      logger.error(f'Can\'t find securities with tic {tic}')
    if len(securities) > 1:
      logger.warning(
        f'Found {len(securities)} securities with tic {tic}')
    security = securities[0]
    return await Equity.from_security(security)

  @staticmethod
  async def from_security(sec):
    company_aws = Company.from_gvkey(sec.gvkey)
    securities_aws = Security.from_gvkey(sec.gvkey)
    fdmts_aws = Fdmt.from_gvkey(sec.gvkey)
    afootnotes_aws = FootnoteA.from_gvkey(sec.gvkey)
    qfootnotes_aws = FootnoteQ.from_gvkey(sec.gvkey)
    shortints_aws = ShortInt.from_gvkey(sec.gvkey)
    secds_aws = Secd.from_gvkey(sec.gvkey)
    estimates_aws = Estimate.from_cusip(sec.cusip)
    actualeps_aws = ActualEPS.from_cusip(sec.cusip)
    pricetargets_aws = PriceTarget.from_cusip(sec.cusip)
    fdmts_ann_aws = FdmtAnn.from_gvkey(sec.gvkey)
    (
      company,
      securities,
      fdmts,
      fdmts_ann,
      afootnotes,
      qfootnotes,
      shortints,
      secds,
      estimates,
      actualeps,
      pricetargets
    ) = await asyncio.gather(
        company_aws,
        securities_aws,
        fdmts_aws,
        fdmts_ann_aws,
        afootnotes_aws,
        qfootnotes_aws,
        shortints_aws,
        secds_aws,
        estimates_aws,
        actualeps_aws,
        pricetargets_aws
    )
    return Equity(
      company,
      securities,
      fdmts,
      fdmts_ann,
      afootnotes,
      qfootnotes,
      shortints,
      secds,
      estimates,
      actualeps,
      pricetargets
    )

  @cached_property
  def company_pd(self):
    return self._make_df(self.company)

  @cached_property
  def securities_pd(self):
    return self._make_df(self.securities)

  @cached_property
  def fdmts_pd(self):
    return self._make_df(self.fdmts)

  @cached_property
  def fdmts_ann_pd(self):
    return self._make_df(self.fdmts_ann)

  @cached_property
  def afootnotes_pd(self):
    return self._make_df(self.afootnotes)

  @cached_property
  def qfootnotes_pd(self):
    return self._make_df(self.qfootnotes)

  @cached_property
  def shortints_pd(self):
    return self._make_df(self.shortints)

  @cached_property
  def secds_pd(self):
    return self._make_df(self.secds)

  @cached_property
  def estimates_pd(self):
    return self._make_df(self.estimates)

  @cached_property
  def actualeps_pd(self):
    return self._make_df(self.actualeps)

  @cached_property
  def pricetargets_pd(self):
    return self._make_df(self.pricetargets)
