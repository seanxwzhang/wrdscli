import attr
from wrdscli.lib.base import WRDSEntity

@attr.s(auto_attribs=True)
class Secd(WRDSEntity):
    schema = 'comp'
    table = 'secd'
    gvkey: str
    datadate: str
    add1: str = None  # ADD1 -- Address Line 1
    add2: str = None  # ADD2 -- Address Line 2
    add3: str = None  # ADD3 -- Address Line 3
    add4: str = None  # ADD4 -- Address Line 4
    addzip: str = None  # ADDZIP -- Postal Code
    adrrc: int = None  # ADRRC -- ADR Ratio - Daily
    ajexdi: int = None  # AJEXDI -- Adjustment Factor (Issue)-Cumulative by Ex-Date
    anncdate: str = None  # ANNCDATE -- Dividend Declaration Date
    busdesc: str = None  # BUSDESC -- S&P Business Description
    capgn: int = None  # CAPGN -- Capital Gains - Daily
    capgnpaydate: str = None  # CAPGNPAYDATE -- Capital Gains Payment Date
    cheqv: int = None  # CHEQV -- Cash Equivalent Distributions
    cheqvpaydate: str = None  # CHEQVPAYDATE -- Cash Equivalent Distributions per Share Payment Date
    cik: str = None  # CIK Number
    city: str = None  # CITY -- City
    conm: str = None  # Company Name
    conml: str = None  # CONML -- Company Legal Name
    costat: str = None  # COSTAT -- Active/Inactive Status Marker
    county: str = None  # COUNTY -- County Code
    cshoc: int = None  # CSHOC -- Shares Outstanding
    cshtrd: int = None  # CSHTRD -- Trading Volume - Daily
    curcdd: str = None  # CURCDD -- ISO Currency Code - Daily
    curcddv: str = None  # CURCDDV -- ISO Currency Code - Dividend
    cusip: str = None  # CUSIP
    div: int = None  # DIV -- Dividends per Share - Ex Date - Daily (Issue)
    divd: int = None  # DIVD -- Cash Dividends - Daily
    divdpaydate: str = None  # DIVDPAYDATE -- Cash Dividends - Daily Payment Date
    divdpaydateind: str = None  # DIVDPAYDATEIND -- Cash Dividends - Daily Payment Date Indicator
    divsp: int = None  # DIVSP -- Special Cash Dividends - Daily
    divsppaydate: str = None  # DIVSPPAYDATE -- Special Cash Dividends - Daily Payment Date
    dldte: str = None  # DLDTE -- Research Company Deletion Date
    dlrsn: str = None  # DLRSN -- Research Co Reason for Deletion
    dvi: int = None  # DVI -- Indicated Annual Dividend - Current
    dvrated: int = None  # DVRATED -- Indicated Annual Dividend Rate - Daily
    ein: str = None  # EIN -- Employer Identification Number
    eps: int = None  # EPS -- Current EPS
    epsmo: int = None  # EPSMO -- Current EPS Month
    exchg: int = None  # Stock Exchange Code
    fax: str = None  # FAX -- Fax Number
    fic: str = None  # Foreign Incorporation Code
    fyrc: int = None  # FYRC -- Current Fiscal Year End Month
    ggroup: str = None  # GGROUP -- GIC Groups
    gind: str = None  # GIND -- GIC Industries
    gsector: str = None  # GSECTOR -- GIC Sectors
    gsubind: str = None  # GSUBIND -- GIC Sub-Industries
    idbflag: str = None  # IDBFLAG -- International, Domestic, Both Indicator
    iid: str = None  # IID -- Issue ID - Dividends
    incorp: str = None  # INCORP -- Current State/Province of Incorporation Code
    ipodate: str = None  # IPODATE -- Company Initial Public Offering Date
    loc: str = None  # LOC -- Current ISO Country Code - Headquarters
    naics: str = None  # NAICS -- North American Industry Classification Code
    paydate: str = None  # PAYDATE -- Dividend Payment Date
    paydateind: str = None  # PAYDATEIND -- Dividend Payment Date Indicator
    phone: str = None  # PHONE -- Phone Number
    prccd: int = None  # PRCCD -- Price - Close - Daily
    prchd: int = None  # PRCHD -- Price - High - Daily
    prcld: int = None  # PRCLD -- Price - Low - Daily
    prcod: int = None  # PRCOD -- Price - Open - Daily
    prcstd: int = None  # PRCSTD -- Price Status Code - Daily
    prican: str = None  # PRICAN -- Current Primary Issue Tag - Canada
    prirow: str = None  # PRIROW -- Primary Issue Tag - Rest of World
    priusa: str = None  # PRIUSA -- Current Primary Issue Tag - US
    recorddate: str = None  # RECORDDATE -- Dividend Record Date
    secstat: str = None  # Security Status Market
    sic: str = None  # SIC -- Standard Industry Classification Code
    spcindcd: int = None  # SPCINDCD -- S&P Industry Sector Code
    spcseccd: int = None  # SPCSECCD -- S&P Economic Sector Code
    spcsrc: str = None  # SPCSRC -- S&P Quality Ranking - Current
    state: str = None  # STATE -- State/Province
    stko: int = None  # STKO -- Stock Ownership Code
    tic: str = None  # Ticker Symbol
    tpci: str = None  # Issue Type Code
    trfd: int = None  # TRFD -- Daily Total Return Factor
    weburl: str = None  # WEBURL -- Web URL


    @staticmethod
    def from_gvkey(gvkey, limit=None):
        return super(Secd, Secd).from_attr(Secd, 'gvkey', gvkey, exact=True, limit=limit)