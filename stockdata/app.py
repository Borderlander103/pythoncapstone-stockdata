from data_loader import Data_Loader
from stock_model import StockData
import interface

interface = interface.Interface()
stocks = []
key = None
value = None
currency = None


class Main:

    def __init__(self):
        self.populate_stocks()
        interface.welcome()
        input = interface.main_menu()
        self.key = input[0]
        self.value = input[1]
        self.currency = input[2]
        print(self.key, self.value, self.currency)

    def populate_stocks(self):
        data_loader = Data_Loader()
        rows = data_loader.main()
        for row in rows:
            stocks.append(StockData(row))


# dev stuff
Main()

# for stock in stocks[:5]:
#     print(stock.__dict__)
