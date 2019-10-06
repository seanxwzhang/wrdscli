#!/usr/bin/env python3

import attr
from wrdscli.lib.base import WRDSEntity

@attr.s(auto_attribs=True)
class Security(WRDSEntity):
    schema = 'comp'
    table = 'security'
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

    @staticmethod
    def from_gvkey(gvkey):
        '''
        Return 0 or more securities given gvkey
        '''
        res_proxy = super(Security, Security).from_attr('gvkey', gvkey)
        res = []
        for obj in [{column: value for column, value in row_proxy.items()} for row_proxy in res_proxy]:
            res.append(Security(**obj))
        return res

    @staticmethod
    def from_tic(tic):
        '''
        Return 0 or more securities given tic
        '''
        res_proxy = super(Security, Security).from_attr('tic', tic)
        res = []
        for obj in [{column: value for column, value in row_proxy.items()} for row_proxy in res_proxy]:
            res.append(Security(**obj))
        return res