import report_creator
import filters
import settings
from interface import welcome, main_menu, save_menu
from data_loader import Data_Loader
from stock_model import StockData

main_menu = main_menu.Main_Menu()
save_menu = save_menu.Save_Menu()


class App:

    def __init__(self):
        self.populate_stocks()
        welcome.welcome()
        self.app()

    def app(self):
        main_menu.main_menu()
        filters.filter_stocks()
        self.populate_stock_values()
        self.generate_report()
        save_menu.save_menu()

    def populate_stocks(self):
        data_loader = Data_Loader()
        rows = data_loader.main()
        for row in rows:
            settings.stocks.append(StockData(row))

    def populate_stock_values(self):
        for stock in settings.filtered_stocks:
            settings.stock_values.append(float(stock.price))

    def generate_report(self):
        reports = report_creator.Report_Creator()
        reports.print_report()


# dev stuff
App()

# for stock in stocks[:5]:
#     print(stock.__dict__)
