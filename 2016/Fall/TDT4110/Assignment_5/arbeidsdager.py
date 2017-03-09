def is_leap_year ( year ):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    return False

weekdays = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

# a)
def weekday_newyear(year):
    sum_leap = 0
    for i in range(1900, year):
        if is_leap_year(i):
            sum_leap += 1
    day = (year - 1900 + sum_leap)%7
    return day

#for year in range(1900,1920):
#    print(year, weekdays[weekday_newyear(year)])


# b)
def is_workday(day):
    return 0<=day<5

# c)
def workdays_in_year(year):
    work=0
    weekday = weekday_newyear(year)
    for i in range(365 + is_leap_year(year)):
        if is_workday(weekday):
            work+=1
        weekday=(weekday+1)%7
    return(work)


for i in range(1900,1920):
    print(i,workdays_in_year(i))
