import json
from enum import Enum
from typing import List, Optional, Union

from constants import STOCKS_DATA_FILE, Responses
from funds import Fund
from portfolio import Portfolio


class Market:

    def __init__(self):
        self.all_funds = []
        self.initialize_all_funds()

        self.portfolio = Portfolio()

    def initialize_all_funds(self):
        with open(STOCKS_DATA_FILE) as stocks_data_file:
            stocks_data = json.load(stocks_data_file)

        for fund in stocks_data.get('funds'):
            _fund = Fund(name=fund.get('name'))
            _fund.add_stocks(stocks_list=fund.get('stocks'))

            self.all_funds.append(_fund)

    def fund_exists(self, fund_name: str) -> Optional[Fund]:
        _fund = None
        for fund in self.all_funds:
            if fund.name == fund_name:
                _fund = fund
                break

        return _fund

    def add_stock_to_fund(self, fund_name: str, stock_name: str) -> Optional[Enum]:
        fund = self.fund_exists(fund_name=fund_name)
        if not fund:
            return Responses.FUND_NOT_FOUND

        fund.add_stock(stock_name=stock_name)

    def set_user_current_portfolio(self, funds_list: List):
        for fund_name in funds_list:
            fund = self.fund_exists(fund_name=fund_name)
            if fund:
                self.portfolio.add_fund(fund=fund)

    def calculate_overlap(self, fund: str) -> Union[Enum, List[str]]:
        fund = self.fund_exists(fund_name=fund)
        if not fund:
            return Responses.FUND_NOT_FOUND

        overlap = []
        for user_fund in self.portfolio.user_funds:
            common_stocks = set(fund.stocks) & set(user_fund.stocks)
            overlap_percentage = (2 * len(common_stocks) * 100) / (fund.stocks_count + user_fund.stocks_count)
            overlap_percentage = round(overlap_percentage, 2)
            overlap.append(f'{fund.name} {user_fund.name} {overlap_percentage}')

        return overlap
