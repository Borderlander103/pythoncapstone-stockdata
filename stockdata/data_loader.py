import csv
import dateutil.parser
from pathlib import Path

data_folder = Path("resources/")
csv_path = data_folder / 'stocks.csv'
rows = []


class Data_Loader:

    # data_folder = Path("resources/")
    # csv_path = data_folder / 'stocks.csv'
    # rows = []

    # def run_data_loader(self):
    #     import_csv()
    #     clean_data()
    #     convert_dates()
    #     print("hello world")
    #     print(rows[:5])

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

    def main(self):
        self.import_csv()
        self.clean_data()
        self.convert_dates()
        print("hello world")
        print(rows[:5])


x = Data_Loader()
print(x)
x.main()
