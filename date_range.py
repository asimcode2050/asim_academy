# https://youtu.be/hpfJHfjyUkw
from datetime import timedelta, date

def get_date_range(start,end):
    return [start + timedelta(n) for n in range(int((end-start).days))]

print(get_date_range(date(2021,10,1), date(2021,10,5)))

