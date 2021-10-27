num = int(input())
numb = bin(num)[2:]
count = 0
for i in range(1,len(numb)+1):
    if numb[0] == "1":
        count += 1
        numb = numb[1:]
    elif numb[0] == "0":
        numb = numb[1:]
        count += 1
print(count)
    
