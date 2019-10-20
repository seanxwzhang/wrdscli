#!/usr/bin/env python3

import attr
from wrdscli.lib.base import WRDSEntity

@attr.s(auto_attribs=True)
class IdxFdmtAnn(WRDSEntity):
  schema = 'comp'
  table = 'idx_ann'
  gvkeyx : str = None  # Global Index Key - Index Annual
  aco : int = None  # Current Assets - Other - Index Fundamental
  act : int = None  # Current Assets - Total - Index Fundamental
  ao : int = None  # Assets - Other - Index Fundamental
  ap : int = None  # Accounts Payable - Index Fundamental
  at : int = None  # Assets - Total - Index Fundamental
  caps : int = None  # Capital Surplus - Index Fundamental
  capx : int = None  # Capital Expenditures - Index Fundamental
  ceq : int = None  # Common Equity - Total - Index Fundamental
  che : int = None  # Cash and Equivalents - Index Fundamental
  cogs : int = None  # Cost of Goods Sold - Index Fundamental
  cstk : int = None  # Common Stock - Index Fundamental
  cstke : int = None  # Common Stock Equivalents - Dollar Savings - Index Fundamental
  dd1 : int = None  # Current Long Term Debt
  dlc : int = None  # Debt in Current Liabilities - Index Fundamental
  dltt : int = None  # Long Term Debt - Total - Index Fundamental
  dp : int = None  # Depreciation and Amortization - Index Fundamental
  dpc : int = None  # Depreciation and Amortization - Statement of Cash Flows - Index Fundamental
  dv : int = None  # Cash Dividends - Annual Index Fundamental Cash Flow
  dvp : int = None  # Preferred Cash Dividends - Index Fundamental
  epsfi : int = None  # Earnings Per Share (Diluted) - Including Extraordinary items
  epsfx : int = None  # Earnings Per Share (Diluted) - Excluding Extraordinary items
  epspi : int = None  # Earnings Per Share - Including Extraordinary Items - Index Fundamental
  epspx : int = None  # Earnings Per Share - Excluding Extraordinary Items - Index Fundamental
  fincf : int = None  # Financing Activities - Net Cash Flow - Index Fundamental
  ib : int = None  # Income Before Extraordinary Items - Index Fundamental
  ibadj : int = None  # Income Before Extraordinary Items - Adjusted for Common Stock Equivalents - Index Fundamental
  ibcom : int = None  # Income Before Extraordinary Items - Available for Common - Index Fundamental
  icapt : int = None  # Invested Capital - Total - Index Fundamental
  intan : int = None  # Intangibles
  invt : int = None  # Inventory - Total - Index Fundamental
  itcb : int = None  # Investment Tax Credit - Balance Sheet - Index Fundamental
  ivaeq : int = None  # Investments and Advancements at Equity
  ivncf : int = None  # Investing Activities - Net Cash Flow - Index Fundamental
  lco : int = None  # Current Liabilities - Other - Index Fundamental
  lct : int = None  # Current Liabilities - Total - Index Fundamental
  lo : int = None  # Liabilities - Other - Index Fundamental
  lt : int = None  # Liabilities - Total - Index Fundamental
  mib : int = None  # Noncontrolling Interest (Balance Sheet)
  mibn : int = None  # Noncontrolling Interests - Nonredeemable - Balance Sheet - Index Fundamental
  mibt : int = None  # Noncontrolling Interests - Total - Balance Sheet - Index Fundamental
  mii : int = None  # Noncontrolling Interest (Income Account)
  ni : int = None  # Net Income - Index Fundamental
  nopi : int = None  # Nonoperating Income - Index Fundamental
  np : int = None  # Notes Payable
  oancf : int = None  # Operating Activities - Net Cash Flow - Index Fundamental
  oiadp : int = None  # Operating Income After Depreciation - Index Fundamental
  oibdp : int = None  # Operating Income Before Depreciation - Index Fundamental
  opeps : int = None  # Earnings Per Share from Operations - Index Fundamental
  opepsx : int = None  # Earnings Per Share (Diluted) from Operations
  pi : int = None  # Pretax Income - Index Fundamental
  ppent : int = None  # PP&E Total - Net - Index Fundamental
  pstk : int = None  # Preferred Stock - Index Fundamental
  re : int = None  # Retained Earnings - Index Fundamental
  rect : int = None  # Receivables - Total - Index Fundamental
  sale : int = None  # Sales - Index Fundamental
  seq : int = None  # Stockholders Equity - Parent
  spi : int = None  # Special Items - Index Fundamental
  sppe : int = None  # Sale of Property, Plant, and Equipment - Index Fundamental
  sstk : int = None  # Sale of Stock - Index Fundamental
  teq : int = None  # Stockholders Equity > Total > Index Fundamental
  tstk : int = None  # Treasury Stock - Total - Index Fundamental
  txdb : int = None  # Deferred Taxes - Balance Sheet - Index Fundamental
  txditc : int = None  # Deferred Taxes and Investment Tax Credit - Index Fundamental
  txp : int = None  # Income Taxes Payable - Index Fundamental
  txr : int = None  # Income Tax Refund - Index Fundamental
  txt : int = None  # Income Taxes - Total - Index Fundamental
  xacc : int = None  # Accrued Expenses - Index Fundamental
  xint : int = None  # Interest Expense - Index Fundamental
  xsga : int = None  # Selling, General, and Administrative Expenses - Index Fundamental
  datadate : int = None  # Data Date - Index Annual


  @staticmethod
  def from_name(conm):
    return super(IdxFdmtAnn, IdxFdmtAnn).from_attr(IdxFdmtAnn, 'conm', conm)

  @staticmethod
  def from_gvkeyx(gvkeyx):
    return super(IdxFdmtAnn, IdxFdmtAnn).from_attr(IdxFdmtAnn, 'gvkeyx', gvkeyx, exact=True)


