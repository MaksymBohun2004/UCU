num=str(input())
list_of_g = []
lengh=len(num)
for i in range(0, len(num), 1):
    list_of_g.append(int(num[i : i + 1]))

if lengh == 3:
    g0=list_of_g[2]
    g1=list_of_g[1]
    g2=list_of_g[0]
    b2=g2
    b1=g2^g1
    b0=b1^g0
    print(b2,b1,b0, sep="")
elif lengh == 4:
    g0=list_of_g[3]
    g1=list_of_g[2]
    g2=list_of_g[1]
    g3=list_of_g[0]
    b3=g3
    b2=g3^g2
    b1=b2^g1
    b0=b1^g0
    print(b3,b2,b1,b0, sep="")
elif  lengh == 5:
    g0=list_of_g[4]
    g1=list_of_g[3]
    g2=list_of_g[2]
    g3=list_of_g[1]
    g4=list_of_g[0]
    b4=g4
    b3=g4^g3
    b2=b3^g2
    b1=b2^g1
    b0=b1^g0
    print(b4,b3,b2,b1,b0, sep="")
elif  lengh == 6:
   g0=list_of_g[5]
   g1=list_of_g[4]
   g2=list_of_g[3]
   g3=list_of_g[2]
   g4=list_of_g[1]
   g5=list_of_g[0]
   b5=g5
   b4=g5^g4
   b3=b4^g3
   b2=b3^g2
   b1=b2^g1
   b0=b1^g0
   print(b5,b4,b3,b2,b1,b0, sep="")