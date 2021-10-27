import string

def get_number():
    number = 49
    return number


# Complete all of the following functions. Currently they all just
# 'pass' rather than explicitly return value, which means that they
# implicitly return None. They all include doctests, which you can
# test by running this file.

# The doctests are just examples. Feel free to add your own doctests.

# ****************************************
# Problem 1
# ****************************************
def get_position(ch):
    """
    str -> int
    Return positon of letter in alphabet. If argument is not a letter function
    should return None.

    >>> get_position('A')
    1
    >>> get_position('z')
    26
    >>> get_position('Dj')

    """
    pass


# ****************************************
# Problem 2
# ****************************************
def compare_char(ch1, ch2):
    """
    (str, str) -> bool
    Compare two char by their position in alphabet. Return True if letter
    ch2 appears before ch1 and False otherwise. If neither ch1 nor ch2 are
    letters function should return None.

    >>> compare_char('a', 'z')
    False
    >>> compare_char('c', 'B')
    True
    >>> compare_char('d', 'ad')

    >>> compare_char('2', 2)

    """
    pass


# ****************************************
# Problem 3
# ****************************************
def compare_str(s1, s2):
    """
    (str, str) -> bool
    Compare two srings lexicographicly. Return True if string s1 is larger
    than string s2 and False otherwise. If arguments aren't string or function
    have different length function should return None.

    >>> compare_str('abc', 'Abd')
    False
    >>> compare_str('zaD', 'zab')
    True
    >>> compare_str('zaD', 'Zad')
    False
    >>> compare_str('aaa', 'aaaaa')

    >>> compare_str('2015', 2015)

    """
    try:
        s1, s2 =  str(s1),str(s2)
    except ValueError:
        return None
    booll = 0
    if s1.isalpha() == False or s2.isalpha() == False:
        return None
    if len(s1) != len(s2):
        return None
    elif s1 < s2:
        booll = True
        return(booll)
    elif s1 > s2:
        booll = False
        return(booll)


# ****************************************
# Problem 4
# ****************************************
def type_by_angles(a, b, c):
    """
    (float, float, float) -> str
    Detect the type of triangle by it's angles in degrees and return type as string
    ("right angled triangle", "obutuse triangle", "acute triangle"). If there is no
    triangle with such angles, then function should return None.

    >>> type_by_angles(60, 60, 60)
    acute triangle
    >>> type_by_angles(90, 30, 60)
    right angled triangle
    >>> type_by_angles(2015, 2015, 2015)

    """
    pass


# ****************************************
# Problem 5
# ****************************************
# ****************************************
# Problem 5
# ****************************************
def type_by_sides(a, b, c):
    """
    (float, float, float) -> str
    Detect the type of triangle by it's sides and return type as string
    ("right angled triangle", "obutuse triangle", "acute triangle"). If there is no
    triangle with such sides, then function should return None.

    >>> type_by_sides(3, 3, 3)
    "acute triangle"
    >>> type_by_sides(3, 4, 5)
    "right angled triangle"
    >>> type_by_sides(3, 3, 2015)
    """
    if a == b and b == c:
        a, b, c = int(a), int(b), int(c)
        return("acute triangle")
    else:
        lst =[ a,b,c]
        lst.sort()
        a = int(lst[0])
        b = int(lst[1])
        c = int(lst[2])
    if a + b < c:
        return(None)
    elif (a ** 2 + b ** 2) == (c ** 2):
        return("right angled triangle")
    elif a ** 2 + b ** 2 < c ** 2:
        return("obutuse triangle")
    elif a ** 2 + b ** 2 > c ** 2:
        return("acute triangle")

# ****************************************
# Problem 6
# ****************************************
def remove_spaces(s):
    """
    str -> str
    Remove all additional spaces in string and return a new string without additional spaces.
    If argument is not a string function should return None.

    >>> remove_spaces("I'll make     him an     offer he can't refuse.")
    I'll make him an offer he can't refuse.
    >>> remove_spaces("Great    men     are    not born great, they grow great...")
    Great men are not born great, they grow great...
    >>> remove_spaces(2015)

    """
    pass


