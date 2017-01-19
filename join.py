"""
Write functions that convert two input args into kebab-case sting output.

>>> together('Chuck', 'Norris')
'Chuck-Norris'

>>> together("hello", 1)
'hello-1'

>>> together(40, 2)
'40-2'
"""

def together(word1, word2):
    words = [str(word1), str(word2)]
    join_words = "-".join(words)
    return join_words
