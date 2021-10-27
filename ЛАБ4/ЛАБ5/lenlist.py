def pickingNumbers(a):
    mainlist = []
    for i in a:
        timedlist = []
        num = a.index(i)
        if i != a[-1]:
            if (int(i) - int(a[num + 1]) in range(0,1) or int(a[num+1]) - int(i)) in range(0,1):
                timedlist.append(i)
                timedlist.append(a[num+1])
        if len(timedlist) > len(mainlist):
            mainlist = timedlist
        else:
            continue
    lengh = int(len(mainlist))
    return lengh
print(pickingNumbers([4, 6, 5, 3, 3, 1]))
