def add_time(start, duration, day_of_week=''):
    to_print = ''
    week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    class time:
        def __init__(self, hour, minutes):
            self.hour = int(hour)
            self.minutes = int(minutes)
    
    class StartTime(time):
        def __init__(self, hour, minutes, meridiem):
            super().__init__(hour, minutes)
            self.meridiem = 'AM' if meridiem == True else 'PM'
    
    starting_time = StartTime(start[0:start.index(':')], start[start.index(':') + 1:5], 'AM' in start)
    add_time = time(duration.split(':')[0], duration.split(':')[1])
    if starting_time.meridiem == 'PM':
        starting_time.hour += 12

    new_mins = starting_time.minutes + add_time.minutes
    extra_mins = 0
    if new_mins >= 60:
        extra_mins = new_mins // 60
        new_mins %= 60
    if len(str(new_mins)) == 1:
        new_mins = '0' + str(new_mins)

    extra_day = 0
    new_hour = starting_time.hour + add_time.hour + extra_mins
    if new_hour >= 24:
        extra_day = new_hour // 24
        new_hour %= 24
    print(extra_day)
    if new_hour == 0:
        new_hour += 12
        new_meridiem = 'AM'
    elif new_hour >= 12:
        if new_hour > 12:
            new_hour -= 12
        new_meridiem = 'PM'
    else:
        new_meridiem = 'AM'
    
    if day_of_week:
        week_number = week.index(day_of_week.title())
        new_week = []
        new_week.extend(week[week_number:])
        new_week.extend(week[0:week_number])
        week_number = 0
        week_number += extra_day
        print(new_week)
        if week_number > 6:
            print('before:', week_number)
            week_number %= 7
            print('after:', week_number)
    

    to_print += f'{new_hour}:{new_mins} {new_meridiem}'
    if day_of_week:
        to_print += f', {new_week[week_number].title()}'

    if extra_day > 1:
        to_print += f' ({extra_day} days later)'
    elif extra_day == 1:
        to_print += f' (next day)'


    return to_print




print(add_time("11:59 PM", "24:05", "Wednesday"))



