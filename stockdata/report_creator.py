import statistics
import settings
from analysis_utils import Analysis_Utils


class Report_Creator(Analysis_Utils):

    def __init__(self, ) -> None:
        super().__init__()
        self.headline = f"\n\n\nStock Report for the {settings.key.title()} '{settings.value}':\n"
        self.average_val = f"Average Value: {self.average(settings.stock_values)}"
        self.median_val = f"Median Value: {self.median(settings.stock_values)}"
        self.max_val = f"Maximum Value: {self.max_min(settings.stock_values)[0]}"
        self.min_val = f"Minimum Value: {self.max_min(settings.stock_values)[1]}"

    def print_report(self):
        print(self.headline)
        print(self.average_val)
        print(self.median_val)
        print(self.max_val)
        print(self.min_val)
        # print(settings.key,
        #       settings.value, settings.currency)
        # print((max(settings.stock_values), min(settings.stock_values)))
        # print(min(settings.stock_values))
        # print(max(settings.stock_values))
        # print(sum(settings.stock_values)/len(settings.stock_values))
        # print(statistics.median(settings.stock_values))
