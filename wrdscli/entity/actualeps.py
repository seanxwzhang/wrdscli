import attr
from wrdscli.lib.base import WRDSEntity

@attr.s(auto_attribs=True)
class ActualEPS(WRDSEntity):
    schema = 'ibes'
    table = 'act_epsus'
    measure: str = None
    pdicity: str = None
    actdats: str = None  # Activation Date, SAS Format
    acttims: int = None  # Activation Time, SAS Format
    anndats: str = None  # Announce Date, SAS Format
    anntims: int = None  # Announce Time, SAS Format
    cname: str = None  # Company Name
    curr_act: str = None  # Currency
    cusip: str = None  # CUSIP/SEDOL
    oftic: str = None  # Official Ticker
    pends: str = None  # Period End Date, SAS Format
    ticker: str = None  # I/B/E/S Ticker
    usfirm: int = None  # U.S. Firm (USFIRM=0 if from .INT, and USFIRM=1 if from .US file)
    value: int = None  # Value


    @staticmethod
    def from_cusip(cusip, limit=None, remove_check=True):
        if remove_check:
            cusip = cusip[:-1]
        return super(ActualEPS, ActualEPS).from_attr(ActualEPS, 'cusip', cusip, exact=True, limit=limit)