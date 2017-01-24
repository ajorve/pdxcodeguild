"""
Return the number of letter occourances in a string.
>>> count_letter('i', 'Antidisestablishmentterianism')
5
>>> count_letter('p', 'Pneumonoultramicroscopicsilicovolcanoconiosis')
2


Return the letter that appears last in the engligh alphabet.
>>> latest_letter('pneumonoultramicroscopicsilicovolcanoconiosis')
the latest letter is v.


Convert input strings to lowercase without any surrounding whitespace.
>>> lower_case("SUPER!")
'super!'
>>> lower_case("        NANNANANANA BATMAN        ")
'nannananana batman'

"""

def count_letter(letter, word):
    number = word.lower().count(letter)
    return(number)

def latest_letter(word):
    number = max(word)
    message = "the latest letter is {}.".format(number)
    print(message)

def lower_case(word):
    result = word.lower().strip()
    return(result)