# ****************************************
# Problem 7
# ****************************************
def convert_to_column(s):
    """
    str -> str
    Convert string to a column of words.
    If argument is not a string function should return None.

    >>> print_column("Revenge is a dish that tastes best when served cold.")
    revenge
    is
    a
    dish
    that
    tastes
    best
    when
    served
    cold
    >>> print_column("Never hate your enemies. It affects your judgment.")
    never
    hate
    your
    enemies
    it
    affects
    your
    judgment
    >>> print_column(2015)
    """
    pass


# ****************************************
# Problem 8
# ****************************************
# ****************************************
# Problem 8
# ****************************************
def number_of_sentences(s):
    """
    str -> str
    Return number of sentence in the string. If argument is not a string function should
    return None.

    >>> number_of_sentences("Revenge is a dish that tastes best when served cold.")
    1
    >>> number_of_sentences("Never hate your enemies. It affects your judgment.")
    2
    >>> number_of_sentences(2015)

    """
    s = str(s)
    if int(s.count(".")) == 0:
        return None
    else:
        return int(s.count("."))



# ****************************************
# Problem 9
# ****************************************
def replace_with_stars(s):
    """
    str -> str
    Replace symbols in string with stars. If argument is not a string function should
    return None.

    >>> number_of_sentences("Revenge is a dish that tastes best when served cold.")
    ****************************************************
    >>> number_of_sentences("Never hate your enemies. It affects your judgment.")
    **************************************************
    >>> number_of_sentences(2015)

    """
    if isinstance(s , str) != True:
        return None
    if int(len(s)) == 0:
        return None
    else:
        x = int(len(s))
        returned_x = ("*" * x)
        print(returned_x)
        return returned_x



