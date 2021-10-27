# my first calc

print("Введіть цифру a:")
a= float(input())

print("Введіть цифру b:")
b= float(input())

print("Виберіть операцію")
print ("1 - додати а + b")
print ("2 - відняти а - b")
print ("3 - помножити а * b")
print ("4 - поділити а : b")
d= int(input())
if d==1 :
    print ("Cума a + b =", a+b)
if d==2 :
    print ("Різниця a - b =", a-b)
if d==3 : 
    print ("Добуток a * b =", a*b)
if d==4 :
    print ("Частка a : b =", a/b)
if d>4 or d<1 :
    print ("Помилка: Введіть число від 1 до 4.")
    d= int(input())
    if d==1 :
         print ("Cума a + b =", a+b)
    if d==2 :
          print ("Різниця a - b =", a-b)
    if d==3 : 
         print ("Добуток a * b =", a*b)
    if d==4 :
        print ("Частка a : b =", a/b)