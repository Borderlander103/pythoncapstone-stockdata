import csv
import dateutil.parser
from pathlib import Path
from .stock_model import StockData

data_folder = Path("resources/")
csv_path = data_folder / 'stocks.csv'
rows = []
stocks = []
