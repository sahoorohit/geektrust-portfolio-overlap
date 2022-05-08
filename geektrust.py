import sys
from enum import Enum

from constants import Operations
from market import Market


def show(output):
    if isinstance(output, Enum):
        print(output.value)

    elif isinstance(output, list):
        for overlap in output:
            print(overlap)


def main():
    input_file = sys.argv[1]

    with open(input_file) as file:
        lines = file.readlines()

    market = Market()
    for line in lines:
        line = line.rstrip()
        words = line.split()

        output = None
        operation = words[0]
        if operation == Operations.CURRENT_PORTFOLIO.value:
            market.set_user_current_portfolio(funds_list=words[1:])
        elif operation == Operations.CALCULATE_OVERLAP.value:
            output = market.calculate_overlap(fund=words[1])
        elif operation == Operations.ADD_STOCK.value:
            output = market.add_stock_to_fund(fund_name=words[1], stock_name=" ".join(words[2:]))

        show(output)


if __name__ == "__main__":
    main()
