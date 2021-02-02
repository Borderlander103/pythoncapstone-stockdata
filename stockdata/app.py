from data_loader import Data_Loader
from stock_model import StockData
import interface
import settings
import filters
import report_creator

interface = interface.Interface()


class App:

    def __init__(self):
        self.populate_stocks()
        interface.welcome()
        interface.main_menu()
        filters.filter_stocks()
        self.populate_stock_values()
        report_creator.generate_report()

    def populate_stocks(self):
        data_loader = Data_Loader()
        rows = data_loader.main()
        for row in rows:
            settings.stocks.append(StockData(row))

    def populate_stock_values(self):
        for stock in settings.filtered_stocks:
            # numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            # for stock in numbers:
            # print(stock.industry, stock.price)
            print('hi')
            # settings.stock_values.append(float(stock.price))
            print(stock)


# dev stuff
App()

# for stock in stocks[:5]:
#     print(stock.__dict__)
