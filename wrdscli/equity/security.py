#!/usr/bin/env python3

import attr
from wrdscli.lib.base import WRDSEntity

@attr.s(auto_attribs=True)
class Security(WRDSEntity):
    iid: str  # Issue ID
    gvkey: str
    tic: str = ''
    cusip: str = ''
    dlrsni: str = ''  # Security Inactivation Code
    dsci: str = ''  # Security Description
    epf: str = ''  # Earnings Participation Flag
    exchg: str = ''  # Stock Exchange
    excntry: str = ''  # Stock Exchange Country Code
    ibtic: str = ''  # I/B/E/S Ticker Symbol
    isin: str = ''  # International Securities Identification Number
    secstat: str = ''  # Security Status Marker
    sedol: str = ''  # Stock Exchange Daily Official List
    tpci: str = ''  # Issue Type
    dldtei: str = ''  # Security Inactivation Date