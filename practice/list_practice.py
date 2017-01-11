"""
Given an input list, return it in reverse.
>>> backwards([56, 57, 58, 59, 60])
[60, 59, 58, 57, 56]


Find the max number in a given list.  Then, change every element in the list containing the first number of the maximum to the maximum number.
>>> maximus([56, 57, 58, 59, 60])
[60, 57, 58, 59, 60]

>>> maximus([56, 67, 56, 59, 60])
[67, 67, 67, 59, 67]


Given two lists, return True of the first two items are the equal.
>>> compare_first_element(['migratory', 'birds', 'fly', 'south'], ['migratory', 'monopoloy', 'mind'])
True

Return True if the first letter of the second element in the list is the same. (case insensitive)
>>> compare_second_letter(['migratory', 'penguins', 'fly', 'south'], ['One', 'Pound', 'Coconut'])
True

>>> compare_second_letter(['migratory', 'birds', 'fly', 'south'], ['One', 'Pound', 'Coconut'])
False


Given two lists, return one list, with all of the items of the first list, then the second
>>> smoosh(['mama', 'llama'], ['baba', 'yaga'])
['mama', 'llama', 'baba', 'yaga']


Use a default argument to allow the user to reverse the order!
>>> smoosh(['mama', 'llama'], ['baba', 'yaga'], reverse=True)
['yaga', 'baba', 'llama', 'mama']


"""

def backwards(input_list):
    input_list.reverse() # or [::-1]
     return input_list

def maximus(input_list):
    max_input = max(input_list)
    check_digit = str(max_input)[0]

    new_input_list = list()
    for each_number in input_list:
        if check_digit in str(each_number):
            new_input_list.append(max_input)
        else:
            new_input_list.append(each_number)
    return new_input_list

def compare_first_element(input_list1, input_list2):
    if input_list1[0].lower() == input_list2[0].lower():
        return True
    else:
        return False

def compare_second_letter(input_list1, input_list2):
    if input_list1[1][0].lower() == input_list2[1][0].lower():
        return True
    else:
        return False

def smoosh(input_list1, input_list2, reverse=False):
    smoosh_list = input_list1 + input_list2
    if reverse is True:
        input_list1.reverse() # or [::-1]
        input_list2.reverse() # or [::-1]
        smoosh_list = input_list2 + input_list1

    return smoosh_list
