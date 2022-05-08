from funds import Fund


class Portfolio:
    def __init__(self):
        self.user_funds = []

    def add_fund(self, fund: Fund):
        self.user_funds.append(fund)
