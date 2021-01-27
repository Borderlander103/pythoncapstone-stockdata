import csv
import dateutil.parser
from pathlib import Path
from stock_model import StockData

data_folder = Path("resources/")
csv_path = data_folder / 'stocks.csv'
rows = []
stocks = []


class Data_Loader:
    def __init__(self):
        print("hello world")
        import_csv()
        clean_data()
        convert_dates()
        populate_stocks()

    def import_csv():
        with open(importfile, 'r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader)
        for row in csvreader:
            rows.append(row)

    def clean_data():
        for row in rows:
            for index, col in enumerate(row):
                if col == '':
                    row[index] = None

    def convert_dates():
        for index, row in enumerate(rows):
            # index 7 is the date column
            if row[7] == None:
                continue
            rows[index][7] = str(dateutil.parser.parse(row[7]).date())

    def populate_stocks()
    for row in rows:
            stocks.append(StockData(row))


x = Data_Loader()
