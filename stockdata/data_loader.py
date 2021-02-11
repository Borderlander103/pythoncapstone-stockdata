import csv
import dateutil.parser
from pathlib import Path

resources_folder = Path(__file__).absolute().parent
# resources_folder = Path("resources/")
csv_path = resources_folder / 'stocks.csv'
rows = []


class Data_Loader:

    def main(self):
        self.import_csv()
        self.clean_data()
        self.convert_dates()
        return rows

    def import_csv(self):
        with open(csv_path, 'r') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=',')
            next(csvreader)
            for row in csvreader:
                rows.append(row)

    def clean_data(self):
        for row in rows:
            for index, col in enumerate(row):
                if col == '':
                    row[index] = None

    def convert_dates(self):
        for index, row in enumerate(rows):
            # index 7 is the date column
            if row[7] == None:
                continue
            rows[index][7] = str(dateutil.parser.parse(row[7]).date())
