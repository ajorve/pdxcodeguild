"""
Write functions that convert two input args into kebab-case sting output.

>>> link('Chuck', 'Norris')
'Chuck-Norris'

>>> link("hello", 1)
'hello-1'

>>> link(40, 2)
'40-2'
"""

def together(word1, word2):
    words = [str(word1), str(word2)]
    join_words = "-".join(words)
    return join_words
