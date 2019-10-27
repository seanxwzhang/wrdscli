
import attr
import pandas as pd
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
    @lru_cache(maxsize=128)
    def from_tic(tic):
        securities = Security.from_tic(tic)
        if not securities:
            logger.error(f'Can\'t find securities with tic {tic}')
        if len(securities) > 1:
            logger.warning(f'Found {len(securities)} securities with tic {tic}')
        security = securities[0]
        return Equity.from_security(security)

    @staticmethod
    def from_security(sec):
        company = Company.from_gvkey(sec.gvkey)
        securities = Security.from_gvkey(sec.gvkey)
        fdmts = Fdmt.from_gvkey(sec.gvkey)
        afootnotes = FootnoteA.from_gvkey(sec.gvkey)
        qfootnotes = FootnoteQ.from_gvkey(sec.gvkey)
        shortints = ShortInt.from_gvkey(sec.gvkey)
        secds = Secd.from_gvkey(sec.gvkey)
        estimates = Estimate.from_cusip(sec.cusip)
        actualeps = ActualEPS.from_cusip(sec.cusip)
        pricetargets = PriceTarget.from_cusip(sec.cusip)
        fdmts_ann = FdmtAnn.from_gvkey(sec.gvkey)
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