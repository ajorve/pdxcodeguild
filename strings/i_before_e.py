"""
Check that a word follows "I before E except after C".

>>> check("recieve")
recieve doesn't follow the rule


>>> check("receive")
receive does follow the rule

"""

def check(word2):

    loc = word2.find('c')

    ei_loc = word2.find('ei')

    if loc + 1 == ei_loc:
        print("The word does follow the rule.")

    else:
        print("The word does not follow the rule.")
