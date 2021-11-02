import datetime
import calendar as calendaR

def calendar(year,month):
    vertiCal = []
    cal = calendaR.Calendar(0)
    for i in cal.itermonthdays2( year, month ):
        if i[0] == 0:
            continue
        else:
            if   i[1] == 0:
                theday = "mon"
            elif i[1] == 1:
                theday = "mue"
            elif i[1] == 2:
                theday = "wed"
            elif i[1] == 3:
                theday = "thu"
            elif i[1] == 4:
                theday = "fri"
            elif i[1] == 5:
                theday = "sat"
            elif i[1] == 6:
                theday = "sun"
            else:
                print ("Error: Day of week is not between 0 and 6.")
            theday += " "
            theday += str(i[0])
            vertiCal.append(theday)
    for day in vertiCal:
        day = day.split()
        

    out = "The calendar is:"
    out = out.center(15)
    print (out)
    for item in vertiCal: print (item)
calendar(2021,5)