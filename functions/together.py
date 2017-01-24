"""
Use the zip() function!

>>> together('knights', 'camalot')
k c
n a
i m
g a
h l
t o
s t
"""

def together(*args):
    for x, y in zip('knights', 'camelot'):
        print(x, y)

together()
