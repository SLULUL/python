import datetime
import calendar

today = datetime.date.today()
dates = [today + datetime.timedelta(days=i) for i in range(7)]

print("出发日期列表:")
print("  ".join(f"{date.day:2}" for date in dates))
print(" ".join(f"{calendar.day_abbr[date.weekday()]:3}" for date in dates))
