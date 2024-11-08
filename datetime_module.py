import datetime
current_datetime=datetime.datetime.now()
print(f"current date and time is : {current_datetime}")

curr_date=datetime.date.today()
print(f"current date is : {curr_date}")

spec_date=datetime.date(2024,11,15)
spec_time=datetime.time(2,30,45)
print(f"specific date and time is :{spec_date},{spec_time}")

formated_datetime=current_datetime.strftime("%Y-%m-%d %H:%M:%S")
print(f"formatted datetime is :{formated_datetime}")