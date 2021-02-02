import statistics
import settings
from analysis_utils import Analysis_Utils


class Report_Creator(Analysis_Utils):

    def __init__(self, ) -> None:
        super().__init__()
        self.headline = f"\n\n\nStock Report for the {settings.key.title()} '{settings.value}':\n"
        self.average_val = "Average Value: ${:,.2f}".format(
            self.average(settings.stock_values), 2)
        self.median_val = "Median Value: ${:,.2f}".format(
            self.median(settings.stock_values), 2)
        self.min_val = "Minimum Value: ${:,.2f}".format(
            self.max_min(settings.stock_values)[1])
        self.max_val = "Maximum Value: ${:,.2f}".format(
            self.max_min(settings.stock_values)[0], 2)

    def print_report(self):
        print(self.headline)
        print(self.average_val)
        print(self.median_val)
        print(self.min_val)
        print(self.max_val)
        # print(settings.key,
        #       settings.value, settings.currency)
        # print((max(settings.stock_values), min(settings.stock_values)))
        # print(min(settings.stock_values))
        # print(max(settings.stock_values))
        # print(sum(settings.stock_values)/len(settings.stock_values))
        # print(statistics.median(settings.stock_values))
