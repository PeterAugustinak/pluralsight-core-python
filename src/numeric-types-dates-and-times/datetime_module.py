"""Working with datetime module"""
import datetime

"""DATE"""
date1 = datetime.date(2022, 1, 25)
date2 = datetime.date(year=2022, day=26, month=1)
today = datetime.date.today()

print(date1)
print(date2)
print(today)

# relative
timestamp = datetime.date.fromtimestamp(1000000000)
ordinal = datetime.date.fromordinal(720669)

print(timestamp)
print(ordinal)

# attrs of date
print(today.year, today.month, today.day)
# weekday 0-6
print(today.weekday())
# weekday 1-7
print(today.isoweekday())

# isoformat
print(today.isoformat())
# strf format
print(today.strftime('%A %d %B %Y'))

# min
print(datetime.date.min)
# max
print(datetime.date.max)
# resolution
print(datetime.date.resolution)


"""TIME"""
print()
time1 = datetime.time(3, 1, 2, 232)
time2 = datetime.time(hour=23, minute=59, second=59, microsecond=999999)

print(time1)
print(time2)

# attrs
print(time1.hour)
print(time1.minute)
print(time1.second)
print(time1.microsecond)

# isoformat
print(time1.isoformat())
# strf format
print(time1.strftime('%Hh%Mm%Ss'))
print(f'{time1.hour}-{time1.min}-{time1.second}')

# min
print(datetime.time.min)
# max
print(datetime.time.max)
# resolution
print(datetime.time.resolution)


"""COMBINE DATE AND TIMES"""
print()
# to avoid confusion use:
# from datetime import datetime as Datetime
# import datetime as dt
# or use full name as follows
datetime1 = datetime.datetime(2022, 1, 25, 18, 54, 32)
now = datetime.datetime.today()
# now with timezone support
now_tz = datetime.datetime.now()
# UTC standard time instead of local machine
now_utc = datetime.datetime.utcnow()

print(datetime1)
print(now)
print(now_tz)
print(now_utc)

# combine datetime objects
d = datetime.date.today()
t = datetime.time(20, 00)
comb = datetime.datetime.combine(d, t)

print(d)
print(t)
print(comb)

# extraction
print(comb.date())
print(comb.time())
print(comb.weekday())


"""DURATIONS"""
print()
# use always keywords args, even if not necessary
td1 = datetime.timedelta(milliseconds=1, microseconds=1000)
print(td1)

td2 = datetime.timedelta(weeks=1, minutes=2, milliseconds=5500)
print(td2)

td3 = datetime.timedelta(days=8, seconds=125, microseconds=500000)
print(td3.days)
print(td3.seconds)
print(td3.microseconds)
print(repr(td3))

# arithmetic
today = datetime.datetime.today()
yesterday = datetime.datetime(2022, 1, 24) # if not specified, it is 00:00:00
diff = today - yesterday
print(diff)

# datetime - timedelta
del1 = datetime.timedelta(days=1)
yesterday_exact = today - del1
print(yesterday_exact)

day_diff_exact = today - yesterday_exact
print(day_diff_exact)

# adding
three_weeks_from_now = datetime.datetime.now() + datetime.timedelta(weeks=3)
print(three_weeks_from_now)


"""TIMEZONES"""
print()
cet = datetime.timezone(datetime.timedelta(hours=1))
print(cet)

departure = datetime.datetime(year=2022, month=1, day=26, hour=11,
                              minute=30, tzinfo=cet)
arrival = datetime.datetime(year=2022, month=1, day=26, hour=13,
                              minute=5, tzinfo=datetime.timezone.utc)
duration = arrival - departure
print(duration)

# other timezone support utils:
#pytz, dateutil
