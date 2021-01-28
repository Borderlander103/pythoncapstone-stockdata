from data_loader import Data_Loader
from stock_model import StockData
import interface

interface = interface.Interface()
stocks = []


class Main:

    def __init__(self):
        self.populate_stocks()
        interface.welcome()
        interface.main_menu()

    def populate_stocks(self):
        data_loader = Data_Loader()
        rows = data_loader.main()
        for row in rows:
            stocks.append(StockData(row))


# dev stuff
Main()

# for stock in stocks[:5]:
#     print(stock.__dict__)
