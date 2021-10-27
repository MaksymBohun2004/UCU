try:
    n = int(input())
except ValueError:
    print("Incorrect Value")
    quit()
numbers = []
for i in range(-1,101):
    if i % 2 != 0: 
        numbers.append(i)
listt=[]
for i in numbers:
    m=(i)
    m+=2
    a=(i+1)
    a+=2
    b=(i+2)
    b+=2
    c=(i+3)
    c+=2
    slash="/"
    minus=" - "
    plus=" + "
    if m > 2:
        m=m+2
    if a > 2:
        a=a+2
    if b > 4:
        b=b+2
    if c > 4:
        c=c+2
    if m > 6:
        m=m+2
    if a > 6:
        a=a+2
    if b > 8:
        b=b+2
    if c > 9:
        c=c+2
    if m > 10:
        m=m+2
    if a > 10:
        a=a+2
    if b > 12:
        b=b+2
    if c > 12:
        c=c+2
    if m > 14:
        m=m+2
    if a > 14:
        a=a+2
    if b > 16:
        b=b+2
    if c > 16:
        c=c+2
    listt.append(m)
    listt.append(slash)
    listt.append(a)
    listt.append(minus)
    listt.append(b)
    listt.append(slash)
    listt.append(c)
    listt.append(plus)
    
fg=(n+((3*n)-1))
if (n>1):
    print(*listt[:fg],sep="")
else:
    print(*listt[:3],sep="")