birth = {'year': 1990, 'month': 2, 'day': 10}
current = {'year': 1991, 'month': 2, 'day': 10}
months = {'Jan': 31, 'Feb': 28, 'Mar': 31, 'Apr': 30, 'May': 31, 'Jun': 30, 'Jul': 31, 'Aug': 31, 'Sep': 30, 'Oct': 31, 'Nov': 30, 'Dec': 31}
monthKeys = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

def howOld(birth, current):
    totalDays = 0

    ##adds the full years inbetween year of birth and current year
    yearsDiff = current['year'] - birth['year'] - 1
    if yearsDiff > 0:
        totalDays += yearsDiff * 365
    print totalDays

    ##adds full months inbetween birth month and end of the year
    mon = birth['month']
    while mon < 12:
        totalDays += months[monthKeys[mon]]
        mon += 1
    print totalDays

    ##adds full months from the beginning of the year to the current month minus 1
    for mon in range((current['month'] - 1)):
        totalDays += months[monthKeys[mon]]
    print totalDays

    ##adds days from current month and from the birth month
    totalDays += (months[monthKeys[(birth['month'] - 1)]] - birth['day'] + 1)
    totalDays += current['day']
    print totalDays

    # ##accounts for leap years
    # days = totalDays
    # leapDays = (totalDays / 365) / 4
    # totalDays += leapDays
    # print totalDays

    ## breaks total days down into years
    totalYears = totalDays / 365
    leftoverDays = totalDays % 365


    print "I am %d days old. AKA %d years and %d days old." %(totalDays, totalYears, leftoverDays)

howOld(birth, current)
