"""
Write a function to return a list of integers
indicating the index of each letter occourance in a given test string.

>>> locate('l', 'hello')
[2, 3]

>>> locate('b', 'bannanas')
[0]

>>> locate('i', 'mississippi')
[1, 4, 7, 10]
"""

def locate(check, word):
    word_list = list()
    for index, letter in enumerate(word):
        if letter == check:
            word_list.append(index)
    print(word_list)
