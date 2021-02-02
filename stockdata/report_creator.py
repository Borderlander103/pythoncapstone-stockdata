import settings


class Report_Creator(Analysis_Utils):

    def __init__(self):
        Analysis_Utils.__init__(self)

    def generate_report(self):
        print(settings.stock_values, settings.key,
              settings.value, settings.currency)
