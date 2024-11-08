#datetime module
import datetime

# 1 # display current date time

datetime_today=datetime.datetime.now()
# print(datetime_today.date())
# print(datetime_today.time())

# 2 # dispaly exact or formatted date and time

formatdate=datetime_today.strftime("%Y-%m-%d")
formattime=datetime_today.strftime("%H:%M:%S")
# print(formatdate)
# print(formattime)

# 3 # display welcome msg based on time

# curr_hour=datetime_today.hour
# if 0<=curr_hour<=12:
#     print("good morning")
# elif 13<=curr_hour<=16:
#     print("good afternoon")
# else:
#     print("good evening")