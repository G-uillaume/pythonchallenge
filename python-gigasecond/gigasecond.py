import datetime
import time

def add_gigasecond(time):
    try:
        assert type(time) is datetime.datetime
        gs = datetime.timedelta(
            seconds=10**9
        )
        return time + gs
    except AssertionError:
        return "Argument's type must be of datetime.datetime"