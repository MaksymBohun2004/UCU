num=str(input())
list_of_b = []
lengh=len(num)
for i in range(0, len(num), 1):
    list_of_b.append(int(num[i : i + 1]))

if lengh == 3:
    b2=list_of_b[0]
    b1=list_of_b[1]
    b0=list_of_b[2]
    g0=b0^b1
    g1=b1^b2
    g2=b2
    print(g2,g1,g0, sep="")
elif lengh == 4:
    b3=list_of_b[0]
    b2=list_of_b[1]
    b1=list_of_b[2]
    b0=list_of_b[3]
    g0=b0^b1
    g1=b1^b2
    g2=b2^b3
    g3=b3
    print(g3,g2,g1,g0, sep="")
elif  lengh == 5:
    b4=list_of_b[0]
    b3=list_of_b[1]
    b2=list_of_b[2]
    b1=list_of_b[3]
    b0=list_of_b[4]
    g0=b0^b1
    g1=b1^b2
    g2=b2^b3
    g3=b3^b4
    g4=b4
    print(g4,g3,g2,g1,g0, sep="")
elif  lengh == 6:
    b5=list_of_b[0]
    b4=list_of_b[1]
    b3=list_of_b[2]
    b2=list_of_b[3]
    b1=list_of_b[4]
    b0=list_of_b[5]
    g0=b0^b1
    g1=b1^b2
    g2=b2^b3
    g3=b3^b4
    g4=b4^b5
    g5=b5
    print(g5,g4,g3,g2,g1,g0, sep="")