import csv
import dateutil.parser
from pathlib import Path

data_folder = Path("resources/")
csv_path = data_folder / 'stocks.csv'
rows = []


class Data_Loader:

    print("data loader loaded")

    def main(self):
        self.import_csv()
        self.clean_data()
        self.convert_dates()
        print("data_loader main ran")
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


# x = Data_Loader()
# x.main()
print("data loader ran")
# print(rows[:5])
