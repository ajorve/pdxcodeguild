"""
>>> a
'music'

>>> b
[17, 28, 42, 31, 12]

>>> spell_out(a)
m
u
s
i
c

>>> spell_out(b)
17
28
42
31
12

>>> first_and_last(b)
17
12

>>> first_and_last(a)
m
c

"""

a = 'music'
b = [17, 28, 42, 31, 12]

def spell_out(llama):
    for x in llama:
        print(x)

def first_and_last(llama):
        first = llama[0]
        last = llama[-1]
        print(first)
        print(last)
