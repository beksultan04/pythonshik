from datetime import datetime, date, timedelta

GIGASECOND = 10**9

def add(moment):
    """
    Return the moment exactly one gigasecond (1_000_000_000 seconds) later.
    Accepts a datetime.datetime or datetime.date and returns a datetime.datetime.
    """
    if isinstance(moment, datetime):
        return moment + timedelta(seconds=GIGASECOND)
    if isinstance(moment, date):
        # convert date to datetime at midnight (naive)
        dt = datetime(moment.year, moment.month, moment.day)
        return dt + timedelta(seconds=GIGASECOND)
    raise TypeError("moment must be a datetime.datetime or datetime.date")
