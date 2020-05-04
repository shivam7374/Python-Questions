import random
import time

def str_time_prop(start, end, format, prop):


    stime = time.mktime(time.strptime(start, format))
    etime = time.mktime(time.strptime(end, format))

    ptime = stime + prop * (etime - stime)

    return time.strftime(format, time.localtime(ptime))


def random_date(start, end, prop):
    return str_time_prop(start, end, '%m/%d/%Y %I:%M %p', prop)

print(random_date("1/1/2016 1:30 PM", "3/23/2018 4:50 AM", random.random()))