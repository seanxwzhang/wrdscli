#!/usr/bin/env python3

import attr
from wrdscli.lib.base import WRDSEntity

@attr.s(auto_attribs=True)
class IdxFdmt(WRDSEntity):
    schema = 'comp'
    table = 'idx_ann'
    aco: int = None  # ACO -- Current Assets - Other - Index Fundamental
    act: int = None  # ACT -- Current Assets - Total - Index Fundamental
    ao: int = None  # AO -- Assets - Other - Index Fundamental
    ap: int = None  # AP -- Accounts Payable - Index Fundamental
    at: int = None  # AT -- Assets - Total - Index Fundamental
    caps: int = None  # CAPS -- Capital Surplus - Index Fundamental
    capx: int = None  # CAPX -- Capital Expenditures - Index Fundamental
    ceq: int = None  # CEQ -- Common Equity - Total - Index Fundamental
    che: int = None  # CHE -- Cash and Equivalents - Index Fundamental
    cogs: int = None  # COGS -- Cost of Goods Sold - Index Fundamental
    conm: str = None  # CONM -- Index Name
    cstk: int = None  # CSTK -- Common Stock - Index Fundamental
    cstke: int = None  # CSTKE -- Common Stock Equivalents - Dollar Savings - Index Fundamental
    dd1: int = None  # DD1 -- Current Long Term Debt
    dlc: int = None  # DLC -- Debt in Current Liabilities - Index Fundamental
    dltt: int = None  # DLTT -- Long Term Debt - Total - Index Fundamental
    dp: int = None  # DP -- Depreciation and Amortization - Index Fundamental
    dpc: int = None  # DPC -- Depreciation and Amortization - Statement of Cash Flows - Index Fundamental
    dv: int = None  # DV -- Cash Dividends - Annual Index Fundamental Cash Flow
    dvp: int = None  # DVP -- Preferred Cash Dividends - Index Fundamental
    epsfi: int = None  # EPSFI -- Earnings Per Share (Diluted) - Including Extraordinary items
    epsfx: int = None  # EPSFX -- Earnings Per Share (Diluted) - Excluding Extraordinary items
    epspi: int = None  # EPSPI -- Earnings Per Share - Including Extraordinary Items - Index Fundamental
    epspx: int = None  # EPSPX -- Earnings Per Share - Excluding Extraordinary Items - Index Fundamental
    fincf: int = None  # FINCF -- Financing Activities - Net Cash Flow - Index Fundamental
    ib: int = None  # IB -- Income Before Extraordinary Items - Index Fundamental
    ibadj: int = None  # IBADJ -- Income Before Extraordinary Items - Adjusted for Common Stock Equivalents -
    ibcom: int = None  # IBCOM -- Income Before Extraordinary Items - Available for Common - Index Fundamenta
    icapt: int = None  # ICAPT -- Invested Capital - Total - Index Fundamental
    indexcat: str = None  # INDEXCAT -- Index Category Code
    indextype: str = None  # INDEXTYPE -- Index Code Type
    intan: int = None  # INTAN -- Intangibles
    invt: int = None  # INVT -- Inventory - Total - Index Fundamental
    itcb: int = None  # ITCB -- Investment Tax Credit - Balance Sheet - Index Fundamental
    ivaeq: int = None  # IVAEQ -- Investments and Advancements at Equity
    ivncf: int = None  # IVNCF -- Investing Activities - Net Cash Flow - Index Fundamental
    lco: int = None  # LCO -- Current Liabilities - Other - Index Fundamental
    lct: int = None  # LCT -- Current Liabilities - Total - Index Fundamental
    lo: int = None  # LO -- Liabilities - Other - Index Fundamental
    lt: int = None  # LT -- Liabilities - Total - Index Fundamental
    mib: int = None  # MIB -- Minority Interest - Balance Sheet - Index Fundamental
    mii: int = None  # MII -- Minority Interest - Income Account - Index Fundamental
    ni: int = None  # NI -- Net Income - Index Fundamental
    nopi: int = None  # NOPI -- Nonoperating Income - Index Fundamental
    np: int = None  # NP -- Notes Payable
    oancf: int = None  # OANCF -- Operating Activities - Net Cash Flow - Index Fundamental
    oiadp: int = None  # OIADP -- Operating Income After Depreciation - Index Fundamental
    oibdp: int = None  # OIBDP -- Operating Income Before Depreciation - Index Fundamental
    opeps: int = None  # OPEPS -- Earnings Per Share from Operations - Index Fundamental
    opepsx: int = None  # OPEPSX -- Earnings Per Share (Diluted) from Operations
    pi: int = None  # PI -- Pretax Income - Index Fundamental
    ppent: int = None  # PPENT -- PP&E Total - Net - Index Fundamental
    pstk: int = None  # PSTK -- Preferred Stock - Index Fundamental
    re: int = None  # RE -- Retained Earnings - Index Fundamental
    rect: int = None  # RECT -- Receivables - Total - Index Fundamental
    sale: int = None  # SALE -- Sales - Index Fundamental
    seq: int = None  # SEQ -- Stockholders Equity - Total - Index Fundamental
    spi: int = None  # SPI -- Special Items - Index Fundamental
    spii: str = None  # SPII -- S&P Industry Index Identifier
    spmi: str = None  # SPMI -- S&P Major Index Identifier
    sppe: int = None  # SPPE -- Sale of Property, Plant, and Equipment - Index Fundamental
    sstk: int = None  # SSTK -- Sale of Stock - Index Fundamental
    tic: str = None  # TIC -- Ticker
    tstk: int = None  # TSTK -- Treasury Stock - Total - Index Fundamental
    txdb: int = None  # TXDB -- Deferred Taxes - Balance Sheet - Index Fundamental
    txditc: int = None  # TXDITC -- Deferred Taxes and Investment Tax Credit - Index Fundamental
    txp: int = None  # TXP -- Income Taxes Payable - Index Fundamental
    txr: int = None  # TXR -- Income Tax Refund - Index Fundamental
    txt: int = None  # TXT -- Income Taxes - Total - Index Fundamental
    xacc: int = None  # XACC -- Accrued Expenses - Index Fundamental
    xint: int = None  # XINT -- Interest Expense - Index Fundamental
    xsga: int = None  # XSGA -- Selling, General, and Administrative Expenses - Index Fundamental

    @staticmethod
    def from_name(conm):
        return super(IdxFdmt, IdxFdmt).from_attr(IdxFdmt, 'conm', conm)
