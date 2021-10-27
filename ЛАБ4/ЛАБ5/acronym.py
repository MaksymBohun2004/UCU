
def create_acronym(message):
    r""" str -> str
    Takes names split by "newline" and returns acronyms.
    >>> print(create_acronym("random access memory\nAs soon As possible")) #doctest + ELLIPSIS
    RAM - random access memory
    ASAP - As soon As possible
    """
    message = message.split("\n")
    string = ""
    for i in message:
        if i != message[-1]:
            i = i.split()
            for j in i:
                string = string + j[0].upper()
            string = string + " - " + str(" ".join(i)) + "\n"
        else:
            i = i.split()
            for j in i:
                string = string + j[0].upper()
            string = string + " - " + str(" ".join(i))
    return string