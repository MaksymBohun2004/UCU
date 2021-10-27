import random
print()
print("Welcome to \"Gypsy\" by Maksym Bohun.")
print()
input('>>> Press Enter to continue ')
print()
print("\'Gypsy\' is a riddle game. In order to complete it, you will have to put your smartness and logical thinking to the test")
print()
input('>>> Press Enter to continue ')
print()
print("The rules are simple: all riddles have a one-word answer that doesn't include numbers or special symbols. P.S: don't take gypsy's predictions too seriously, she's just a lier.")
print()
name=0
while name!="": #Makes sure you only input a name that consists of letters
    name = input(">>> Enter your name to start: ")
    if name == "" or name.isalpha() == False :
        print()
        print("Your name must consist of atleast 1 letter. No special symbols or numbers allowed.")
        print()
        input(">>> Press Enter to continue")
        name=0
        print()
    elif name.isalpha() == True: #makes sure you only input letters
        print("Welcome, ",name,". Let's begin!",sep="")
        break
    

list_of_riddles= ['egg', "What has to be broken before you can use it?", "candle", "I'm tall when I'm young, and I’m short when I'm old. What am I?",'weights','What heavy seven letter word can you take two away from and be left with eight?',"tie","I am a word with two meanings. With one I can be broken, with the second I hold on. What am I?","dozens","A word I know, Six letters it contains, Subtract just one, And twelve is what remains.","short","What common English word becomes shorter when you add two letters?","incorrectly","What common 11-letter word is always spelled incorrectly?","firetruck","Name a word that starts with \"f\" and ends with \"u-c-k\"? (tip: you'll need it when your house is burning)","envelope","What word starts with E and ends with E and only has 1 letter in it?","alone","I am a solitary word, 5 letters long. Behead me, and I am still the same. Behead me again, and I am still the same.","me","who"]

def minigame(): # minigame where you have to guess a code
    print("minigame")

error_counter=0 
points=0
answer=0
while points<10:
    try:
        riddle_number = random.randrange(0, (len(list_of_riddles)/2)) #generates random riddles
    except ValueError:
        print()
        print('You have used too much of my time today. Leave.')
        print()
        quit()
    name, riddle = list_of_riddles[riddle_number * 2], list_of_riddles[riddle_number * 2 + 1] 
    print()
    print(riddle)
    print()
    list_of_riddles.pop(riddle_number*2+1) #makes sure you don't get the same riddle twice
    list_of_riddles.pop(riddle_number*2)

while answer!="": #Makes sure you only input a name that consists of letters
    answer = input(">>> Enter your name to start: ")
    if answer == "" or answer.isalpha() == False :
        print()
        print("Your name must consist of atleast 1 letter. No special symbols or numbers allowed.")
        print()
        input(">>> Press Enter to continue")
        answer=0
        print()
        break
    elif answer.isalpha() == True: #makes sure you only input letters
        print("Welcome, ",name,". Let's begin!",sep="")
        break
    

    if answer.lower() == name.lower() and points == 9: #checks if the answer is true
        points+=1
        print()
        print("WOW! You're smarter that I thought. Perhaps I underestimated your genius.")
        print()
        input(">>> Press Enter to continue")
        print()
    elif answer.lower() == name.lower() and points<9:
        points+=1 
        print()
        print('Correct!',"You have succesfully answered",points,"of my questions.", 10-points ,"more to go!")
        print()
        input(">>> Press Enter to continue.")
        print()
    else:
        error_counter+=1 
        print()
        print("Wrong. I hoped you'd be a bit better at this.","The correct answer was", name , ".")
        print()
        input(">>> Press Enter to continue.")
        print()
if points == 10 and error_counter == 0: #if you completed the game flawlessly
    print()
    print('Congrats,https://parade.com/947956/parade/riddles/')
    print()
    quit()
elif points == 10 and error_counter>0: #if you have made atleast one mistake, you'll have to play the minigame
    minigame()


