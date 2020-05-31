import datetime

def to_string(datetime_object):
    return datetime.datetime.strftime(datetime_object, '%a %d %b %Y')

print('\nWelcome to Lockdown Counter\n')

lockdown_start = datetime.date(2020, 3, 24)
today = datetime.date.today()
total_days = today - lockdown_start +datetime.timedelta(days=1)

print("UK Lockdown start: {}".format(to_string(lockdown_start)))
print("Today: {}".format(to_string(today)))
print("This is day {}\n".format(total_days.days))

print("\n---PHASE 1---")
for day in range(1,total_days.days+1):
    lockdown_date = lockdown_start+datetime.timedelta(days=day-1)
    if lockdown_date.day == 1:
        print () # separate the months
    if lockdown_date == datetime.date(2020, 4, 8):
        print("\n\n---PHASE 2---")
    if lockdown_date == datetime.date(2020, 5, 11):
        print("\n\n---PHASE 3---")
    print("DAY {} : {}".format(day, to_string(lockdown_date)))