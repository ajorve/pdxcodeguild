"""
# Return the Sum of two or less elements:
>>> combine_two(7, 4)
11

>>> combine_two(42)
42

# Return the sum of any number of integers
>>> combine_many(980, 667, 4432, 788, 122, 9, 545, 222)
7765

# Return the longest string
>>> choose_longer("Dalton", "Clinton")
'Clinton'
"""

def combine_two(num1, num2=0):
    total = sum([num1, num2])
    return total

def combine_many(*args):
    numbers = sum(args)
    return numbers

def choose_longer(word1, word2):
    if len(word1) > len(word2):
        return word1
    else:
        return word2
