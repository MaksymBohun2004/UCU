from typing import List


try:
    starting_number = int(input())
    size = int(input())
except ValueError:
    print("Incorrect Value")
numbers = []
for i in range(-100,100):
    i = int(i)
    numbers.append(i)
string = size
number_of_strings = size
list_starting_number = int(starting_number+100)
list_size = int(list_starting_number+size)
timed_starting_number=starting_number
listt=[]
for i in range(list_starting_number,list_size):
    n=(numbers[i])
    listt.append(n)
    timed_starting_number-=1
    list_size-=1
newlist_size=size
t=newlist_size
for i in range(1,newlist_size+1):
    print(*listt[:t])
    t-=1