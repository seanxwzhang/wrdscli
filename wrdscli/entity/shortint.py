import attr
from wrdscli.lib.base import WRDSEntity

@attr.s(auto_attribs=True)
class ShortInt(WRDSEntity):
    schema = 'comp'
    table = 'sec_shortint'
    datadate: str = None
    cik: str = None  # CIK Number
    cusip: str = None  # CUSIP
    gvkey: str = None  # GVKEY
    iid: str = None  # IID -- Global Issue Key
    naics: str = None  # NAICS Code
    shortint: int = None  # SHORTINT -- Shares Held Short as of Settlement Date
    shortintadj: int = None  # SHORTINTADJ -- Shares Held Short as of Settlement Date - Adjusted
    sic: str = None  # SIC Code
    splitadjdate: str = None  # SPLITADJDATE -- Month End Split Adjustment Date
    tic: str = None  # Ticker Symbol

    @staticmethod
    def from_gvkey(gvkey):
        return super(ShortInt, ShortInt).from_attr(ShortInt, 'gvkey', gvkey, exact=True)