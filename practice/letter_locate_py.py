"""
Write a function to return a list of integers
indicating the index of each letter occourance in a given test string.

>>> locate('l', 'hello')
[2, 3]

>>> locate('b', 'bananas')
[0]

>>> locate('i', 'mississippi')
[1, 4, 7, 10]

>>> locate('l', 'llama')
[0, 1]

>>> locate('l', 'killer')
[2, 3]

"""

def locate(letter, thing):
