import math
x = float(input())
cosh= math.cosh(x)
exp= 1/2*(math.exp(x)+math.exp(-x))
e =  1/2 * (math.e**(x)+math.e**(-x))
print("COS =",f"{cosh:.4f}")
print("EXP =",f"{exp:.4f}")
print("E =",f"{e:.4f}")