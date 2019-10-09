
import attr
import pandas as pd
from typing import List
from wrdscli.entity.company import Company
from wrdscli.entity.security import Security
from wrdscli.entity.fdmt import Fdmt
from wrdscli.entity.footnote import FootnoteA, FootnoteQ
from wrdscli.entity.shortint import ShortInt
from wrdscli.entity.secd import Secd
from wrdscli.entity.estimate import Estimate
from wrdscli.entity.actualeps import ActualEPS
from wrdscli.entity.ptarget import PriceTarget
from wrdscli.lib.base import WRDSHelper
from wrdscli.common import get_logger

logger = get_logger('equity')

@attr.s(auto_attribs=True)
class Equity(WRDSHelper):
    company: Company
    securities: List[Security] = []
    fdmts: List[Fdmt] = []
    afootnotes: List[FootnoteA] = []
    qfootnotes: List[FootnoteQ] = []
    shortints: List[ShortInt] = []
    secds: List[Secd] = []
    estimates: List[Estimate] = []
    actualeps: List[ActualEPS] = []
    pricetargets: List[PriceTarget] = []

    @staticmethod
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
        return Equity(
            company,
            securities,
            fdmts,
            afootnotes,
            qfootnotes,
            shortints,
            secds,
            estimates,
            actualeps,
            pricetargets
            )

    @property
    def company_pd(self):
        return self._make_df(self.company)

    @property
    def securities_pd(self):
        return self._make_df(self.securities)

    @property
    def fdmts_pd(self):
        return self._make_df(self.fdmts)

    @property
    def afootnotes_pd(self):
        return self._make_df(self.afootnotes)

    @property
    def qfootnotes_pd(self):
        return self._make_df(self.qfootnotes)

    @property
    def shortints_pd(self):
        return self._make_df(self.shortints)

    @property
    def secds_pd(self):
        return self._make_df(self.secds)

    @property
    def estimates_pd(self):
        return self._make_df(self.estimates)

    @property
    def actualeps_pd(self):
        return self._make_df(self.actualeps)

    @property
    def pricetargets_pd(self):
        return self._make_df(self.pricetargets)