
days_this_year = int(input("How many days are in this year?"))

days_in_one_year = 365
days_in_one_leapyear = days_in_one_year + 1
hours_in_one_day = 24
minutes_in_one_hour = 60
seconds_in_one_minute = 60

seconds_minute_hours = hours_in_one_day * minutes_in_one_hour * seconds_in_one_minute

result = days_in_one_year * seconds_minute_hours

leap_year_result = days_in_one_leapyear * seconds_minute_hours


if days_this_year == 366:
  print("Number of seconds in a leap year are", leap_year_result)
elif days_this_year == 365:
  print("Number of seconds in a year are", result)
else:
    print(f"Number of seconds in a year with {days_this_year} days are", seconds_minute_hours * days_this_year)