import random


countries = ["Afghanistan", "Albania", "Argentina", "Armenia", "Australia",
             "Austria", "Azerbaijan", "Belarus", "Belgium",
             "Bosnia and Herzegovina", "Brazil", "Bulgaria", "Cambodia",
             "Canada", "China", "Colombia", "Costa Rica", "Croatia",
             "Czech Republic", "Denmark", "Egypt", "England", "Estonia",
             "Finland", "France", "Georgia", "Germany", "Greece", "Hungary",
             "Iceland", "India", "Ireland", "Israel", "Italy", "Japan",
             "Kazakhstan", "Kuwait", "Latvia", "Libya", "Lithuania", "Mexico",
             "Moldova", "Monaco", "Mongolia", "Montenegro", "Morocco",
             "Nepal", "Netherlands", "New Zealand", "North Korea",
             "North Macedonia", "Northern Ireland", "Norway", "Peru",
             "Philippines", "Poland", "Portugal", "Romania", "Scotland",
             "Serbia", "Slovakia", "Slovenia", "South Korea", "Spain",
             "Sweden", "Switzerland", "Thailand", "Turkey", "Ukraine",
             "United Arab Emirates", "United States", "Wales"]

capitals = ["Kabul", "Tirana", "Buenos Aires", "Yerevan", "Canberra",
            "Vienna", "Baku", "Minsk", "Brussels", "Sarajevo", "Brasilia",
            "Sofia", "Phnom Penh", "Ottawa", "Beijing", "Bogota", "San Jose",
            "Zagreb", "Prague", "Copenhagen", "Cairo", "London", "Tallinn",
            "Helsinki", "Paris", "Tbilisi", "Berlin", "Athens", "Budapest",
            "Reykjavik", "New Delhi", "Dublin", "Jerusalem", "Rome", "Tokyo",
            "Nur-Sultan", "Kuwait City", "Riga", "Tripoli", "Vilnius",
            "Mexico City", "Chisinau", "Monaco", "Ulaanbaatar", "Podgorica",
            "Rabat", "Kathmandu", "Amsterdam", "Wellington", "Pyongyang",
            "Skopje", "Belfast", "Oslo", "Lima", "Manila", "Warsaw", "Lisbon",
            "Bucharest", "Edinburgh", "Belgrade", "Bratislava", "Ljubljana",
            "Seoul", "Madrid", "Stockholm", "Bern", "Bangkok", "Ankara",
            "Kiev", "Abu Dhabi", "Washington D.C.", "Cardiff"]

print("Background: You came to a travel agency to buy vacation vouchers")
print("Input your name: ")
name = input(">>> ")
start_msg = f"""'{name}, it turned out that you have become an
anniversary customer and the company offers to play a
game where you need to choose the right capitals of some
countries. If you guess the specified number of times,
the plane tickets will be paid to the tour agency, and
if not - then you still have to pay for them ...'"""

print(start_msg)


random_index = random.randint(0, len(countries) - 1)
# run the game


def generat_guess_list(capital):
    """
    This function randomly selects the country and capital to guess
    + wrong answers
    :param capital: str, items from the list
    :return: str,
    """
    test_guess = [capital]
    while len(test_guess) != 3:
        cap = random.choice(capitals)
        if cap not in capital:
            test_guess.append(cap)
    return form_choices(test_guess)


def form_choices(test_guess):
    """
    str -> str
    This function takes data from the previous one and generates
    "tasks", which in turn will output the function "main".
    :test_guess: data from the previous function.
    :return:str, choices which the player will choose.
    """
    random.shuffle(test_guess)
    choices = {"a": test_guess[0],
               "b": test_guess[1],
               "c": test_guess[2]
               }
    return choices


MISTAKES = 0
COUNT = 0


def main(country, capital):
    """
    str -> str
    This function displays tasks, takes answers, processes them,
    counts points and mistakes.
    :param country: str, items from the list.
    :param capital: str, items from the list.
    return: the result of the whole game.
    """
    choices = generat_guess_list(capital)

    pre = "Select a Capital for the %s:\n" % country + \
          "\n".join([i + ") " + choices[i] for i in choices.keys()])
    print(pre + "\nYour answer (just letter, e.g. 'a'): ")
    res = input(">>> ").lower()
    while res not in ["a", "b", "c"]:
        print("Please input one of the available options('a', 'b' or 'c')!")
        res = input(">>> ").lower()

    global MISTAKES
    global COUNT

    if choices[res] == capital:
        # guess the question
        COUNT += 1
        print("Well done!\n")
        # play once more
    elif choices[res] != capital:
        MISTAKES += 1
        COUNT += 1
        print("Failed\n")

    if COUNT == 6 and MISTAKES == 1:
        # win the game
        print("Congrats. Tickets are yours!!!")
        quit()
    if COUNT == 7:
        # game is over
        print("Congrats. Tickets are yours!!!")
        quit()
    if MISTAKES == 2:
        # game is over
        print("You lost your chance...")
        quit()
    random_index = random.randint(0, len(countries) - 1)

    main(countries[random_index], capitals[random_index])


begin_game = ('Would you like to start game \nWrite "yes" or "no"')
# This cycle is responsible for starting the game
print(begin_game)
"""
At the beginning there are two dictionaries of where the countries and
their capitals will be taken for tasks, as well as a brief background
to explain to the player what, where and how.
"""
start_game = input(">>> ").lower()
while start_game not in ["yes", "no"]:
    print("Please write 'yes' or 'no'")
    start_game = input(">>> ").lower()
if start_game == "yes":
    print()
    main(countries[random_index], capitals[random_index])
elif start_game == "no":
    print("Ok.Bye")
    quit()


if __name__ == '__main__':
    main()
