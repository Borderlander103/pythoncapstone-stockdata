import statistics


class Analysis_Utils:

    def max_min(self, values):
        return (max(values), min(values))

    def average(self, values):
        return sum(values)/len(values)

    def median(self, values):
        return statistics.median(values)

    def conver_currency(self, new_currency):
        pass
