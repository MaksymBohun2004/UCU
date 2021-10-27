p=float(input())
r=float(input())
n=float(input())
t=float(input())
r_divby100=r/100
a=p*(1+(r_divby100/n))**(n*t)
print(a)