@attr.s(auto_attribs=True)
class IdxFdmtQrt(WRDSEntity):
  schema = 'comp'
  table = 'idx_qrt'
  gvkeyx : str = None  # Global Index Key - Index Quarterly
  acoq : int = None  # Current Assets - Other - Index Fundamental - Quarterly
  actq : int = None  # Current Assets - Total - Index Fundamental -Quarterly
  aoq : int = None  # Assets - Other - Index Fundamental - Quarterly
  apq : int = None  # Accounts Payable - Index Fundamental - Quarterly
  atq : int = None  # Assets - Total - Index Fundamental - Quarterly
  capsq : int = None  # Capital Surplus - Index Fundamental -Quarterly
  capxqx : int = None  # Capital Expenditures - Index Fundamental - Quarterly
  ceqq : int = None  # Common Equity - Total - Index Fundamental - Quarterly
  cheq : int = None  # Cash and Equivalents - Index Fundamental - Quarterly
  cogsq : int = None  # Cost of Goods Sold - Index Fundamental - Quarterly
  cstkeq : int = None  # Common Stock Equivalents - Dollar Savings - Index Fundamental - Quarterly
  cstkq : int = None  # Common Stock - Index Fundamental -Quarterly
  dlcq : int = None  # Debt in Current Liabilities - Index Fundamental - Quarterly
  dlttq : int = None  # Long Term Debt - Total - Index Fundamental - Quarterly
  dpq : int = None  # Depreciation and Amortization - Index Fundamental - Quarterly
  dvpq : int = None  # Preferred Cash Dividends - Index Fundamental - Quarterly
  epsfiq : int = None  # Earnings Per Share (Diluted) - Including Extraordinary items - Quarterly
  epsfxq : int = None  # Earnings Per Share (Diluted) - Excluding Extraordinary items - Quarterly
  epspiq : int = None  # Earnings Per Share - Including Extraordinary Items - Index Fundamental - Quarterly
  epspxq : int = None  # Earnings Per Share - Excluding Extraordinary Items - Index Fundamental - Quarterly
  epsx12 : int = None  # Earnings Per Share - 12 Months Moving
  ibadjq : int = None  # Income Before Extraordinary Items - Adjusted for Common Stock Equivalents - Index Fundamental - Quarterly
  ibcomq : int = None  # Income Before Extraordinary Items - Available for Common - Index Fundamental - Quarterly
  ibq : int = None  # Income Before Extraordinary Items - Index Fundamental -Quarterly
  icaptq : int = None  # Invested Capital - Total - Index Fundamental - Quarterly
  invtq : int = None  # Inventory - Total - Index Fundamental - Quarterly
  lcoq : int = None  # Current Liabilities - Other - Index Fundamental - Quarterly
  lctq : int = None  # Current Liabilities - Total - Index Fundamental - Quarterly
  loq : int = None  # Liabilities - Other - Index Fundamental - Quarterly
  ltq : int = None  # Liabilities - Total - Index Fundamental - Quarterly
  mibnq : int = None  # Noncontrolling Interests - Nonredeemable - Balance Sheet - Index Fundamental
  mibq : int = None  # Noncontrolling Interest - Redeemable - Balance Sheet
  mibtq : int = None  # Noncontrolling Interests - Total - Balance Sheet - Index Fundamental
  miiq : int = None  # Noncontrolling Interest - Income Account
  niq : int = None  # Net Income - Index Fundamental - Quarterly
  nopiq : int = None  # Nonoperating Income - Index Fundamental - Quarterly
  oepsxq : int = None  # Earnings Per Share (Diluted) from Operations - Quarterly
  oiadpq : int = None  # Operating Income After Depreciation - Index Fundamental - Quarterly
  oibdpq : int = None  # Operating Income Before Depreciation - Index Fundamental - Quarterly
  opepsq : int = None  # Earnings Per Share from Operations - Index Fundamental - Quarterly
  piq : int = None  # Pretax Income - Index Fundamental - Quarterly
  ppentq : int = None  # PP&E Total - Net - Index Fundamental - Quarterly
  pstkq : int = None  # Preferred Stock - Index Fundamental - Quarterly
  rectq : int = None  # Receivables - Total - Index Fundamental - Quarterly
  req : int = None  # Retained Earnings - Index Fundamental - Quarterly
  saleq : int = None  # Sales - Index Fundamental - Quarterly
  seqq : int = None  # Stockholders Equity > Parent > Index Fundamental > Quarterly
  spiq : int = None  # Special Items - Index Fundamental - Quarterly
  teqq : int = None  # Stockholders Equity > Total > Index Fundamental > Quarterly
  tstkq : int = None  # Treasury Stock - Total - Index Fundamental - Quarterly
  txditq : int = None  # Deferred Taxes and Investment Tax Credit - Index Fundamental - Quarterly
  txpq : int = None  # Income Taxes Payable - Index Fundamental - Quarterly
  txtq : int = None  # Income Taxes - Total - Index Fundamental - Quarterly
  xintq : int = None  # Interest Expense - Index Fundamental - Quarterly
  xsgaq : int = None  # Selling, General, and Administrative Expenses - Index Fundamental - Quarterly
  datadate : int = None  # Data Date - Index Quarterly

  @staticmethod
  def from_gvkeyx(gvkeyx):
    return super(IdxFdmtQrt, IdxFdmtQrt).from_attr(IdxFdmtQrt, 'gvkeyx', gvkeyx, exact=True)


