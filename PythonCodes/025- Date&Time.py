# ------------------------------- Date and Time -------------------------------
import datetime

# print current date and time
print(datetime.datetime.now())                  # 2024-01-31 22:24:23.790772
print(datetime.datetime.now().year)             # 2024
print(datetime.datetime.now().month)            # 1
print(datetime.datetime.now().day)              # 31
print(datetime.datetime.now().time())           # 22:24:23.792696
print(datetime.datetime.now().time().hour)      # 22
print(datetime.datetime.now().time().minute)    # 24
print(datetime.datetime.now().time().second)    # 23

# print start and end of date
print(datetime.datetime.min)                    # 0001-01-01 00:00:00
print(datetime.datetime.max)                    # 9999-12-31 23:59:59.999999

# prnit spesific date
print(datetime.datetime(2003, 9, 21))           # 2003-09-21 00:00:00

# time left
daybefor = datetime.datetime(2024, 1, 4, 19, 36)
daynow = datetime.datetime.now()
print(daynow - daybefor)                        # 27 days, 22:35:02.608801

# -------------------------------- Date Format --------------------------------
# click link: "https://strftime.org"

daynow = datetime.datetime.now()

print(daynow.strftime("%a"))                    # Wed
print(daynow.strftime("%A"))                    # Wednesday

print(daynow.strftime("%b"))                    # Jan
print(daynow.strftime("%B"))                    # January

print(daynow.strftime("%y"))                    # 24
print(daynow.strftime("%Y"))                    # 2024

print(daynow.strftime("%c"))                    # Wed Jan 31 23:01:49 2024