import statistics
from currency_converter import CurrencyConverter


class Analysis_Utils:

    def __init__(self):
        converter = CurrencyConverter()

    def max_min(self, values):
        return (max(values), min(values))

    def average(self, values):
        return sum(values)/len(values)

    def median(self, values):
        return statistics.median(values)

    def conver_currency(self, value, new_currency):
        return self.converter.convert(value, 'USD', new_currency)
