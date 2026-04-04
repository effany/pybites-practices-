from datetime import datetime, timedelta

PYBITES_BORN = datetime(year=2016, month=12, day=19)


def gen_special_pybites_dates():
    day = PYBITES_BORN
    while True:
        day += timedelta(days = 100)
        yield day
        
    