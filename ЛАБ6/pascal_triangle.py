
def generate_pascal_triangle(number):
    """
    Returns a list of n lists that represents a Pascal triangle

    >>> generate_pascal_triangle(5)
    [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
    """
    if isinstance(number,int) == False or number <= 0 :
        return []
    lst = [[0 for i in range(number)]
              for j in range(number)]
    for line in range (0, number):
        for pascal in range (0, line + 1):
            if pascal == 0 or pascal == line:
                lst[line][pascal] = 1
            else:
                lst[line][pascal] = (lst[line - 1][pascal - 1] +
                                lst[line - 1][pascal])
    jlist = [-1 for minus1 in range(0,number)]
    for remove0s in range(0,len(lst[0]) -1):
        for fromthelist in jlist:
            if lst[remove0s][fromthelist] == 0:
                lst[remove0s].remove(lst[remove0s][fromthelist])
    return lst
