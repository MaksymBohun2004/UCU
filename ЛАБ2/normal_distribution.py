import math
from math import pi, e 
x= float(input())
m= float(input())
o= float(input())
f=(1/(2*pi*o**2)**0.5)*e**(-(x-m)**2/(2*o**2))
f_round=round(f,10)
print(f_round)