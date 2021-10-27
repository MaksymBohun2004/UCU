import calendar
import daytime
def total_occurrences(s1, s2, ch):
    """
    (str, str, str) -> int
    Precondition: len(ch) == 1
    Return the total number of times that ch occurs in s1 and s2.
    >>> total_occurrences('color', 'yellow', 'l')
    3
    >>> total_occurrences('red', 'blue', 'l')
    1
    >>> total_occurrences('green', 'purple', 'b')
    0
    """
    return s1.count(ch) + s2.count(ch)

def dyvo_insert(sentence, flag):
    """
    (str, str) -> str
    Inserting word "диво" before every word that starts with flag.
    >>> dyvo_insert("Кит кота по хвилях катав - кит у воді, кіт на киті","ки")
    'дивокит кота по хвилях катав - дивокит у воді, кіт на дивокиті'
    >>> dyvo_insert("Корова їла сіно, коти бігали подвір'ям","ко")
    "дивокорова їла сіно, дивокоти бігали подвір'ям"
    >>> dyvo_insert("Основи програмування - надзвичайно цікавий предмет!", "пр")
    'основи дивопрограмування - надзвичайно цікавий дивопредмет!'
    """
    sent1 = ("диво" + flag).join(sentence.lower().split(flag))
    return sent1

import calendar
def semester_calendar(output_type, year, first_month, last_month):
    r""" (str, int, int, int) -> str
    Generates a text calendar or an html one that displays all days of the week
    from the month that you picked to be the first one to
    the last one
    >>> semester_calendar("html",2021,2,3) #doctest: +ELLIPSIS
    '<table border="0" cellpadding="0" cellspacing="0"...'
    >>> (semester_calendar("txt",2021,2,3) #doctest: +ELLIPSIS
    '   February 2021...'
    """
    if output_type == "txt":
        mycalendar = ""
        for i in range(first_month, last_month+1):
            mycalendar = mycalendar + calendar.month(year,i)
    elif output_type == "html":
        mycal = ""
        mycalendar = ""
        for i in range(first_month, last_month+1):
            mycal = calendar.HTMLCalendar(year)
            mycal = mycal.formatmonth(year,i)
            mycalendar = mycalendar + mycal
    return mycalendar
print(semester_calendar("txt",2021,2,3))