"""
Implement solutions in as many ways as possible.

- Increment
- Enumerate
- Range
- For Each

>>> a = 'music'
>>> b = [17, 28, 42, 31, 12]

>>> display_indexes(a)
m 0
u 1
s 2
i 3
c 4


>>> parallel(a, b)
m 17
u 28
s 42
i 31
c 12

"""

def display_indexes(index_a):
    for index, letter in enumerate(index_a):
        print(letter, index)

def parallel(index_a, index_b):
    for x, y in zip(index_a, index_b):
        print(x, y)

def index_range(index_a, index_b):
    combined_indexes = index_a + index_b
    for index, x in range(combined_indexes):
        print(x)
