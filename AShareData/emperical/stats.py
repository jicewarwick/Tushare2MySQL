import math

import pandas as pd

from AShareData.date_utils import SHSZTradingCalendar

DAYS_IN_YEAR = 365


def annual_return(prices: pd.Series):
    dates = prices.index.get_level_values('DateTime')
    days = (dates[-1].date() - dates[0].date()).days
    pct_change = prices[-1] / prices[0]
    years = days / DAYS_IN_YEAR
    return pow(pct_change, 1 / years) - 1


def annual_volatility(prices: pd.Series):
    dates = prices.index.get_level_values('DateTime')
    cal = SHSZTradingCalendar()
    date_index = cal.select_dates(start_date=dates[0], end_date=dates[-1])
    prices = prices.droplevel('ID').reindex(date_index).interpolate()
    return prices.pct_change().std() * math.sqrt(DAYS_IN_YEAR)


def sharpe_ratio(prices: pd.Series):
    return annual_return(prices) / annual_volatility(prices)
