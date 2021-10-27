import random

number = int(input("How many numbers do you need to generate? "))
spectrum=int(input("Enter the number range (1 to x): "))

while True:
    if (number<=0) or (spectrum <= 0):
        print("Error: input an integer, number > 0")
        exit()
        
    else:
        
        num_list=[]
        for i in range(number):
            random_num=random.randrange(spectrum)
            num_list.append(random_num)
    print(num_list)
    break