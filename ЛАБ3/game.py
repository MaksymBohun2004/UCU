import random

list_of_riddles= [
    'egg', "Gypsy: What has to be broken before you can use it?",
     "candle", "Gypsy: I'm tall when I'm young, and I’m short when I'm old. What am I?",
     'weights','Gypsy: What heavy seven letter word can you take two away from and be left with eight?',
     "tie","Gypsy: I am a word with two meanings. With one I can be broken, with the second I hold on. What am I?",
     "dozens","Gypsy: A word I know, Six letters it contains, Subtract just one, And twelve is what remains.",
     "short","Gypsy: What common English word becomes shorter when you add two letters?",
     "incorrectly","Gypsy: What common 11-letter word is always spelled incorrectly?",
     "firetruck","Gypsy: Name a word that starts with \"f\" and ends with \"u-c-k\"? (tip: you'll need it when your house is burning)",
     "envelope","Gypsy: What word starts with E and ends with E and only has 1 letter in it?",
     "alone","Gypsy: I am a solitary word, 5 letters long. Behead me, and I am still the same. Behead me again, and I am still the same.",
     "misspelled","Gypsy: One word in this sentence is misspelled. What word is it?",
     "snail","Gypsy: If a man carried my burden he would break his back. I am not big but leave silver in my tracks. What am I?",
     "thursday","Gypsy: Alice is walking throught the forest of forgetfulness. She wants to know what day of the week it is. She stops and asks a lion and a unicorn. Now the lion lies all of the time on Monday, Tuesday, and Wednesday. The unicorn always lies on Thursday, Friday and Saturday.Alice asks the lion what day it is, he says, \"Well, yesterday was one of my lying days.\" Alice can't figure it out just from the lion's answer so she asks the unicorn and the unicorn says, \"Yesterday was also one of my lying days.\" What day is it?",
     "match","Gypsy: You have three stoves: a gas stove, a wood stove, and a coal stove, but only one match. Which should you light first?",
     "ohio","Gypsy: Which American state is round on the ends and high in the middle?",
     "window","Gypsy: Almost everyone sees me without noticing me,for what is beyond is what he or she seeks.What am I?",
     "oil","Gypsy: I am the fountain from which no one can drink. For many I am considered a necessary link. Like gold to all I am sought for, But my continued death brings wealth for all to want more.What am I?",
     "breath","Gypsy: I’m lighter than a feather, yet the strongest man can’t hold me for more than 5 minutes.",
     "dream","Gypsy: I come in darkness, but fill the mind with light.I bring enlightenment to some, while gripping others in the hand of fear.With me it can be a journey of inexplicable joy and sorrow.What I will show you will often be unreachable.Journey with me and what you see may haunt you.Journey with me and you may never want to return home.Journey with me and you will never know when it will end.What am I?",
     "clock","Gypsy: What has a face and two hands but no arms or legs?",
     "Mary","Gypsy: Mary's father has five daughters - Nana, Nene, Nini, Nono. What is the fifth daughter's name?",
     "cloud","Gypsy: I do not have wings, but I can fly. I don't have eyes, but I can cry! What  am I?",
     "fire","Gypsy: If I drink, I die. If I eat, I am fine. What am I?",
     'sandwich', 'Gypsy: What you call a witch at a beach?',
     'Screwdriver', 'Gypsy: What driver does not have a license?',
     'lawsuit', 'Gypsy: What kind of clothes do lawyers wear?',
     'barber', 'Gypsy: For what person do all men take off their hats?',
     'rainbow', 'Gypsy: The King cannot reach me and neither can the Queen.',
     'button', 'Gypsy: I have eyes,but I can’t see one bit.',
     'river', 'Gypsy: Always runs but never walks, often murmurs, never talks.',
     'towel', 'Gypsy: What gets wetter and wetter the more it dries? ',
     'teapot', 'Gypsy: What starts with T, ends with T and is full of T?',
     'cheese', 'Gypsy: You smile when you name it.',
     'mushroom', 'Gypsy: I grow in the dark, but I come up white.',
     'sugar', 'Gypsy: Clean, but not water, white, but not snow ,sweet, but not ice-cream, what is it?',
     'cat', "Gypsy: I am one with eight to spare, lest I lose my one. I'm not a number. What am I?",
     'echo', "Gypsy: You heard me before, yet you hear me again. Then I die, 'Til you call me again. What am I?",
     'key', 'Gypsy: I turn around once. What is out will not get in. I turn around again. What is in will not get out. What am I?',
     'time', 'Gypsy: Until I am measured, I am not known. Yet how you miss me, when I have flown. What am I?',
     'ostrich', 'Gypsy: Which bird does not belong in this group? Finch, gull, eagle, ostrich, or sparrow?',
     'ware', 'Gypsy: Which word can be placed between the two following words to make two new ones: TABLE - - - - HOUSE',
     'what', "Gypsy: What word doesn't belong in this group? That, hat, what, mat, cat, sat, pat, or chat?",
     'suicide', 'Gypsy: A certain crime is punishable if attempted but not punishable if committed. What is it?',
     'onion', 'Gypsy: You use a knife to slice my head and weep beside me when I am dead. What am I?',
     'shadow', "Gypsy: I'm the part of the bird that's not in the sky. I can swim in the ocean and yet remain dry. What am I?",
     'hole', "Gypsy: I am weightless, but you can see me. Put me in a bucket, and I'll make it lighter. What am I?",
     'eye', "Gypsy: Pronounced as one letter, and written with three, two letters there are, and two only in me. I'm double, I'm single, I'm black, blue, and gray, I'm read from both ends, and the same either way. What am I?",
     'e', 'Gypsy: From the beginning of eternity To the end of time and space To the beginning of every end And the end of every place. What am I?',
     'wind', 'Gypsy: All about, but cannot be seen, Can be captured, cannot be held, No throat, but can be heard. What is it?',
     'counterfeit', 'Gypsy: Whoever makes it, tells it not. Whoever takes it, knows it not. Whoever knows it, wants it not. What is it?',
     't', 'Gypsy: Which letter is a hot drink?',
     'Iceberg', 'Gypsy: Lighter than what I am made of, more of me is hidden than is seen.',
     'volcano', 'Gypsy: My thunder comes before the lightning; My lightning comes before the clouds; My rain dries all the land it touches. What am I?',
     'Mirror', 'Gypsy: look at my face and you see somebody. Look at my back and you see nobody',
     'stamp', 'Gypsy: What can travel around the world while staying in a corner?',
     'rain', 'Gypsy: What comes down but never goes up?'
     ]
