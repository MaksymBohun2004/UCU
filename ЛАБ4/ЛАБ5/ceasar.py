import string
def caesar_encode(message,key):
    """ (str, int) -> str
    Encodes a message in caesar's cypher
    >>> print(caesar_encode("Caesars cypher encodes a message.", 4))
    Geiwevw gctliv irgshiw e qiwweki.
    """
    alphabet = []
    for i in range(key):
        for j in list(string.ascii_uppercase):
            alphabet.append(j)
    if isinstance(message , str) != True or isinstance(key,int) != True:
        return None
    letter_string =""
    for i in range(0,len(message)):
            if message[i] == " ":
                letter_string += " "
            elif message[i] == ".":
                letter_string += "."
            elif message[i] == message[i].lower():
                let = message[i]
                saui = string.ascii_lowercase.index(let)
                let_num = int((saui + key))
                letter_string += alphabet[let_num].lower()
            elif  message[i] == message[i].upper():
                let = message[i]
                saui = string.ascii_uppercase.index(let)
                let_num = int((saui + key))
                letter_string += alphabet[let_num]
    return letter_string
import string
def caesar_decode(message,key):
    """ (str, int) -> str
    Decodes a message in caesar's cypher
    >>> print(caesar_decode("Geiwevw gctliv irgshiw e qiwweki.", 4))
    Caesars cypher encodes a message.
    """
    alphabet = []
    for i in range(key):
        for j in list(string.ascii_uppercase):
            alphabet.append(j)
    if isinstance(message , str) != True or isinstance(key,int) != True:
        return None
    letter_string =""
    for i in range(0,len(message)):
            if message[i] == " ":
                letter_string += " "
            elif message[i] == ".":
                letter_string += "."
            elif message[i] == message[i].lower():
                let = message[i]
                saui = string.ascii_lowercase.index(let)
                let_num = int((saui - key))
                letter_string += alphabet[let_num].lower()
            elif  message[i] == message[i].upper():
                let = message[i]
                saui = string.ascii_uppercase.index(let)
                let_num = int((saui - key))
                letter_string += alphabet[let_num]
    return letter_string