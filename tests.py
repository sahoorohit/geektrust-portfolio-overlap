import copy
import unittest
from typing import List

from constants import Responses
from funds import Fund
from market import Market


class TestMarket(unittest.TestCase):

    def setUp(self) -> None:
        self.market = Market()

    def get_funds_name_list(self, funds: List[Fund]) -> List[str]:
        return [fund.name for fund in funds]

    def test_add_fund_to_portfolio_when_fund_not_exists(self):
        funds = ["invalid-fund"]
        self.market.set_user_current_portfolio(funds_list=funds)
        self.assertEqual(self.market.portfolio.user_funds, [])

    def test_add_single_fund_to_portfolio(self):
        funds = ["ICICI_PRU_NIFTY_NEXT_50_INDEX"]
        self.market.set_user_current_portfolio(funds_list=funds)
        self.assertEqual(self.get_funds_name_list(self.market.portfolio.user_funds), funds)

    def test_add_multiple_funds_to_portfolio(self):
        funds = ["ICICI_PRU_NIFTY_NEXT_50_INDEX", "UTI_NIFTY_INDEX"]
        self.market.set_user_current_portfolio(funds_list=funds)
        self.assertEqual(self.get_funds_name_list(self.market.portfolio.user_funds), funds)

    def test_calculate_overlap(self):
        self.test_add_single_fund_to_portfolio()
        output = self.market.calculate_overlap(fund="UTI_NIFTY_INDEX")
        expected_output = ["UTI_NIFTY_INDEX ICICI_PRU_NIFTY_NEXT_50_INDEX 20.37%"]
        self.assertEqual(output, expected_output)

    def test_calculate_overlap_when_overlap_is_100_percent(self):
        self.test_add_single_fund_to_portfolio()
        output = self.market.calculate_overlap(fund="ICICI_PRU_NIFTY_NEXT_50_INDEX")
        expected_output = ["ICICI_PRU_NIFTY_NEXT_50_INDEX ICICI_PRU_NIFTY_NEXT_50_INDEX 100.00%"]
        self.assertEqual(output, expected_output)

    def test_add_stock_when_fund_not_exists(self):
        fund = "invalid-fund"
        output = self.market.add_stock_to_fund(fund_name=fund, stock_name="NOCIL")
        self.assertEqual(output, Responses.FUND_NOT_FOUND)

    def test_add_stock_when_fund_exists(self):
        fund = "ICICI_PRU_NIFTY_NEXT_50_INDEX"

        fund_obj = self.market.fund_exists(fund_name=fund)
        fund_stocks_before_operation = copy.deepcopy(fund_obj.stocks)

        stock = "NOCIL"
        output = self.market.add_stock_to_fund(fund_name=fund, stock_name=stock)
        self.assertIsNone(output)

        self.assertEqual(fund_stocks_before_operation + [stock], fund_obj.stocks)