def randomprediction(name):
    """ Last function in the game. It's simple, it picks a random prediction from the list
    and prints it.

    Your fortune is:
    What awaits is death, despair, and misfortune along that paths which you wa-
    oh I had the card upside down. Good fortune upon you, safe travels in the near future!

    Your fortune is:
    Ugh, that's no good...you will get kicked out of your university... you can avoid it if you...ummm.. study harder, i guess?
    """

    print()
    print('Congrats, you have shown that you\'re a true genius, ', name ,'! Guess i\'ll have to read your fortune now... ready to hear it? ',sep="")
    print()
    print("Press Enter to hear your fortune ")
    input(">>> ")
    print()
    print(name,": I'm ready!!!")
    print()
    predictions = ["You will come into a great fortune and then ... oh dear ... oh well, easy come easy go I guess.. or you may become a happy billionaire, I'm not sure...",
     "You will die...ummm...uhhh...one day.",
     "Ugh, that's no good...you will get kicked out of your university... you can avoid it if you...ummm.. study harder, i guess?",
     "You will be betrayed by one of your friends...oh no wait, wrong card, my bad. Where did i put the right one? Hmmm...cant find it. Sorry.",
     "With gold and silver, it will mark the utmost of the rings.  From out of the dark will rise a true king! All will hear the mages of the beach. You will fear the wish you beseech..To be honest, I dont quite understand what that means, too... but it sounds fancy, doesn't it?",
     "Ah, traveller...the Gods don't want me to reveal all that they have in store for you...but just between us, don't forget to pack extra wine. Why would you need wine? I LOVE wine, that's because.",
      "What awaits is death, despair, and misfortune along that paths which you wa- oh I had the card upside down. Good fortune upon you, safe travels in the near future!"]
    prediction = random.randrange(0, len(predictions)) #picks a random prectiction from the list
    print("Your fortune is:")
    print(predictions[prediction])
    print()
    print("Press Enter to react ")
    input(">>> ")
    print()
    print(name, ": Is that all you have to say after I solved all of your dumb riddles?")
    print()
    print("Gypsy: In case you want to hear more, my credit card number is 5168...")
    print()
    print("Press Enter to interrupt ")
    input(">>> ")
    print()
    print(name, ": But I told you i didn't have any money... that's why you made me solve the riddles in the first place!")
    print()
    print("Gypsy: At this point you're simply wasting my time. Bye")
    print("*beep*")
    print()
    print("Press Enter to see credits.")
    input(">>> ")
    print()
    print('Dear', name, '! Thanks for finding time to play this game! It means a lot to me. I would like to give credit to the resources I used while creating the game. I took some riddles from https://parade.com/947956/parade/riddles/ ,https://lim-english.com/posts/zagadki-na-angliiskom-yazike/ , http://grammar-tei.com/zagadki-dlya-detej-na-anglijskom-s-otvetami-riddles-for-kids/ and https://www.riddles.com/archives/180 . The other resource is https://www.reddit.com/r/DnD/comments/7hfwq5/i_need_at_least_twenty_different_random_fortunes/ , I took a few fortune predictions from there. ')
    SystemExit()
