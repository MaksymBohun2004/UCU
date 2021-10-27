try:
    x=int(input())
except ValueError:
    print("Error")
    quit()
list=[]
list_of_prime=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
if x<=2:
    print("Error")
    quit()
    
for i in range(1,x):
     if i in list_of_prime and (x%i)!=0:
        list.append(i)
print(list[0]) 
     