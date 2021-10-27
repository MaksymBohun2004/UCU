guess=0
password="Maxx2004"
tries=int(3)
i=0
while guess!=password:
    print()
    guess=input("Enter password: ")
    print()
    i+=1
    tries-=1
    if guess==password:
        print()
        print("Welcome. You have used",(i-1),"tries.")
        print()
    elif tries==0:
        print()
        print("You're out of tries.")
        print()
        quit()
    elif guess!= password:
        print()
        print("Wrong password.",'You have',tries,"tries left.")
        print()