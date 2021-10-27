num=int(input())
if num==1:
        print('1/2')
        quit()
for i in range(1,num*2):
    n=0
    if i%4==0:
        n=" + "
    else:
        n=" - "
    if i%2!=0 and i!= ((int(num*2)-1)):
        print(i,"/",sep="",end="")
    elif i==(num*2)-1:
        print(i,"/",i+1,sep="")
    elif i%2==0:
        print(i,n,sep="",end="")