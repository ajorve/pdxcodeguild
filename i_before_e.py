"""
Check that a word follows "I before E except after C".

>>> check("recieve")
recieve doesn't follow the rule

>>> check("receive")
receive does follow the rule
"""
#
# def check(word):
#
#     if 'cei' in word:
#          pass
#     elif 'cie' in word:
#         pass
#     else:
#         raise ValueError("Cannot be done.")

def check(word2):

    loc = word2.find('c')

    ei_loc = word2.find('ei')

    if loc + 1 == ei_loc:
        print("The word does follow the rule.")

    else:
        print("The word does not follow the rule.")


    ##standard_rule = 'ei'
    ##exception_to_rule = 'ie'

    ##word check for standard_rule
    ##else return exception_to_rule

    ##if 'ie' in x =
    ##elif 'ei' in x =


