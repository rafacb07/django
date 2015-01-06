import datetime

class Calendar(object):
    date = ''
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    def __init__(self, date):
        # Force the date to be an instance of datetime.date
        if not isinstance(date, datetime.date):
            raise TypeError("date must be a datetime")
        self.date = date

    def get_date(self):
        return self.date

    def get_week_days(self):
        formatted_days = []
        week_days = [self.date + datetime.timedelta(days=i) for i in range(0 - self.date.weekday(), 7 - self.date.weekday())]
        for day_index in xrange(7):
            day = self.days_of_week[day_index]+', '+week_days[day_index].strftime("%B-%d-%Y")
            formatted_days.append(day)
        return formatted_days


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