def minigame(name): # minigame where you have to guess a code
    """ A minigame that makes you solve an equation and open the box
    that gypsy gave you. It's not too hard, and you have unlimited tries, so everyone should be
    able to do it. You have to add two binary numbers and input your answer in decimal.


    In order to open the box, start by solving the first equation! Write your answer in decimal: 0b10 + 0b110 =
    >>> 8

    Correct!


    Solve the second equation to continue. Write your answer in decimal: 0b10 + 0b111 =
    >>> 9

    Correct!


    You're going strong! Are you smart enough to solve the third one? Write your answer in decimal: 0b101 + 0b111 =
    >>> 12

    Correct!

    """

    print()
    for i in range(1,4): # generates 3 random equations and checks if the answer is correct
        num1 = random.randrange(1,10)
        num2 = random.randrange(1,10)
        num1_b = bin(num1)
        num2_b = bin(num2)
        ranswer = num1 + num2
        if i == 1:
            print()
            print("In order to open the box, start by solving the first equation! Write your answer in decimal: " ,num1_b, " + ",num2_b, " = ",sep="")
        elif i == 2:
            print()
            print("Solve the second equation to continue. Write your answer in decimal: " ,num1_b, " + ",num2_b, " = ",sep="")
        elif i == 3:
            print()
            print("You're going strong! Are you smart enough to solve the third one? Write your answer in decimal: " ,num1_b, " + ",num2_b, " = ",sep="")
        answer = 0
        status = 0
        while status != True: #checks if the answer is an integer and if the answer is correct
            answer = input(">>> ")
            try:
                answer = int(answer)
            except:
                print()
                print("Wrong. Try again. Please, input one number in decimal.")
                print()
                continue
            if answer == ranswer:
                print()
                print("Correct!")
                status = 1
                print()
            elif answer != ranswer:
                print()
                print("Wrong. Try again. Please, input one number in decimal.")
                print()
    print("The box opens. It flashes brightly and dissappears.",name," is shook. ",sep="")
    print()
    print("Press Enter to ask what happened")
    input(">>> ")
    print(name,": What happened? What was in the box?")
    print()
    print("Gypsy: A really expensive diamond. I couldn't solve those equations for years, and I was starting to lose hope. Thanks for doing it for me!")
    randomprediction(name)

