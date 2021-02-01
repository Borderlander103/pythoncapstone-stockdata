import settings


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
