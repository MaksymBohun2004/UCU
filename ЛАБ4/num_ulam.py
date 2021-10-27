# ****************************************
# Problem 24
# ****************************************
def numbers_Ulam(n):
    """
    Return a list that consists of n Ulam numbers, starting from 1. 
    Ulam number is a number that is the smallest whole
    number that: 
    1. Is a sum of two numbers that are already in the list.
    2.  Can only be found in one way.
    3. Is larger than the biggest number in the list.
    >>> numbers_Ulam(10)
    [1, 2, 3, 4, 6, 8, 11, 13, 16, 18]
    >>> numbers_Ulam(2)
    [1, 2]
    >>> numbers_Ulam(1)
    [1]
    """
    timedlist = [1,2]
    mainlist = []
    for i in range (3,1000):
        count = 0
        for j in range(len(timedlist)-1):
            for k in range(j+1,len(timedlist)):
                if timedlist[j] + timedlist[k] == i:
                    count += 1
                if count > 1:
                    break
            if count > 1: break
        if count == 1:
            timedlist.append(i)
    for i in range(0,n):
        mainlist.append(timedlist[i])
    print(mainlist)
    return mainlist
numbers_Ulam(100)