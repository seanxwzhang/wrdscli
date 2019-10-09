import attr
from wrdscli.lib.base import WRDSEntity

@attr.s(auto_attribs=True)
class PriceTarget(WRDSEntity):
    schema = 'ibes'
    table = 'ptgdet'
    measure: str = None
    pdicity: str = None
    actdats: str = None  # Activation Date, SAS Format
    acttims: int = None  # Activation Time, SAS Format
    alysnam: str = None  # Analyst Name
    amaskcd: int = None  # Analyst Mask Code
    anndats: str = None  # Announce Date, SAS Format
    anntims: int = None  # Announce Time, SAS Format
    cname: str = None  # Company Name
    curr: str = None  # Currency at Company Level
    cusip: str = None  # CUSIP/SEDOL
    estcur: str = None  # Estimate Currency
    estimid: str = None  # Estimator ID
    horizon: str = None  # Horizon
    oftic: str = None  # Official Ticker
    ticker: str = None  # I/B/E/S Ticker
    usfirm: int = None  # USFIRM=0 if from .INT file and USFIRM=1 if from .US file
    value: int = None  # Value



    @staticmethod
    def from_cusip(cusip, limit=None, remove_check=True):
        if remove_check:
            cusip = cusip[:-1]
        return super(PriceTarget, PriceTarget).from_attr(PriceTarget, 'cusip', cusip, exact=True, limit=limit)