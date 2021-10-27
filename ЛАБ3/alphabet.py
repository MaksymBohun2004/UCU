Alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
try:
    letter=int(input())
except ValueError:
    print("Incorrect Value")
temporary_letter = letter
string = 0
string_length = 0
letter_number = 0
while temporary_letter > 0:
    string += 1
    temporary_letter -= string
    string_length += 1
for i in range(1, string + 1):
    diversion = string_length - i
    letter_num = int(i)
    if letter_num > letter:
        letter_num = letter
    while letter_num > 0:
        if letter_num == 1:
            print("  " * diversion, Alphabet[letter_number], sep="")
        else:
            print("  " * diversion, Alphabet[letter_number], " ", end = "", sep="")
        diversion = 0
        letter_number += 1
        letter_num -= 1
        letter -= 1
    