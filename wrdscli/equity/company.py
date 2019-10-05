#!/usr/bin/env python3

import attr

@attr.s(auto_attribs=True)
class Company:
    conm: str  # Company name
    gvkey: str
    add1: str = ''
    add2: str = ''
    add3: str = ''
    add4: str = ''
    addzip: str = ''
    busdesc: str = ''
    cik: str = '' # CIK number
    city: str = ''
    conml: str = ''  # company legal name
    costat: str = ''  # activae/inactive status marker
    dlrsn: str = ''  # delete reason
    ein: str = ''  # Employer Identification Number
    fax: str = ''  # Fax Number
    fic: str = ''  # ISO country code
    fyrc: int = -1  # Fiscal year-end month
    ggroup: str = ''  # GICS Industry Groups
    gind: str = '' # GICS industries
    gsector: str = ''  # GICS sector
    gsubind: str = ''  # GICS sub-industries
    idbflag: str = ''  # International, domestic, both indicator
    incorp: str = ''  # State/Province of Incorporation Code
    loc: str = ''  # ISO Country Code - Headquarters
    naics: str = ''  # NAICS Codes
    phone: str = ''
    prican: str = ''  # Primary Issue Tag - Canada
    prirow: str = ''  # Primary Issue - Global
    priusa: str = ''  # Primary Issue Tag - U.S.
    sic: str = ''  # SIC Code
    spcindcd: int = -1  # S&P Industry Sector Code
    spcseccd: int = -1  # S&P Economic Sector Code
    spcsrc: str = ''  # S&P Quality Ranking - Current
    state: str = ''  # State/Province
    stko: str = ''  # Stock Ownership
    weburl: str = ''
    dldte: str = ''  # Research Company Deletion Date
    ipodate: str = ''  # Initial Public Offering Date
