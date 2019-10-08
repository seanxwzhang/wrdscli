#!/usr/bin/env python3

import attr
from wrdscli.lib.base import WRDSEntity

@attr.s(auto_attribs=True)
class Security(WRDSEntity):
    schema = 'comp'
    table = 'security'
    iid: str  # Issue ID
    gvkey: str
    tic: str = None
    cusip: str = None
    dlrsni: str = None  # Security Inactivation Code
    dsci: str = None  # Security Description
    epf: str = None  # Earnings Participation Flag
    exchg: str = None  # Stock Exchange
    excntry: str = None  # Stock Exchange Country Code
    ibtic: str = None  # I/B/E/S Ticker Symbol
    isin: str = None  # International Securities Identification Number
    secstat: str = None  # Security Status Marker
    sedol: str = None  # Stock Exchange Daily Official List
    tpci: str = None  # Issue Type
    dldtei: str = None  # Security Inactivation Date

    @staticmethod
    def from_gvkey(gvkey):
        '''
        Return 0 or more securities given gvkey
        '''
        return super(Security, Security).from_attr(Security, 'gvkey', gvkey)

    @staticmethod
    def from_tic(tic):
        '''
        Return 0 or more securities given tic
        '''
        return super(Security, Security).from_attr(Security, 'tic', tic, exact=True)