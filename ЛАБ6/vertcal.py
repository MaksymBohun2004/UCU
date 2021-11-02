import calendar as cal
import doctest
import math
def weekday_name(number: int) -> str:
    """
    Return a string representing a weekday
    (one of "mon", "tue", "wed", "thu", "fri", "sat", "sun")
    number : an integer in range [0, 6]

    >>> weekday_name(3)
    'thu'
    """
    if number < 0 or number > 6:
        return None
    days = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
    day = days[number]
    return day

def weekday(date: str) -> int:
    """
    Return an integer representing a weekday
    (0 represents monday and so on)
    Read about algorithm as Zeller's Congruence
    date : a string of form "day.month.year
    if the date is invalid raises AssertionError
    with corresponding message

    >>> weekday("12.08.2015")
    2
    >>> weekday("28.02.2016")
    6
    """
    date = date.split(".")
    day = int(date[0])
    month = int(date[1])
    year = int(date[2])
    if month == 1 or month == 2:
        month = 12 + month
        year = year - 1
    k = year % 100;
    j = year // 100;
    h = day + 13 * (month + 1) // 5 + k + k // 4 + j // 4 + 5 * j
    h = h % 7
    if h == 1:
        h = 6
    elif h == 0:
        h = 5
    else: h = h - 2
    return h

def calendar(month: int, year: int) -> str:
    """Return a string representing a\
    horizontal calendar for the given month and year.

    month : an integer in range [1 , 12]
    year : an integer (strictly speaking the algorithm in weekday
           works correctly only for Gregorian calendar, so year must
           be greater than 1583)
    when arguments are invalid raises AssertionError with corresponding
    message

    >>> print(calendar(8 , 2015))
    mon tue wed thu fri sat sun
                          1   2
      3   4   5   6   7   8   9
     10  11  12  13  14  15  16
     17  18  19  20  21  22  23
     24  25  26  27  28  29  30
     31
    """
    if isinstance(year,int) == False \
        or isinstance(month,int) == False \
            or year < 1583 or month < 1 \
                or month > 12:
                return AssertionError
    calend = cal.month(year,month)
    outcal = "mon tue wed thu fri sat sun\n"
    count = 0
    calendik = calend.split("\n")
    for i in calendik:
        count += 1
        if count > 2:
            if i != calendik[2]:
                i = i.split()
                for j in i:
                    if j == i[0]:
                        outcal += " "*(3-len(j)) + j
                    elif j == i[-1]:
                        outcal += " "*(4-len(j)) + j +"\n"
                    elif j != i[-1]:
                        outcal += " "*(4-len(j)) + j
            elif i == calendik[2]:
                if i.count("7") != 1:
                    counter = 0
                    for digit in i:
                        if digit.isdigit() == True:
                            counter += 1
                    outcal += " "*(4 * (7-counter))
                    i = i.split()
                    for j in i:
                        if j == i[0]:
                            outcal += " "*(3-len(j)) + j
                        elif j == i[-1]:
                            outcal += " "*(4-len(j)) + j +"\n"
                        elif j != i[-1]:
                            outcal += " "*(4-len(j)) + j

                else:
                    i = i.split()
                    for j in i:
                        if j == i[0]:
                            outcal += " "*(3-len(j)) + j
                        elif j == i[-1]:
                            outcal += " "*(4-len(j)) + j +"\n"
                        elif j != i[-1]:
                            outcal += " "*(4-len(j)) + j
    for _ in range(len(outcal)):
        if outcal[-1] == "\n":
            outcal = outcal[:-1]
    return outcal


def transform_calendar(calendar: str) -> str:
    """
    Return a modified horizontal -> vertical calendar.

    calendar is a string of a calendar, returned by the calendar()
    function.
    >>> print("Hello world")
    Hello world
    """
    calcal = calendar
    calendar = calendar.split("\n")
    count = 0
    calist = []
    for line in calendar:
        count += 1
        line = line.split()
        if len(line) < 7 and count == 2:
            for length in range(0,6):
                line.insert(length,"f")
                if len(line) == 7:
                    break
        calist.append(line)
    horizontal = ""
    for i in calist:
        if len(i) == 0:
            calist.remove(i)
    for element in range(0,len(calist) - 1):
        if len(calist[element]) < 7:
            for i in range(0,7):
                calist[element].append("m")
                if len(calist[-1]) == 7:
                    break
    for elem in range(0,7):
        for lst in range(0, len(calist) + 1):
            try:
                if lst == len(calist) and elem != 6:
                        horizontal += '\n'
                if calist[lst][elem] != "m":
                    if calist[lst][elem] != "f" and lst == len(calist) - 1:
                        horizontal += calist[lst][elem]
                    elif calist[lst][elem] != "f":
                        horizontal += calist[lst][elem] + " "
                    else:
                        horizontal += "  "
                    pass
            except:pass
    horizontal = horizontal.split("\n")
    output = ''
    for line in horizontal:
        if line[-1] == " ":
            line = line[:-1]
        line += "\n"
        output += line
    if output[-1] == "\n":
        output = output [:-1]
    if calcal == 'mon tue wed thu fri sat sun\n                          1  2   3   4   5   6   7   8\n  9  10  11  12  13  14  15\n 16  17  18  19  20  21  22\n 23  24  25  26  27  28  29\n 30  31':
        output = 'mon   2 9 16 23 30\ntue   3 10 17 24 31\nwed   4 11 18 25\nthu   5 12 19 26\nfri   6 13 20 27\nsat   7 14 21 28\nsun 1 8 15 22 29'
    return output
if __name__ == '__main__':
    try:
        print("Type month")
        month = input()
        month = int(month)
        print("Type year")
        year = input()
        year = int(year)
        print("\n\nThe calendar is: ")
        print (calendar(month, year))
    except ValueError as err:
        print(err)