def main(name):
    """ Main part of the game. In order to move forward, you have to solve 10 riddles.
    All riddles have a one-word answer that only consists of letters(no numbers or special symbols).
    Riddles are picked randomly from the list of riddles and removed from it so you won't have to solve the same riddle twice.
    If you can solve 10 riddles flawlessly(without any mistakes), you will hear your fortune prediction instantly.
    If you make atleast 1 mistake, you will have to complete the minigame in order to hear your fortune prediction.
    If all the riddles are used up and you still didn't reach the score of 10 points, you will fail and the game will restart automatically.

    """
    error_counter=0 # error counter is 1 or more, you will have to complete the minigame.
    points=0 # if points are 10 you will proceed to the next stage of the game
    while points<10:
        try:
            riddle_number = random.randrange(0, (len(list_of_riddles)/2)) #generates random riddles
        except ValueError:  # if there are no riddles left
            print()
            print('You have used too much of my time today. Leave.')
            print("*beep*")
            print()
            print("You failed, ",name,". Better luck next time! The game will restart now.")
            print()
            print("Press Enter to restart the game ")
            input(">>> ")
            opening()
        ranswer, riddle = list_of_riddles[riddle_number * 2], list_of_riddles[riddle_number * 2 + 1]
        print()
        print(riddle)
        print()
        list_of_riddles.pop(riddle_number*2+1) #makes sure you don't get the same riddle twice
        list_of_riddles.pop(riddle_number*2)
        print("Enter your answer: ")
        answer=str(input(">>> "))
        if answer.isalpha() == False:  #checks if the answer only consists of letters
            print()
            print("You can only input letters")
            print()
            print("Enter your answer using letters only: ")
            answer=str(input(">>> "))
            print()
        elif answer.isalpha() == True: #makes sure you only input letters
            pass

        if answer.lower() == ranswer.lower() and points == 9: # if you solve 10 riddles you proceed to the next stage
            points+=1
            print()
            print("Gypsy: WOW! You're smarter that I thought, ",name, ". Perhaps I underestimated your genius.",sep="")
            print()
            print("Press Enter to continue")
            input(">>> ")
            print()
        elif answer.lower() == ranswer.lower() and points<9:  # shows you how many riddles you already solved and how many more you have to
            points+=1
            print()
            print('Correct!',"You have succesfully answered",points,"of my questions.", 10-points ,"more to go!")
            print()
            print("Press Enter to continue.")
            input(">>> ")
            print()
        else:
            error_counter+=1  #adds to the error counter and tells what the right answer was
            print()
            print("Gypsy: Wrong. I hoped you'd be a bit better at this, ",name,". The correct answer was ", ranswer , ".", sep="")
            print()
            print("Press Enter to continue.")
            input(">>> ")
            print()
    if points == 10 and error_counter == 0: #if you completed the game flawlessly
        randomprediction(name)
    elif points == 10 and error_counter>0: #if you have made atleast one mistake, you'll have to play the minigame
        print()
        print("Gypsy: You did well, ",name,"! But  you did make some mistakes while solving, so in order to make sure that you're worthy to hear your fortune, i'll give you a box. If you are smart enough to solve the equation and guess the code that unlocks it, i'll tell you your fortune.", sep="")
        print()
        print("Press Enter to speak")
        input(">>> ")
        print()
        print(name,": H-how will you give me the bo...")
        print()
        print(name,"sees a bright light. He looks around him and sees a small box behind him. It has a lock and a piece of paper on it.")
        minigame(name)

