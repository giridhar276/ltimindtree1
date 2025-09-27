############################# working with date and time ####################
import time

# todays time in epoch time
print(time.time())

print(time.ctime())

# time.strftime( string formatted time)
# %d will display date
# %b will display Month
# %Y will display yyyy
# %y will display yy format
print(time.strftime("%d")) # date
print(time.strftime("%b")) # month
print(time.strftime("%Y")) # yyyy fomrat
print(time.strftime("%y")) # year

import datetime
print(datetime.datetime.fromtimestamp(time.time()).strftime("%Y-%m-%d %H:%M:%S"))

import calendar
print(calendar.month(2025,9))
print(calendar.calendar(2025))
