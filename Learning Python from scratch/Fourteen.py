import datetime, time, calendar, decimal

print(datetime.datetime.today())
print(datetime.datetime.today()-datetime.timedelta(days=6))
print(datetime.datetime.today().timetuple())
print(time.mktime(datetime.datetime.today().timetuple()))
print(datetime.datetime.fromtimestamp(1584611616.0))
print(datetime.datetime.now())
print(datetime.date.today())
print(time.mktime(datetime.date.today().timetuple()))
print(calendar.calendar(2039))
print(calendar.isleap(1300))
print(time.localtime())
print(decimal.Decimal("0.1"))

