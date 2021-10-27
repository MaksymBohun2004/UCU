list=["SS","RR","PP","SR","RS","SP","PS","RP","PR"]
x = 0
while x!="":
    x=input()
    if x == "":
        quit()
    elif x==(list[0]) or x == (list[1]) or x == (list[2]):
         print("False | False")
    elif x==(list[3]) or x==(list[6]) or x==(list[7]):
         print("False")
    elif x==(list[4]) or x==(list[5]) or x==(list[8]):
         print("True")
