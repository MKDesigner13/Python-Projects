def add_time(start, duration, day_of_week=''):

    #Set input start values
    print('Start time: ' + start + ' ' + day_of_week.lower().capitalize())
    print('Plus: ' + duration)
    start_time_colon_index = start.find(':')
    start_hr = int(start[:start_time_colon_index])
    start_min = int(start[start_time_colon_index + 1:start_time_colon_index + 3])
    total_start_minutes = (start_hr * 60) + start_min
    weekday = day_of_week.lower().capitalize()

    #Check for AM/PM
    am_pm = start[start_time_colon_index + 4:]
    is_am = True if am_pm == 'AM' else False
    total_start_minutes = total_start_minutes if is_am else total_start_minutes + 720

    #Set input duration values
    duration_colon_index = duration.find(':')
    duration_hr = int(duration[:duration_colon_index])
    duration_min = int(duration[duration_colon_index + 1:duration_colon_index + 3])
    total_duration_minutes = (duration_hr * 60) + duration_min

    #Add time values
    new_total_minutes = total_start_minutes + total_duration_minutes

    #Split new total minutes into hr and min
    new_hr = new_total_minutes // 60
    new_min = new_total_minutes - (new_hr * 60)

    #Check for days past and AM/PM
    days_past = 0
    while new_hr > 23:
        new_hr -= 24
        days_past += 1
        am_pm = 'AM'
    if new_hr > 11:
        new_hr -= 12
        am_pm = 'PM'
    if new_hr == 0:
        new_hr = 12

    #Format minute
    if new_min < 10:
        new_min = '0' + str(new_min)
    else:
        new_min = str(new_min)

    #Format new_time
    new_time = ''
    if days_past > 1:
        new_time = str(new_hr) + ':' + new_min + ' ' + am_pm + f' ({days_past} days later)'
    elif days_past == 1:
        new_time = str(new_hr) + ':' + new_min + ' ' + am_pm + ' (next day)'
    else:
        new_time = str(new_hr) + ':' + new_min + ' ' + am_pm

    #Check for weekday
    weekday_list = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    
    if weekday:
        weekday_index = weekday_list.index(weekday)
        if days_past > 0:
            weekday_index += days_past
            new_weeks = weekday_index // 7
            weekday = weekday_list[weekday_index - (new_weeks * 7)]
        am_pm_index = new_time.find('M')
        new_time = new_time[:am_pm_index + 1] + f', {weekday}' + new_time[am_pm_index + 1:]
    
    #Return statement
    print("New time: ", new_time)
    
    return new_time

add_time('8:16 PM', '60:02', 'saturday')

"""
Arguments(Starting-time, Time to add(hh:mm), starting-day)
"""

