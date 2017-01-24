"""
>>> arb(1, 2, 3, 4, 5, True, None, False, 'Python')
The 9 args are: (1, 2, 3, 4, 5, True, None, False, 'Python')

>>> arb(1, None)
The 2 args are: (1, None)


>>> stats(1, 67, 88, 44, 55, 33, 44, 22, 55, 7, 88, 9, 55, 66, 44, 33, 876)
Sum: 1587
Max: 876
Min: 1
Avg: 93
Range: 875
Entries: 17

"""


def arb(*args):
    print('The {a} args are: {b}'.format(a=len(args), b=args))

def stats(*args):
    max_range = max(args) # defines the max object range in list
    min_range = min(args) # defines the min object range in list.
    list_range = max_range - min_range

    print('Sum: {}'.format(sum(args)))
    print('Max: {}'.format(max(args)))
    print('Min: {}'.format(min(args)))
    print('Avg: {}'.format(sum(args) // len(args)))
    print('Range: {}'.format(list_range))
    print('Entries: {}'.format(len(args)))
