import datetime


# converts a datetime time to number of hours as a float
def time_to_num(time):
    if type(time) != datetime.time:
        raise TypeError('Function parameter must be a datetime time')
    else:
        hours = time.hour
        minutes = time.minute
        seconds = time.second
        num = hours + minutes / 60 + seconds / 3600
        return num