# ****************************************
# Problem 10
# ****************************************
def encrypt_message(s):
    """
    str -> str
    Replace all letters in string with next letters in aplhabet. If argument is not a string
    function should return None.

    >>> encrypt_message("Revenge is a dish that tastes best when served cold.")
    Sfwfohf jt b ejti uibu ubtuft cftu xifo tfswfe dpme.
    >>> encrypt_message("Never hate your enemies. It affects your judgment.")
    Ofwfs ibuf zpvs fofnjft. Ju bggfdut zpvs kvehnfou.
    >>> encrypt_message(2015)

    """
    alphabet = ["A", "B", "C", "D", "E", "F", 
    "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", 
    "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    if isinstance(s , str) != True:
        return None
    letter_string =""
    for i in range(0,len(s)):
        if s[i] == " ":
            letter_string += " "
        elif s[i] == ".":
            letter_string += "."
        elif s[i] == s[i].lower():
            let = s[i]
            saui = string.ascii_lowercase.index(let)
            let_num = int((saui + 1))
            letter_string += alphabet[let_num].lower()
        elif s[i] == s[i].upper():
            let = s[i]
            saui = string.ascii_uppercase.index(let)
            let_num = int((saui + 1))
            letter_string += alphabet[let_num]
    return letter_string



import string
# ****************************************
# Problem 11
# ****************************************
def decrypt_message(s):
    """
    str -> str
    Replace all letters in string with previous letters in aplhabet. If argument isn't a string
    function should return None.

    >>> decrypt_message("Sfwfohf jt b ejti uibu ubtuft cftu xifo tfswfe dpme.")
    Revenge is a dish that tastes best when served cold.
    >>> decrypt_message("Ofwfs ibuf zpvs fofnjft. Ju bggfdut zpvs kvehnfou.")
    Never hate your enemies. It affects your judgment.
    >>> decrypt_message(2015)

    """
    alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    if isinstance(s , str) != True:
        return None
    letter_string =""
    for i in range(0,len(s)):
        if s[i] == " ":
            letter_string += " "
        elif s[i] == ".":
            letter_string += "."
        elif s[i] == s[i].lower():
            let = s[i]
            saui = string.ascii_lowercase.index(let)
            let_num = int((saui - 1))
            letter_string += alphabet[let_num].lower()
        elif s[i] == s[i].upper():
            let = s[i]
            saui = string.ascii_uppercase.index(let)
            let_num = int((saui - 1))
            letter_string += alphabet[let_num]
    return letter_string


# ****************************************
# Problem 12
# ****************************************
def exclude_letters(s1, s2):
    """
    (str, str) -> str
    Delete all letter from string s2 in string s1. If arguments aren't strings function should
    return None.

    >>> exclude_letters("aaabb", "b")
    aaa
    >>> exclude_letters("abcc", "cczzyy")
    ab
    >>> exclude_letters(2015, "sasd")

    """
    if isinstance(s1, str) != True or isinstance(s2, str) != True :
        return None
    for i in s1:
        for j in s2:
            if i == j:
                s1 = s1.replace(i,"")
    return s1

# ****************************************
# Problem 13
# ****************************************
def create_string(lst):
    """
    list -> str
    Create and return string from histogrma of letters. If argument isn't list of 26 positive
    integer numbers function should return None.

    >>> create_string([0, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    bcc
    >>> create_string([4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4])
    aaaazzzz
    >>> create_string([4, 0, 0, 0, 0, 0])

    """
    alphabet = list(string.ascii_lowercase)
    string_ = ""
    lengh = len(lst)
    if len(lst) != 26:
        return None
    for i in range(0, lengh):
        if lst[i] < 0: 
            return None
        elif lst[i] >= 0:
            string_ = string_ + (alphabet[i] * lst[i])
    return(string_)


# ****************************************
# Problem 14
# ****************************************
def get_letters(n):
    """
    int -> str
    Create and return string of first n letters of an alphabet. If arguments isn't
    positive integer number function should return None.

    >>> get_letters(0)

    >>> get_letters(1)
    a
    >>> get_letters(-2015)

    """
    pass


# ****************************************
# Problem 15
# ****************************************
def find_intersection(s1, s2):
    """
    (str, str) -> str
    Find and returs string of all letters in alphabetic order that
    are present in both strings. If arguments aren't strings function
    should return None.

    >>> find_intersection("aaabb", "bbbbccc")
    b
    >>> find_intersection("aZAbc", "zzYYxp")
    z
    >>> find_intersection("sfdfsdf", 2015)

    """
    pass


# ****************************************
# Problem 16
# ****************************************
def find_union(s1, s2):
    """
    (str, str) -> str
    Find and return string of all letters in alphabetic order that
    are present in either strings. If arguments aren't strings function should
    return None.

    >>> find_union("aaabb", "bbbbccc")
    abc
    >>> find_union("aZAbc", "zzYYxp")
    AYZabcpxz
    >>> find_union("sfdfsdf", 2015)

    """
    pass


# ****************************************
# Problem 17
# ****************************************
def number_of_occurence(lst, s):
    """
    (list, str) -> int
    Find and return number of occurence of string s in all elements of the
    list lst. If lst isn't list of strings or s isn't string function should
    return None.

    >>> number_of_occurence(["man", "girl", "women", "boy"], "m")
    2
    >>> number_of_occurence(["ab", "aba", "a", "b", "ba"], "ba")
    2
    >>> number_of_occurence([1, 2, 2015, 1, 3], "1")

    """
    pass


# ****************************************
# Problem 18
# ****************************************
def number_of_capital_letters(s):
    """
    str -> str
    Find and return number of capital letters in string. If argument isn't string
    function should return None.

    >>> number_of_capital_letters("ArithmeticError")
    2
    >>> number_of_occurence("EOFError")
    4
    >>> number_of_capital_letters(1)

    """
    pass


# ****************************************
# Problem 19
# ****************************************
def polygon_area(vertices):
    """
    Calculates the area of a 3 or 4-angled figure 
    using the locations of it's points.
    >>> polygon_area([(4,10), (9,7), (11,2), (2,2)])
    45.5
    >>> polygon_area([(9,7), (11,2), (2,2), (4, 10)])
    45.5
    >>> polygon_area([(0, 0), (0.5,1), (1,0)])
    0.5
    >>> polygon_area([(0, 10), (0.5,11), (1,10)])
    0.5
    >>> polygon_area([(-0.5, 10), (0,-11), (0.5,10)])
    10.5

    """
    if len(vertices) == 3:
          a1 = 0
          a2 = 0
          b1 = 0
          b2 = 0
          c1 = 0
          c2 = 0
          for point in vertices:
                if point == vertices[0]:
                  a1 = point[0]
                  a2 = point[1]
                elif point == vertices[1]:
                  b1 = point[0]
                  b2 = point[1]
                elif point == vertices[2]:
                  c1 = point[0]
                  c2 = point[1]
          lengthAB = ((b1 - a1)**2 + (b2 - a2)**2)**0.5
          lengthBC = ((c1 - b1)**2 + (c2 - b2)**2)**0.5
          lengthAC = ((c1 - a1)**2 + (c2 - a2)**2)**0.5
          p = (lengthAB + lengthBC + lengthAC)/2
          s = (p*(p - lengthAB)*(p - lengthBC)*(p - lengthAC))**0.5
          return s
          
    elif len(vertices) == 4:
      x1 = 0
      y1 = 0
      x2 = 0
      y2 = 0
      x3 = 0
      y3 = 0
      x4 = 0
      y4 = 0
    
      for i in range(0,len(vertices)):
        if i == 0:
          x1 = vertices[i][0]
          y1 = vertices[i][1]
        elif i == 1:
          x2 = vertices[i][0]
          y2 = vertices[i][1]
        elif i == 2:
          x3 = vertices[i][0]
          y3 = vertices[i][1]
        elif i == 3:
          x4 = vertices[i][0]
          y4 = vertices[i][1]
    print(x1,y1,x2,y2,x3,y3,x4,y4)
    s = (abs(((x1 * y2) - (x2 * y1)) + ((x2 * y3) - (x3 * y2)) + ((x3 * y4) - (x4 * y3)) + ((x4 * y1) - (x1 * y4))))/2
    return s



# ****************************************
# Problem 20
# ****************************************
def polynomial_eval(coefficients, value):
    """
    # f(x) = 2x^3 + 3x^2 + 4, f(4) = 180
    >>> polynomial_eval([2,3,0,4], 4)
    180
    # f(x) = 6, f(42) = 6
    >>> polynomial_eval([6], 42)
    6
    # f(x) = 6x^2 -2x - 20, f(-1) = -12
    >>> polynomial_eval([6,-2,-20], -1)
    -12
    # f(x) = 6x^5-8x^3-8x, f(2) = 112, f(1) = -10, f(0) = 0
    >>> polynomial_eval([6,0,-8,0,-8,0], 2)
    112
    >>> polynomial_eval([6,0,-8,0,-8,0], 1)
    -10
    >>> polynomial_eval([6,0,-8,0,-8,0], 0)
    0
    """

    return True


# ****************************************
# Problem 21
# ****************************************
def polynomials_multiply(polynom1, polynom2):
    """
    # (2x)*(3x) == 6
    >>> polynomials_multiply([2], [3])
    [6]
    # (2x-4)*(3x+5) == 6x^2 -2x - 20
    >>> polynomials_multiply([2,-4],[3,5])
    [6,-2,-20]
    # (2x^2-4)*(3x^3+2x) == (6x^5-8x^3-8x)
    >>> polynomials_multiply([2,0,-4],[3,0,2,0])
    [6,0,-8,0,-8,0]

    """

    return True


# ****************************************
# Problem 22
# ****************************************
def pattern_number(sequence):
    """
    Finds a pattern in a string or a list and returns 
    a cortage of the pattern and a number of repeats
    >>> pattern_number([])
    None
    >>> pattern_number([42])
    None
    >>> pattern_number([1,2])
    None
    >>> pattern_number([1,1])
    ([1], 2)
    >>> pattern_number([1,2,1])
    None
    >>> pattern_number([1,2,3,1,2,3])
    ([1,2,3], 2)
    >>> pattern_number([1,2,3,1,2])
    None
    >>> pattern_number([1,2,3,1,2,3,1])
    None
    >>> pattern_number(list(range(10))*20)
    ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 20)
    >>> pattern_number('мама')
    ('ма', 2)
    >>> pattern_number('барабан')
    None
    """

    for i in range(len(sequence) // 2):
        seq = sequence[0:i+1]
        if type(sequence) == list:
            timed_sequence = sequence.copy()
        else:
            timed_sequence = sequence
        variable = True
        counter = 0
        while len(timed_sequence) > 0:
            if variable == False:
                break
            count = 0
            variable = 0
            for j in seq:
                if j == timed_sequence[count]:
                    count += 1
                    variable = True
                    pass
                else:
                    variable = False
                    break
            if variable == True:
                for _ in range(len(seq)):
                    if type(sequence) == list:
                        timed_sequence.pop(0)
                    else:
                        timed_sequence = timed_sequence[1:]
                counter += 1
            else:
                continue
        if len(timed_sequence) == 0:
            return seq, counter
    return None



# ****************************************
# Problem 23
# ****************************************
def one_swap_sorting(sequence):
      """
      This function returns True if you can sort a list by changing the position
      of two elements in it, and False in any other situation.

      >>> one_swap_sorting([0,1,2,3])
      False
      >>> one_swap_sorting([])
      False
      >>> one_swap_sorting([42])
      False
      >>> one_swap_sorting([3,2])
      True
      >>> one_swap_sorting([2,2])
      False
      >>> one_swap_sorting([5,2,3,4,1,6])
      True
      >>> one_swap_sorting([1,2,3,5,4])
      True
      """
      if len(sequence) > 0:
            pass
      else: 
            return False
      sorted_sequence = sorted(sequence)
      if sorted_sequence == sequence:
            return False
      else: 
            pass
      count = 0 
      for i in range(0,len(sequence)):
          if sequence[i] == sorted_sequence[i]:
                continue
          else:
                count += 1
      if count == 2:
            return True
      else: 
            return False


# ****************************************
# Problem 24
# ****************************************
def numbers_Ulam(n):
    """
    Return a list that consists of n Ulam numbers, starting from 1. 
    Ulam number is a number that is the smallest whole
    number that: 
    1. Is a sum of two numbers that are already in the list.
    2.  Can only be found in one way.
    3. Is larger than the biggest number in the list.
    >>> numbers_Ulam(10)
    [1, 2, 3, 4, 6, 8, 11, 13, 16, 18]
    >>> numbers_Ulam(2)
    [1, 2]
    >>> numbers_Ulam(1)
    [1]
    """
    timedlist = [1,2]
    mainlist = []
    for i in range (3,1000):
        count = 0
        for j in range(len(timedlist)-1):
            for k in range(j+1,len(timedlist)):
                if timedlist[j] + timedlist[k] == i:
                    count += 1
                if count > 1:
                    break
            if count > 1: break
        if count == 1:
            timedlist.append(i)
    for i in range(0,n):
        mainlist.append(timedlist[i])
    return mainlist


# ****************************************
# Problem 25
# ****************************************
def happy_number(n):
    """
    >>> happy_number(32)
    True
    >>> happy_number(33)
    False
    """

    return True


# ****************************************
# Problem 26
# ****************************************
def sum_of_divisors(n, lst):
    """
    Find and return sum of all odd numbers in the list, that are divisible by n.

    >>> sum_of_divisors(3, [2, 0, 1, 5])
    0
    >>> sum_of_divisors(5, [2, 0, 1, 5])
    5
    >>> sum_of_divisors(7, [])
    0

    """
    pass


# ****************************************
# Problem 27
# ****************************************
def turn_over(n, lst):
    """
    Reverse first n items of the list and return it. If n <= 0, return
    the empty list. Do not consume MORE than n items of iterable.

    >>> reverse(4, ['f', 'o', 'o', 't', 'b', 'a', 'l', 'l'])
    ['t', 'o', 'o', 'f', 'b', 'a', 'l', 'l']
    >>> reverse(5, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    [5, 4, 3, 2, 1, 6, 7, 8, 9, 10]
    >>> reverse(10, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    >>> reverse(-5, [])
    []

    """
    pass


# ****************************************
# Problem 28
# ****************************************
def generate_number(number, digit, position):
    """
    Take a number and returns a new one with a digit
    inserted in a given position if digit is bigger
    then initital digit in position

     >>> generate_number(3746, 5, 0)
    3746
    >>> generate_number(3746, 5, 1)
    3756
    >>> generate_number(3746, 5, 2)
    3746
    >>> generate_number(3746, 5, 3)
    5746
    >>> generate_number(3746, 5, 4)
    53746
    >>> generate_number(3746, 5, 7)
    50003746
    >>> generate_number(-12345, 9, 10)
    -90000012345
    """
    pass

# if __name__ == "__main__":
#   import doctest
#   print(doctest.testmod())
