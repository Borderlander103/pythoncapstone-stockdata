import statistics
import time
import settings
from analysis_utils import Analysis_Utils


class Report_Creator(Analysis_Utils):

    def __init__(self, ) -> None:
        super().__init__()
        self.headline = f"Stock Report for the {settings.key.title()} '{settings.value}':\n"
        self.average_val = "Average Value: ${:,.2f}".format(
            self.average(settings.stock_values), 2)
        self.median_val = "Median Value: ${:,.2f}".format(
            self.median(settings.stock_values), 2)
        self.min_val = "Minimum Value: ${:,.2f}".format(
            self.max_min(settings.stock_values)[1])
        self.max_val = "Maximum Value: ${:,.2f}".format(
            self.max_min(settings.stock_values)[0], 2)

    def print_report(self):
        time.sleep(1)
        print(f"\n\nOkay, looking this up.")
        time.sleep(2)
        print("Give me a second...")
        time.sleep(3)
        print("\n\n\n-------------------")
        print(self.headline)
        print(self.average_val)
        print(self.median_val)
        print(self.min_val)
        print(self.max_val)
        print("-------------------\n\n")
        time.sleep(2)
        print("Press Enter for more options.")
        input()

    def save_report(self):
        print("save")
