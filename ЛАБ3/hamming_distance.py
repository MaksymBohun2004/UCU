x, y = input().split()
x=int(x)
y=int(y)
m=x^y
hamming_weight=bin(m).count("1")
print(hamming_weight)