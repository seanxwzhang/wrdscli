
import attr
from typing import List
from wrdscli.equity.company import Company
from wrdscli.equity.security import Security
from wrdscli.lib.base import Loggable

@attr.s(auto_attribs=True)
class Equity(Loggable):
    company: Company
    securities: List[Security] = []
