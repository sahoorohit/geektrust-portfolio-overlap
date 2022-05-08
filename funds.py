from typing import List


class Fund:
    def __init__(self, name: str):
        self.name = name
        self.stocks = []

    def add_stock(self, stock_name: str):
        self.stocks.append(stock_name)

    def add_stocks(self, stocks_list: List[str]):
        for stock in stocks_list:
            self.add_stock(stock_name=stock)

    @property
    def stocks_count(self) -> int:
        return len(self.stocks)
