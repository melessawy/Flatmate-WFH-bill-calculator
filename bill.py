import datetime
import calendar

class Bill:
    """
    an object that holds monthly bill data
    """

    def __init__(self, amount):
        self.amount = amount
        self.current_date = datetime.date.today()
        self.days_in_month = calendar.monthrange(self.current_date.year, self.current_date.month)[1]