@attr.s(auto_attribs=True)
class IdxMth(WRDSEntity):
  schema = 'comp'
  table = 'idx_mth'
  gvkeyx : str = None  # Global Index Key - Index Monthly
  ajexm : int = None  # Adjustment Factor
  bkvlps : int = None  # Book Value Per Share - Index
  cshtrm : int = None  # Common Shares Traded
  dvpsxm : int = None  # Dividend Per Share - Index
  dvrate : int = None  # Indicated Annual Dividend
  epsx12 : int = None  # Earnings Per Share - 12MM - Index
  prccm : int = None  # Index Price - Close Monthly
  prccmdiv : int = None  # Index Value - Total Return Monthly
  prccmdivn : int = None  # Index Value - Total Return Net Monthly
  prccmdivnusd : int = None  # Index Value - Total Return Net Monthly - US Dollars
  prccmdivusd : int = None  # Index Value - Total Return Monthly - US Dollars
  prccmhdgaud : int = None  # Index Value - Close Monthly - Australian Dollar
  prccmhdgeur : int = None  # Index Value - Close Monthly - EUR
  prccmhdggbp : int = None  # Index Value - Close Monthly - British Pound
  prccmhdgjpy : int = None  # Index Value - Close Monthly - Japanese Yen
  prccmhdgusd : int = None  # Index Value - Close Monthly - US Dollars
  prccmusd : int = None  # Index Price - Close Monthly - US Dollars
  prchm : int = None  # Index Price - High Monthly
  prclm : int = None  # Index Price - Low Monthly
  datadate : int = None  # Data Date - Index Monthly

  @staticmethod
  def from_gvkeyx(gvkeyx):
    return super(IdxMth, IdxMth).from_attr(IdxMth, 'gvkeyx', gvkeyx, exact=True)


@attr.s(auto_attribs=True)
class IdxDaily(WRDSEntity):
  schema = 'comp'
  table = 'idx_daily'
  gvkeyx : str = None  # Global Index Key - Index Daily
  dvpsxd : int = None  # Index Daily Dividends
  newnum : int = None  # Index Number - New
  oldnum : int = None  # Index Number - Old
  prccd : int = None  # Index Price - Close Daily
  prccddiv : int = None  # Index Value - Total Return
  prccddivn : int = None  # Index Value - Total Return - Net Dividends
  prchd : int = None  # Index Price - High Daily
  prcld : int = None  # Index Price - Low Daily
  datadate : int = None  # Data Date - Index Daily

  @staticmethod
  def from_gvkeyx(gvkeyx):
    return super(IdxDaily, IdxDaily).from_attr(IdxDaily, 'gvkeyx', gvkeyx, exact=True)

