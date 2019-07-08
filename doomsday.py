## Doomsday Algorithm used to be able to display specific day of the week for date given.
## Neat stuff.
## in question. All date inputs must be Anno Domini (AD).
## By Alex Sahinidis
## Last Edited: 7/8/19

import sys
from datetime import date


if len(sys.argv) != 4:
    print("""------------

    This script requires exactly 3 arguments. First, the month, then the day, then the year.

    i.e., python doosmday.py 5 19 2000

    ------------""")
    exit()


month = int(sys.argv[1])
day = int(sys.argv[2])
year = int(sys.argv[3])

# Determines whether year inputted is a leap year or not.
leap = False
if float(year) % 4 == 0:
    if float(year) % 100 == 0:
        if float(year) % 400 == 0:
            leap = True
        else:
            leap = False
    else:
        leap = True

# Determines the maximum number of days for each month. Used to give user error if
# day of the month is invalid.
if leap == False:
    daysForEachMonth = dict([(1, 31), (2, 28), (3, 31), (4, 30), (5, 31), (6, 30),
                             (7, 31), (8, 31), (9, 30), (10,31), (11, 30), (12, 31)])
else:
    daysForEachMonth = dict([(1, 31), (2, 29), (3, 31), (4, 30), (5, 31), (6, 30),
                             (7, 31), (8, 31), (9, 30), (10,31), (11, 30), (12, 31)])

if  int(sys.argv[1]) < 1 or int(sys.argv[1]) > 12:
    print("""------------

    Please enter a real month.

    ------------""")
    exit()


if day > daysForEachMonth[month] or day < 1:
    print("""------------

    Please enter a real day.

    ------------""")
    exit()

## Calculating doomsday for given year.
lastTwoDigits = year % 1000
one = lastTwoDigits // 12
two = lastTwoDigits % 12
three = two // 4
if (year - lastTwoDigits) % 400 == 200:
    four = 5
elif (year - lastTwoDigits) % 400 == 300:
    four = 3
elif (year - lastTwoDigits) % 400 == 000:
    four = 2
elif (year - lastTwoDigits) % 400 == 100:
    four = 0
summation = one + two + three + four
yearDoomsday = summation % 7
## Now, we are going to create a dictionary with keys of months and values of day
## for the memorable dates of the year (also known as Doomsdays)
if leap == True:
    doomsdaysDict = dict([(1, 4), (2, 29), (3, 7), (4, 4),
                          (5, 9), (6, 6), (7, 11), (8, 8),
                          (9, 5), (10, 10), (11, 7),(12, 12)])
else:
    doomsdaysDict = dict([(1, 3), (2, 28), (3, 7), (4, 4),
                          (5, 9), (6, 6), (7, 11), (8, 8),
                          (9, 5), (10, 10), (11, 7), (12, 12)])
contestors = []
if month == 1:
    for doomsday in doomsdaysDict:
        if doomsday == month:
            contestors.append((doomsday, doomsdaysDict[doomsday]))
        if doomsday == 2:
            contestors.append((doomsday, doomsdaysDict[doomsday]))
        if doomsday == 12:
            contestors.append((doomsday, doomsdaysDict[doomsday]))
else:
    for doomsday in doomsdaysDict:
        if doomsday == month:
            contestors.append((doomsday, doomsdaysDict[doomsday]))
        if doomsday == ((month + 1) % 12):
            contestors.append((doomsday, doomsdaysDict[doomsday]))
        if doomsday == (month - 1):
            contestors.append((doomsday, doomsdaysDict[doomsday]))
ourDate = date(year, month, day)
referenceDay = date(year, contestors[0][0], contestors[0][1])
daysDifference = ourDate - referenceDay
daysDifference = daysDifference.days
finalAnswer = (yearDoomsday + daysDifference) % 7
if finalAnswer == 0:
    print("Sunday")
elif finalAnswer == 1:
    print("Monday")
elif finalAnswer == 2:
    print("Tuesday")
elif finalAnswer == 3:
    print("Wednesday")
elif finalAnswer == 4:
    print("Thursday")
elif finalAnswer == 5:
    print("Friday")
elif finalAnswer == 6:
    print("Saturday")
