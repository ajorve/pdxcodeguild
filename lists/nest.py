"""
>>> letters = [['a', 'b', 'c'], ['d', 'e', 'f', 'g'], ['h', 'i']]

>>> denest()
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
"""


def nest():
    nested_letters = [x for y in LETTERS for x in y]
    return nested_letters

def denest():
    denested_letters = list()
    x = [x for each_letter in LETTERS for x in each_letter]

    return x
