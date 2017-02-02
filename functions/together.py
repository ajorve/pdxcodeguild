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

def together(x, y):
    for a, b in zip(x, y):
        print(a, b)


