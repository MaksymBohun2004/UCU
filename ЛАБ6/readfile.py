from typing import List
import random
import string
import urllib.request
def generate_grid() -> List[List[str]]:
    """
    Generates list of lists of letters - i.e. grid for the game.
    e.g. [['I', 'G', 'E'], ['P', 'I', 'S'], ['W', 'M', 'G']]
    """
    letters = []
    lst = []
    for i in range(0,9):
        lst.append(string.ascii_uppercase[random.randrange(0,26)])
        if len(lst) == 3:
            letters.append(lst)
            lst = []
    return letters
def get_words(f: str, letters: List[str]) -> List[str]:
    """
    Reads the file f. Checks the words with rules and returns a list of words.
    """
    words_from_dict = []
    alphabet = [i for i in string.ascii_lowercase]
    letlist = []
    for lele in letters:
        letlist.append(lele.lower())
    for let in letlist:
        try:
            alphabet.remove(let.lower())
        except: continue
    with open (f,encoding="utf-8") as words:
        for word in words:
            counter = 0
            word = word[:-1].lower()
            for i in word:
                if i in alphabet:
                    counter += 1
                    break
            if counter == 0 and len(word) > 3 and letters[4].lower() in word:
                counterr = 0
                for i in word:
                    if word.count(i) > letlist.count(i):
                        counterr += 1
                if counterr == 0:
                    words_from_dict.append(word.lower())
    return words_from_dict


def get_user_words() -> List[str]:
    """
    Gets words from user input and returns a list with these words.
    Usage: enter a word or press ctrl+d to finish.
    """
    user_words = input().split()
    return user_words


def get_pure_user_words(user_words: List[str], letters: List[str], words_from_dict: List[str]) -> List[str]:
    """
    (list, list, list) -> list

    Checks user words with the rules and returns list of those words
    that are not in dictionary.
    """
    pure_words = []
    for i in user_words:
        if len(i) > 3 or letters[4] in i:
            if i not in words_from_dict:
                pure_words.append(i)
    return pure_words




def results():
    """
    Calls other functions and returns the results of the game
    """
    letters = generate_grid()
    letstr = ""
    for i in range(9):
        letstr += letters[i] + " "
        if len(letstr.replace("\n",'')) % 3 == 0:
            letstr += "\n"
    print(letstr)
    words_from_dict = get_words("en.txt", letters)
    user_words = get_user_words()
    pure_words = get_pure_user_words(user_words, letters, words_from_dict)
    rightcount = 0
    timed_words = words_from_dict.copy()
    for i in user_words:
        if i in words_from_dict:
            rightcount += 1
            words_from_dict.remove(i)
    print(rightcount)
    print(*words_from_dict)
    print(*timed_words)
    print(*pure_words)
results()
