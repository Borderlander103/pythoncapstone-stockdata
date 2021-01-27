from data_loader import Data_Loader
from stock_model import StockData

stocks = []

print("pre-load")


class StockDataApp:

    print("pre-init")

    def __init__(self):
        print("init 1")
        self.populate_stocks()
        print("init 2")

    def populate_stocks(self):
        data_loader = Data_Loader()
        rows = data_loader.main()
        for row in rows:
            stocks.append(StockData(row))
        print("populate_stocks ran")


StockDataApp()
print('app ran')

# x = Data_Loader()
# x.main()
# print("data loader ran")
print(stocks[:5])
for stock in stocks[:5]:
    print(stock.__dict__)
