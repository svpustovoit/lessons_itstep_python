import datetime
'''
date_time = datetime.datetime(2026,
                              3,
                              7,
                              hour=16,
                              minute=17,
                              second=34,
                              microsecond=584)
print(f"object datetime:\n\t{date_time}")
print(f"method date:\n\t{date_time.date()}")
print(f"type(date_time):\n\t{type(date_time.date())})")
print(f"method time:\n\t{date_time.time()}")
print(f"type(time):\n\t{type(date_time.time())}")

print()

date_1 = datetime.date(2026, 3,7)
time_1 = datetime.time(16, 30, 45,1582)
print(f"date: {date_1}, \ntype date: {type(date_1)}")
print(f"time: {time_1}, \ntype time: {type(time_1)}")

date_time_2 = datetime.datetime.combine(date_1, time_1)
print(f"date: {date_time_2}, \ntype date: {type(date_time_2)}")

print(f"new date: {date_time_2.replace(2020,10, 25)}")
print(f"date_time_2: {date_time_2}")  # !!!!

x = date_time_2.replace(2020,10, 25)
print(f"x: {x}")

date_now = datetime.datetime.now()
print(f"date_now: {date_now}")

date_today = datetime.datetime.today()
print(f"date_today: {date_today}")

date_date_today = datetime.date.today()
print(f"date_date_today: {date_date_today}")

print(f"time now: {date_now.time()}")

print(f"weekday(): {date_now.weekday()}")
print(f"isoweekday(): {date_now.isoweekday()}")

date_now = datetime.datetime.now()
time_stamp = date_now.timestamp()
print(f"time_stamp: {time_stamp}")
print(f"fromtimestamp(): {date_now.fromtimestamp(time_stamp)}")
'''
date_now = datetime.datetime.now()
print(f"date_time to str: {date_now.strftime('%d/%m/%Y  %H:%M:%S')}")
print(f"date to str: {date_now.strftime('%d_%m_%Y %A %B')}")
print(f"time to str: {date_now.strftime('%H.%M.%S')}")

date_now = datetime.datetime.now()
print(f"date_now:{date_now}")
delta = datetime.timedelta(days = 20,
                           hours =16,
                           weeks=5)
print(f"delta: {delta}")
date_future = date_now + delta
print(date_future)
print(f"day week: {date_future.strftime('%A')}")




