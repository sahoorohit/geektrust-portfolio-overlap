from enum import Enum


class Responses(Enum):
    FUND_NOT_FOUND = "FUND_NOT_FOUND"


class Operations(Enum):
    CURRENT_PORTFOLIO = "CURRENT_PORTFOLIO"
    CALCULATE_OVERLAP = "CALCULATE_OVERLAP"
    ADD_STOCK = "ADD_STOCK"


STOCKS_DATA_FILE = "stock_data.json"
ZERO_PERCENT = float(0.0)
