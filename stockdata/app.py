from data_loader import Data_Loader
from stock_model import StockData
import interface
import settings
import filters

interface = interface.Interface()
# stocks = []
# selected_stock = []
# key = None
# value = None
# currency = None


class Main:

    def __init__(self):
        self.populate_stocks()
        interface.welcome()
        # self.populate_values(interface.main_menu)
        interface.main_menu()
        filters.filter_stocks()

    def populate_stocks(self):
        data_loader = Data_Loader()
        rows = data_loader.main()
        for row in rows:
            settings.stocks.append(StockData(row))

    def populate_stock_values(self):
        for stock in settings.filtered_stocks:
            settings.stock_values.append(float(stock.price))


# dev stuff
Main()

# for stock in stocks[:5]:
#     print(stock.__dict__)
