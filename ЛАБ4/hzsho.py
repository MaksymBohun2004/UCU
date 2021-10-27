a, b, c =input('Enter three numbers: ')
if a > b:
    if b > c:
        print( "Допоможіть будь ласка!", end = " ")
    else:
        print( "Все було чудово!", end = " ")
elif b > c:
    print( "Каву будь ласка,", end = " ")
    if a >= c:
        print( "чорну.", end = " ")
    elif a < b:
        print( "з молоком.", end = " ")
    elif c == b:
        print( "без цукру.", end = " ")
else:
    print( "Чай будь ласка,", end = " ")
    if a == b:
        print( "з цукром.", end = " ")
    else:
        print( "з молоком.", end = " ")
print( "Дякую")