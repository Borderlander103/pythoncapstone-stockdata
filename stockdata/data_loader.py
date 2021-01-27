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


x = Data_Loader()
