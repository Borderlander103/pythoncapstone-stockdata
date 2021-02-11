import settings


def nameFilter(stock):
    if(stock.name == settings.value):
        return True
    else:
        return False


def industryFilter(stock):
    if(stock.industry == settings.value):
        return True
    else:
        return False


def marketFilter(stock):
    if(stock.market == settings.value):
        return True
    else:
        return False


def filter_stocks():
    if settings.key == 'name':
        settings.filtered_stocks = filter(
            nameFilter, settings.stocks)
    elif settings.key == 'industry':
        settings.filtered_stocks = filter(
            industryFilter, settings.stocks)
    elif settings.key == 'market':
        settings.filtered_stocks = filter(
            marketFilter, settings.stocks)
    else:
        print("You shouldn't get here.")
