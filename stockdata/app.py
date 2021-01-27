from data_loader import Data_Loader
from stock_model import StockData

stocks = []


class StockDataApp:

    def __init__(self):
        self.populate_stocks()

    def populate_stocks(self):
        data_loader = Data_Loader()
        rows = data_loader.main()
        for row in rows:
            stocks.append(StockData(row))


StockDataApp()

for stock in stocks[:5]:
    print(stock.__dict__)
