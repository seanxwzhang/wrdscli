
import attr
from typing import List
from wrdscli.equity.company import Company
from wrdscli.equity.security import Security
from wrdscli.lib.base import Loggable
from wrdscli.common import get_logger

logger = get_logger('equity')

@attr.s(auto_attribs=True)
class Equity(Loggable):
    company: Company
    securities: List[Security] = []

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
        return Equity(company, securities)
