"""
A game where you have to guess words that start with
a letter from a generated list and are less that 5 letters
long.
"""
import random


def generate_grid():
    """
    Generates a grid of 5 letters
    Always fails in CMS :-)
    """
    alphabet = "абвгґдеєжзиіїйклмнопрстуфхцчшщьюя"
    letters = []
    while len(letters) < 5:
        let = random.choice(alphabet)
        if let not in letters:
            letters.append(let)
    return letters


def get_words(file, letters):
    r"""
    Returns all words from Ukrainian dictionary that
    start with one of the generated letters and are longer that 5 letters,
    in tuples (word, language_part)
    >>> get_words("base.lst", ['ю', 'щ', 'я', 'ц', 'г']) #doctest: +ELLIPSIS
    [('габа', 'noun'), ('габро', 'noun'), ('гавин', 'adjective')...
    """
    dict_of_words = []
    with open(file, encoding="utf-8") as words:
        for line in words:
            line = line.split()
            if len(line[0]) <= 5:
                if line[0][0] in letters:
                    if line[1].startswith("/n") or line[1].startswith("noun"):
                        dict_of_words.append((line[0], "noun"))
                    elif line[1].startswith("/v") or line[1].startswith("verb"):
                        dict_of_words.append((line[0], "verb"))
                    elif line[1].startswith("/adj") or line[1].startswith("adj"):
                        dict_of_words.append((line[0], "adjective"))
                    elif line[1].startswith("/adv") or line[1].startswith("adv"):
                        dict_of_words.append((line[0], "adverb"))
    return dict_of_words


def check_user_words(user_words, language_part, letters, dict_of_words):
    """
    Checks which of the user words meet the requirements and returns a list
    of words guessed
    >>> check_user_words(['гаяти', 'гнати', 'ініціалізація', 'узяти', 'щавель'], "verb",\
['ю', 'щ', 'я', 'ц', 'г'], get_words("base.lst", ['ю', 'щ', 'я', 'ц', 'г']))
    (['гаяти', 'гнати'], ['гнити', 'гнути', 'гоїти', 'грати', 'гріти', 'густи', \
'юшити', 'явити', 'яріти', 'ячати'])
    """
    correct_words = []
    missed_words = []
    for isword in range(len(user_words) - 1):
        if user_words[isword][0] not in letters or len(user_words[isword]) > 5:
            del user_words[isword]
    for word in dict_of_words:
        if word[0] in user_words:
            if word[1] == language_part:
                correct_words.append(word[0])
        elif word[0] not in user_words:
            if word[1] == language_part:
                missed_words.append(word[0])
    return correct_words, missed_words


def get_user_words():
    """
    Takes user words and returns a list of them
    """
    user_words = input("Enter your words: ").split()
    return user_words


def language_part_gen():
    """
    Generates a random language part
    """
    parts = ['noun', 'verb', 'adjective', 'adverb']
    return random.choice(parts)


def results():
    """
    Calls all of the functions and makes them work in unison,
    the game is played through this function and the user
    gets to see results of his play
    """
    for i  jaan
    letters = generate_grid()
    print(*letters)
    language_part = language_part_gen()
    print("Language part is:", language_part)
    dict_of_words = get_words("base.lst", letters)
    user_words = get_user_words()
    correct_words, missed_words = \
        check_user_words(user_words, language_part, letters, dict_of_words)
    print("You guessed ", len(correct_words), " words correctly")
    print("You missed those words: ", *missed_words)
