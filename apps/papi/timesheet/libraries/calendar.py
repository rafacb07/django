import datetime

class Calendar(object):
    date = ''

    def __init__(self, date):
        # Force the date to be an instance of datetime.date
        if not isinstance(date, datetime.date):
            raise TypeError("date must be a datetime")
        self.date = date

    def get_date(self):
        return self.date

    def get_week_days(self):
        return [self.date + datetime.timedelta(days=i) for i in range(0 - self.date.weekday(), 7 - self.date.weekday())]

    def set_date(self, date):
        # Force the date to be an instance of datetime.date
        if not isinstance(date, datetime.date):
            raise TypeError("date must be a datetime")
        self.date = date
        return self.date

    def set_next_previous_week(self, next = True):
        if next:
            self.date = self.date + datetime.timedelta(days=7)
        else:
            self.date = self.date - datetime.timedelta(days=7)
        return self.date

    def to_string(self, date = None):
        if not date:
            return self.date.strftime("%Y-%m-%d %H:%M:%S")
        return date.strftime("%Y-%m-%d %H:%M:%S")