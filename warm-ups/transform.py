"""
Python

'horse' == 'h3e'

'duck' == 'd2k'

'student' == 's5t'

Write a function that will provide the following result.

"""

def transform(word):
    first_letter = str(word[0])
    last_letter = str(word[-1])
    length_middle = len(word) -2
    transformed = "".join(first_letter, str(length_middle), last_letter)
    return transformed
