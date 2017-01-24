"""
>>> squares
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

>>> square_halves
[2, 8, 18, 32, 50]

>>> names
['Kieran', 'Suki', 'Alex', 'Serada', 'Jeff', 'Fin', 'Alfonzo']

# Return a list of names that are least n charachters long.
>>> long_names(5)
['Kieran', 'Serada', 'Alfonzo']

>>> starts_with('S')
['Suki', 'Serada']

# Test Data Below.  Leave this line alone.
>>> people = [('Kieran', 'Prasch', 'Instructor'), ('Alfonzo', 'Ward', 'Student'), ('Fin', 'Balnik', 'Student')]

>>> last_names(people)
['Prasch', 'Ward', 'Balnik']

>>> smoosh(people)
['Kieran', 'Prasch', 'Instructor', 'Alfonzo', 'Ward', 'Student', 'Fin', 'Balnik', 'Student']

"""

squares = [i * i for i in range(1,11)]
square_halves = [i // 2 for i in squares[1::2]]
names = ['Kieran', 'Suki', 'Alex', 'Serada', 'Jeff', 'Fin', 'Alfonzo']

def long_names(num):
    name = [x for x in names if len(x) >= num]
    return name

def starts_with(letter):
    name = [x for x in names if x[0] == letter]
    return name

def last_names(people):
    name = [x[1] for x in people]
    return name

def smoosh(people):
    denested_people = list()
    name = [x for x in people for x in x]
    print(name)
