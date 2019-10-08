import attr
from wrdscli.lib.base import WRDSEntity

@attr.s(auto_attribs=True)
class Estimate(WRDSEntity):
    schema = 'ibes'
    table = 'det_epsus'
    measure: str = None
    fpi: str = None  # Forecast Period Indicator
    actdats: str = None  # Activation Date, SAS Format
    actdats_act: int = None  # Activation Date of the Actual, from the Detail Actual File, SAS Format
    acttims: int = None  # Activation Time, SAS Format
    acttims_act: int = None  # Activation Time of the Actual, from the Detail Actual File, SAS Format
    actual: int = None  # Actual Value, from the Detail Actuals File
    analys: int = None  # Analyst Code
    anndats: str = None  # Announce Date, SAS Format
    anndats_act: int = None  # Announce Date of the Actual, from the Detail Actuals File, SAS Format
    anntims: int = None  # Announce Time, SAS Format
    anntims_act: int = None  # Announce Time of the Actual, from the Detail Actuals File, SAS Format
    cname: str = None  # Company Name
    curr: str = None  # Currency
    curr_act: str = None  # Currency from the detail Actuals File
    currfl: str = None  # Canadian Currency (Estimate Level)
    cusip: str = None  # CUSIP (8-digit)
    estimator: int = None  # Estimator
    fpedats: int = None  # Forecast Period End Date, SAS Format
    oftic: str = None  # Official Ticker
    pdf: str = None  # Primary/Diluted Flag(Estimate Level)
    report_curr: str = None  # Report Currency from Report Currency File
    revdats: int = None  # Review Date, SAS Format
    revtims: int = None  # Review Time, SAS Format
    ticker: str = None  # I/B/E/S Ticker
    usfirm: int = None  # U.S. Firm (USFIRM=0 if from .INT, and USFIRM=1 if from .US file)
    value: int = None  # Estimate Value


    @staticmethod
    def from_cusip(cusip, limit=None, remove_check=True):
        if remove_check:
            cusip = cusip[:-1]
        return super(Estimate, Estimate).from_attr(Estimate, 'cusip', cusip, exact=True, limit=limit)