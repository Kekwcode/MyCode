import datetime
import calendar

x = datetime.datetime(int(input("Enter your birth Year: ")), int(input("Enter your birth Month: ")),
                      int(input("Enter first Date: ")))

print(calendar.day_name[x.weekday()])