def opening(): #indroduces the player to the game and gives a backstory
    """ The beggining of the game. It gives a backstory and an rpg-ish feeling to it.
        It's impossible to get an error and there are no tests, so all players can proceed to solving the riddles.
        This part also has a multiple-choice option, but it is made that way to give the player the illusion of choice,
        because no matter what he/she picks he/she is still going to get to the same main function and solve roddles.
        This function also collects info on the player's name which is going to be used though the rest of the game.

        Example 1:
        Enter your name to start:
        >>> Max
        Welcome, Max. Let's begin!

        Max is having a bad day. In fact, this last few month were a disaster for Max. Everything Max does seems to go extremely wrong, and Max doesn't know what to do.

        >>> Press Enter to continue


        Example 2:
        Gypsy: Of course I know your name! I know everything about you! In fact, I know everything about everybody! How would you like to transfer the funds?

        >>> How would you like to answer? Press Enter to see the options

        Choose your answer(1 or 2):
        1. I have no money... i was hoping you'd tell me my faith for free.(tell the truth)
        2. I have lots of cash to burn! Send me your credit card details right now!(lie)
        Make your choice:
        >>> 2

        Max : I have lots of cash to burn! Send me your credit card details right now!

        Gypsy: well, it's 5168 19...
    """
    for i in range(1,150): #cleans the console before starting the game
        print()
    print("Welcome to \"Gypsy\" by Maksym Bohun.")
    print()
    print('Press Enter to continue ')
    input(">>> ")
    print()
    print("\'Gypsy\' is a riddle game. In order to complete it, you will have to put your smartness and logical thinking to the test!")
    print()
    print('Press Enter to continue ')
    input(">>> ")
    print()
    print("The rules are simple: all riddles have a one-word answer that doesn't include numbers or special symbols. P.S: don't take gypsy's predictions too seriously, she's just a lier.")
    print()
    name=0
    while name!="": #Makes sure you only input a name that consists of letters
        print("Enter your name to start: ")
        name = input(">>> ")
        if name == "" or name.isalpha() == False :
            print()
            print("Your name must consist of atleast 1 letter. No special symbols or numbers allowed.")
            print()
            print("Press Enter to continue")
            input(">>> ")
            name=0
            print()
        elif name.isalpha() == True: #makes sure you only input letters
            print("Welcome, ",name,". Let's begin!",sep="")
            break
    print()
    print(name," is having a bad day. In fact, this last few month were a disaster for ",name,". Everything ",name," does seems to go extremely wrong, and ",name, " doesn't know what to do.",sep="")
    print()
    print('Press Enter to continue ')
    input(">>> ")
    print()
    print("While surfing the net, ",name," comes across an article on gypsies and their magical powers which ",name, " finds extremely intriguing. In the end of the article ",name," sees an add that says:\"Call me right now! Im a gypsy who will tell you your future for a small pay! ",name," decides to call",sep="")
    print()
    print("Press Enter to continue ")
    input(">>> ")
    print()
    print("Gypsy: Hi, ",name,"! It's me, the gypsy from the article! I will tell your future for a small pay!",sep="")
    print()
    print("Press Enter to talk ")
    input(">>> ")
    print()
    print(name,": W-what?! How do you know my name?")
    print()
    print("Gypsy: Of course I know your name! I know everything about you! In fact, I know everything about everybody! How would you like to transfer the funds?")
    print()
    print("How would you like to answer? Press Enter to see the options ")
    input(">>> ")
    print()
    print("Choose your answer(1 or 2):")
    print("1. I have no money... i was hoping you'd tell me my faith for free.(tell the truth)")
    print("2. I have lots of cash to burn! Send me your credit card details right now!(lie)")
    an=0
    while an!="": #Makes sure you only input 1 or 2
        try:
            print("Make your choice: ")
            an = int(input(">>> "))
        except ValueError:
            print()
        if an == 1:
            print()
            print(name,": I have no money... i was hoping you'd tell me my faith for free.")
            print()
            print("Gypsy: i've never met such an arrogant human being... fine, i'll tell you your faith, but only if you are smart enough to solve 10 of my riddles! Ready?")
            print()
            print("Press Enter to say that you're ready ")
            input(">>> ")
            print()
            print(name,": I was born ready!")
            print()
            print("Gypsy: look at you, so full of yourself! Let's see how smart you actually are!")
            print()
            print("Press Enter to start solving! ")
            input(">>> ")
            main(name)
            break
        elif an==2:
            print()
            print(name,": I have lots of cash to burn! Send me your credit card details right now!")
            print()
            print("Gypsy: well, it's 5168 19...")
            print()
            print("Press Enter to interrupt ")
            input(">>> ")
            print()
            print(name,": sorry for lying...I have no money... ")
            print()
            print("Gypsy: you little lier! Fine, ill tell you your faith for free, but only if you are smart enough to solve 10 of my riddles. Ready?")
            print()
            print("Press Enter to say that you're ready ")
            input(">>> ")
            print()
            print(name,": I was born ready!")
            print()
            print("Gypsy: look at you, so full of yourself! Let's see how smart you actually are!")
            print()
            print("Press Enter to start solving! ")
            input(">>> ")
            main(name)
            break
        elif an != 1 and an != 2:
            print()
            print("Please choose a number (1 or 2)")
            print()
    return(name)
opening()