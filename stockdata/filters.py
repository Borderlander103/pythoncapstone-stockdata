import settings


def filter_stocks(self):
    if settings.key == 'name':
        settings.selected_stock = filter(
            filters.nameFilter, settings.filtered_stocks)
    elif settings.key == 'industry':
        settings.selected_stock = filter(
            filters.industryFilter, settings.filtered_stocks)
    elif settings.key == 'market':
        settings.selected_stock = filter(
            filters.marketFilter, settings.filtered_stocks)
    else:
        print("You shouldn't get here.")


def nameFilter(stock):
    if(stock.name == settings.key):
        return True
    else:
        return False


def industryFilter(stock):
    if(stock.industry == settings.key):
        return True
    else:
        return False


def marketFilter(stock):
    if(stock.market == settings.key):
        return True
    else:
        return False
