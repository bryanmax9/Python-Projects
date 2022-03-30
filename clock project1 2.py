# get values in hours
time_now = int(input("Enter the current time in military time: "))
wait_time = int(input("Enter the time for alarm: "))

#calculation

if wait_time > 24:      # identify if the value for wait_time is more than a day
    day_to_hours = wait_time // 24 # convert the day in hours with no minutes
    time_alarm_off = time_now + day_to_hours # add our current time with the hours
    exact_time = time_alarm_off - 12 # these calculation is to get the exact time

    if time_alarm_off >= 12:  # we need to identify if is in the afternoon or in the morning
        print(f"The alarm will get off at {time_alarm_off}:00 ({exact_time}:00 PM)")

    else:
        print(f"The alarm will get off at {time_alarm_off}:00 ({exact_time}:00 AM)")
    
    
else:  # if the amount of hours is less than the amount of hours in a day
    time_alarm_off = time_now + wait_time

    if time_alarm_off >= 12:
        exact_time = time_alarm_off - 12
        print(f"The alarm will get off at {time_alarm_off}:00 ({exact_time}:00 PM)")
    else:
        print(f"The alarm will get off at {time_alarm_off}:00 ({time_alarm_off}:00 AM)")
    



