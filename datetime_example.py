#Datetime module : it represents date and time in python. It has many classes and methods to work with date and time.   

#Example:
import datetime
date = datetime.date(2025,1,2)#printing date in YYYY-MM-DD format
print(date)
today = datetime.date.today()#printing today's date
print(today)
time = datetime.time(12,30,45)#printing time in HH:MM:SS format
print(time)
now = datetime.datetime.now()#printing current date and time
print(now)
now = now.strftime("%Y-%m-%d %H:%M:%S")#printing current date and time in YYYY-MM-DD HH:MM:SS format
print(now)
