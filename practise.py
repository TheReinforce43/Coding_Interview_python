from datetime import datetime,date,time  

dt=datetime(2011,10,29,20,30,21)
# print(dt.day)
# print(dt.month)
# print(dt.year)
# print(dt.date())
# print(dt.time())
# print(dt.datetime())
string_date=dt.strftime("%m-%d-%y %H:%M:%S")

# print(string_date)

date_to_string=datetime.strptime('2009-10-21','%Y-%m-%d')

print(date_to_string)