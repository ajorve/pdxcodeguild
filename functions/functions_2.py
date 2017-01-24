"""
# Return the Sum of two or less elements using a default argument:
>>> combine(7, 4)
11

>>> combine(42)
42

# Return the sum of any number of integers using *args.
>>> combine_many(980, 667, 4432, 788, 122, 9, 545, 222)
7765

# Return the longest.
>>> choose_longer("Greg", "Rooney")
'Rooney'

>>> choose_longer("Greg", "Rooney", "Philip", "Maximus", "Gabrielle")
'Gabrielle'

>>> choose_longer("Greg", [0, 0, 0, 0, 4])
[0, 0, 0, 0, 4]

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
