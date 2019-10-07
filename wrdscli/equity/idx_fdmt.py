#!/usr/bin/env python3

import attr
from wrdscli.lib.base import WRDSEntity

@attr.s(auto_attribs=True)
class IdxFdmt(WRDSEntity):
    schema = 'comp'
    table = 'idx_ann'
    aco: int = -1  # ACO -- Current Assets - Other - Index Fundamental
    act: int = -1  # ACT -- Current Assets - Total - Index Fundamental
    ao: int = -1  # AO -- Assets - Other - Index Fundamental
    ap: int = -1  # AP -- Accounts Payable - Index Fundamental
    at: int = -1  # AT -- Assets - Total - Index Fundamental
    caps: int = -1  # CAPS -- Capital Surplus - Index Fundamental
    capx: int = -1  # CAPX -- Capital Expenditures - Index Fundamental
    ceq: int = -1  # CEQ -- Common Equity - Total - Index Fundamental
    che: int = -1  # CHE -- Cash and Equivalents - Index Fundamental
    cogs: int = -1  # COGS -- Cost of Goods Sold - Index Fundamental
    conm: str = ''  # CONM -- Index Name
    cstk: int = -1  # CSTK -- Common Stock - Index Fundamental
    cstke: int = -1  # CSTKE -- Common Stock Equivalents - Dollar Savings - Index Fundamental
    dd1: int = -1  # DD1 -- Current Long Term Debt
    dlc: int = -1  # DLC -- Debt in Current Liabilities - Index Fundamental
    dltt: int = -1  # DLTT -- Long Term Debt - Total - Index Fundamental
    dp: int = -1  # DP -- Depreciation and Amortization - Index Fundamental
    dpc: int = -1  # DPC -- Depreciation and Amortization - Statement of Cash Flows - Index Fundamental
    dv: int = -1  # DV -- Cash Dividends - Annual Index Fundamental Cash Flow
    dvp: int = -1  # DVP -- Preferred Cash Dividends - Index Fundamental
    epsfi: int = -1  # EPSFI -- Earnings Per Share (Diluted) - Including Extraordinary items
    epsfx: int = -1  # EPSFX -- Earnings Per Share (Diluted) - Excluding Extraordinary items
    epspi: int = -1  # EPSPI -- Earnings Per Share - Including Extraordinary Items - Index Fundamental
    epspx: int = -1  # EPSPX -- Earnings Per Share - Excluding Extraordinary Items - Index Fundamental
    fincf: int = -1  # FINCF -- Financing Activities - Net Cash Flow - Index Fundamental
    ib: int = -1  # IB -- Income Before Extraordinary Items - Index Fundamental
    ibadj: int = -1  # IBADJ -- Income Before Extraordinary Items - Adjusted for Common Stock Equivalents -
    ibcom: int = -1  # IBCOM -- Income Before Extraordinary Items - Available for Common - Index Fundamenta
    icapt: int = -1  # ICAPT -- Invested Capital - Total - Index Fundamental
    indexcat: str = ''  # INDEXCAT -- Index Category Code
    indextype: str = ''  # INDEXTYPE -- Index Code Type
    intan: int = -1  # INTAN -- Intangibles
    invt: int = -1  # INVT -- Inventory - Total - Index Fundamental
    itcb: int = -1  # ITCB -- Investment Tax Credit - Balance Sheet - Index Fundamental
    ivaeq: int = -1  # IVAEQ -- Investments and Advancements at Equity
    ivncf: int = -1  # IVNCF -- Investing Activities - Net Cash Flow - Index Fundamental
    lco: int = -1  # LCO -- Current Liabilities - Other - Index Fundamental
    lct: int = -1  # LCT -- Current Liabilities - Total - Index Fundamental
    lo: int = -1  # LO -- Liabilities - Other - Index Fundamental
    lt: int = -1  # LT -- Liabilities - Total - Index Fundamental
    mib: int = -1  # MIB -- Minority Interest - Balance Sheet - Index Fundamental
    mii: int = -1  # MII -- Minority Interest - Income Account - Index Fundamental
    ni: int = -1  # NI -- Net Income - Index Fundamental
    nopi: int = -1  # NOPI -- Nonoperating Income - Index Fundamental
    np: int = -1  # NP -- Notes Payable
    oancf: int = -1  # OANCF -- Operating Activities - Net Cash Flow - Index Fundamental
    oiadp: int = -1  # OIADP -- Operating Income After Depreciation - Index Fundamental
    oibdp: int = -1  # OIBDP -- Operating Income Before Depreciation - Index Fundamental
    opeps: int = -1  # OPEPS -- Earnings Per Share from Operations - Index Fundamental
    opepsx: int = -1  # OPEPSX -- Earnings Per Share (Diluted) from Operations
    pi: int = -1  # PI -- Pretax Income - Index Fundamental
    ppent: int = -1  # PPENT -- PP&E Total - Net - Index Fundamental
    pstk: int = -1  # PSTK -- Preferred Stock - Index Fundamental
    re: int = -1  # RE -- Retained Earnings - Index Fundamental
    rect: int = -1  # RECT -- Receivables - Total - Index Fundamental
    sale: int = -1  # SALE -- Sales - Index Fundamental
    seq: int = -1  # SEQ -- Stockholders Equity - Total - Index Fundamental
    spi: int = -1  # SPI -- Special Items - Index Fundamental
    spii: str = ''  # SPII -- S&P Industry Index Identifier
    spmi: str = ''  # SPMI -- S&P Major Index Identifier
    sppe: int = -1  # SPPE -- Sale of Property, Plant, and Equipment - Index Fundamental
    sstk: int = -1  # SSTK -- Sale of Stock - Index Fundamental
    tic: str = ''  # TIC -- Ticker
    tstk: int = -1  # TSTK -- Treasury Stock - Total - Index Fundamental
    txdb: int = -1  # TXDB -- Deferred Taxes - Balance Sheet - Index Fundamental
    txditc: int = -1  # TXDITC -- Deferred Taxes and Investment Tax Credit - Index Fundamental
    txp: int = -1  # TXP -- Income Taxes Payable - Index Fundamental
    txr: int = -1  # TXR -- Income Tax Refund - Index Fundamental
    txt: int = -1  # TXT -- Income Taxes - Total - Index Fundamental
    xacc: int = -1  # XACC -- Accrued Expenses - Index Fundamental
    xint: int = -1  # XINT -- Interest Expense - Index Fundamental
    xsga: int = -1  # XSGA -- Selling, General, and Administrative Expenses - Index Fundamental

    @staticmethod
    def from_name(conm):
        return super(IdxFdmt, IdxFdmt).from_attr(IdxFdmt, 'conm', conm)
