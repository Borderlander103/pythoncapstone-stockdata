import time
import datetime
import settings
from pathlib import Path
from analysis_utils import Analysis_Utils

report_name = 'stock_reports.txt'
output_folder = Path("output/")
report_file = output_folder / report_name


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
        time.sleep(3)
        print("Press Enter for more options.")
        input()

    def save_report(self):
        report = open(report_file, "a")
        report.write("\n\n\n_____________________________________________\n")
        report.write(f"\n{datetime.datetime.now()}\n")
        report.write("\n-------------------")
        report.write("\n" + self.headline)
        report.write("\n\n" + self.average_val)
        report.write("\n" + self.median_val)
        report.write("\n" + self.min_val)
        report.write("\n" + self.max_val)
        report.write("\n-------------------")
        report.close()
        time.sleep(2)
        print(f"\nThe report has been saved in '{report_name}'.")
        print("\nIt is located in here:")
        print(f"{Path().absolute()}\{output_folder}")
        time.sleep(2)
        print("\nPress Enter to return to the Main Menu.")
        input()

    def clear_report(self):
        self.headline = None
        self.average_val = None
        self.median_val = None
        self.min_val = None
        self.max_val = None
