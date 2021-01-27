class StockData:
    # Contains data for an individual, imported stock.
    # Param: takes in "row" as a list of values from imported csv file.
    def __init__(self, row):
        self.id = row[0]
        self.name = row[1]
        self.price = row[2]
        self.symbol = row[3]
        self.industry = row[4]
        self.market = row[5]
        self.currency = row[6]
        self.date = row[7]
