"""
Return a list with *each* element multiplied by n.
If the product is 0, do not include it in the output list.

This type of operation is known as "mapping."

#  Leave the line beloe alone, it is test data.
>>> llamas = [45, 37, 96, 23, 55, 2, 0, 88, 0, 45, 0, 345, 1, 76, 45, 34, 87]

>>> apply_to_all(llamas, 2)
[90, 74, 192, 46, 110, 4, 176, 90, 690, 2, 152, 90, 68, 174]

"""

def apply_to_all(llamas, n):
    my_list = list()
    for each_number in llamas:
        if each_number > 0:
            my_list.append(each_number * n)
        else:
            continue
    return my_list
