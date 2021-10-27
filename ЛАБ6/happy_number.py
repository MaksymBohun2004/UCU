def happy_number(number):
    """
    >>> happy_number(12345)
    False
    >>> happy_number(43211234)
    True
    """
    number = str(number)
    sum1 = 0
    sum2 = 0
    if len(number) < 8:
        number = number.zfill(8)
    iteration = 0
    for i in str(number):
        iteration += 1
        if iteration <= 4:
            sum1 += int(i)
        else:
            sum2 += int(i)
    if sum1 == sum2:
        return True
    else:
        return False

def count_happy_numbers(n):
    """
    >>> count_happy_numbers(4321)
    1
    """
    happy_numbers_list = []
    for number in range(0, n+1):
        number = str(number)
        sum1 = 0
        sum2 = 0
        if len(number) < 8:
            number = number.zfill(8)
        iteration = 0
        for i in str(number):
            iteration += 1
            if iteration <= 4:
                sum1 += int(i)
            else:
                sum2 += int(i)
        if sum1 == sum2:
            happy_numbers_list.append(int(number))
    return len(happy_numbers_list)

def happy_numbers(m, n):
    """
    >>> happy_numbers(43211234,43211324)
    [43211234, 43211243, 43211252, 43211261, 43211270, 43211306, 43211315, 43211324]
    """
    happy_numbers_list = []
    for number in range(m, n+1):
        number = str(number)
        sum1 = 0
        sum2 = 0
        if len(number) < 8:
            number = number.zfill(8)
        iteration = 0
        for i in str(number):
            iteration += 1
            if iteration <= 4:
                sum1 += int(i)
            else:
                sum2 += int(i)
        if sum1 == sum2:
            happy_numbers_list.append(int(number))
    return happy_numbers_list
# if __name__ == "__main__":
#     print(doctest.testmod())