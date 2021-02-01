from data_loader import Data_Loader
from stock_model import StockData
import interface

interface = interface.Interface()
stocks = []
selected_stock = []
key = None
value = None
currency = None


class Main:

    def __init__(self):
        self.populate_stocks()
        interface.welcome()
        self.populate_values(interface.main_menu)

    def populate_stocks(self):
        data_loader = Data_Loader()
        rows = data_loader.main()
        for row in rows:
            stocks.append(StockData(row))

    def populate_values():
        self.key = input[0]
        self.value = input[1]
        self.currency = input[2]


# dev stuff
Main()

# for stock in stocks[:5]:
#     print(stock.__dict__)
