import os

if os.getcwd().split('\\')[-1] == 'osdan':
    import defaults
else:
    from osdan import defaults

from calendar import monthrange


def year_and_month_gen(start_time, end_time):

    if start_time.day == 1 and start_time.hour == 0 and start_time.minute == 0:
        if start_time.month == 1:
            start_time = start_time.replace(month=12)
            start_time = start_time.replace(year=start_time.year - 1)
        else:
            start_time = start_time.replace(month=start_time.month - 1)

    end_year = end_time.year
    start_year = start_time.year
    for year in range(start_year, end_year + 1):
        if year == end_year:
            end_month = end_time.month
        else:
            end_month = 12
        if year == start_year:
            start_month = start_time.month - 1
        else:
            start_month = 0
        for month in defaults.months[start_month:end_month]:
            yield str(year), month, None, None


def year_month_day_index_gen(start_time, end_time):

    end_year = end_time.year
    start_year = start_time.year

    for year in range(start_year, end_year + 1):
        if year == end_year:
            end_month = end_time.month
        else:
            end_month = 12
        if year == start_year:
            start_month = start_time.month - 1
        else:
            start_month = 0

        for month in defaults.months[start_month:end_month]:
            for day in range(1, monthrange(int(year), int(month))[1] + 1):
                if ((day < start_time.day and int(month) == start_time.month and year == start_year)
                        or (day > end_time.day and int(month) == end_time.month and year == end_year)):
                    continue
                for hour in range(23, -1, -1):
                    if (hour < start_time.hour and int(month) == start_time.month and year == start_year
                        and start_time.day == day) \
                            or (hour > end_time.hour  and int(month) == end_time.month and year == end_year and
                                end_time.day == day):
                        continue
                    for minute in range(55, -1, -5):
                        index = str(hour).zfill(2) + str(minute).zfill(2)
                        yield str(year), month, str(day).zfill(2), index